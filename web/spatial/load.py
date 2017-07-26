import os
from django.contrib.gis.utils import LayerMapping
from django.db.models import Count
from .models import Area, VotingDistrict
from promises.models import Person
from django.contrib.gis import geos

mapping = {
    'area_id' : 'ADM_DR_CD',
    'name' : 'ADM_DR_NM',
    'voting_district_name' : 'precinct_n',
    'province' : 'province',
    'precinct' : 'SGG_NM',
    'mpoly' : 'MULTIPOLYGON',
}

def run(shp_file, verbose=True):
    Area.objects.all().delete()
    lm = LayerMapping(
        Area, shp_file, mapping,
        encoding='utf-8',
        transform=False,
    )
    lm.save(strict=True, verbose=verbose)

    voting_districts()
    elected_members()

def voting_districts():
    voting_districts = Area.objects.values('voting_district_name').annotate(count=Count("id"))
    for district in voting_districts:
        name = district['voting_district_name']
        areas = Area.objects.filter(voting_district_name=name)
        # Union all areas
        union = areas[0].mpoly
        for area in areas[1:]:
            union = union.union(area.mpoly)
        if union and isinstance(union, geos.Polygon):
            union = geos.MultiPolygon(union)
        # Save district
        v = VotingDistrict(name=name, mpoly=union)
        v.save()
        v.areas = areas
        v.save()
        print("Imported %s with %d areas" % (name, district['count']))

def elected_members():
    f = open("/data/voting-districts/results.txt")
    results = dict([line.split() for line in f])
    for v in VotingDistrict.objects.all():
        if v.name not in results:
            print("Missing result for %s" % v.name)
            continue
        member_name = results.get(v.name)
        member = Person(name=member_name, mop_for_district=v)
        member.save()
