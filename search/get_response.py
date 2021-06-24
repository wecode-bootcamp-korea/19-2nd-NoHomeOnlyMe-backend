from decimal import Decimal
from math    import pi

from django.http.response import JsonResponse

from search.models import Amenity, AmenityType
from homes.models  import GuType, DongType, Home
from mysettings    import MEAN_EARTH_RADIUS, ZOOM_DICT

def get_response(latitude, longitude, zoom, q):
    
    view_size = ZOOM_DICT[zoom]['view_size']
    MIN_LAT   = latitude  - Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    MAX_LAT   = latitude  + Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    MIN_LNG   = longitude - Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    MAX_LNG   = longitude + Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    
    if ZOOM_DICT[zoom]['boxsize'] == '구':
        gu_list   = GuType.objects.filter(latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG))
        home_list = Home.objects.filter(q, latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG), id__lte = 600).distinct()
        room_list = [{
                "name"      : gu.name,
                "latitude"  : float(gu.latitude),
                "longitude" : float(gu.longitude),
                "room_id"   : [home.id for home in home_list if home.legalcode.gu_type_id == gu.id]
                } for gu in gu_list]
    
    if ZOOM_DICT[zoom]['boxsize'] == '동' or type(ZOOM_DICT[zoom]['boxsize']) == int:
        dong_list = DongType.objects.filter(latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG))
        home_list = Home.objects.filter(q, latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG), id__lte = 600).distinct()
        room_list = [{
                "name"      : dong.name,
                "latitude"  : float(dong.latitude),
                "longitude" : float(dong.longitude),
                "room_id"   : [home.id for home in home_list if home.legalcode.id == dong.id]
                } for dong in dong_list]
    
    subway_list = Amenity.objects.filter(latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG), type_id = 1)
    univ_list = Amenity.objects.filter(latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG), type_id = 2)
    
    SLICING = 10
    subway_list = [subway for subway in subway_list if subway.id % SLICING == 0]
    univ_list = [univ for univ in univ_list if univ.id % SLICING == 0]
    
    results = {
        "center" : {
            "latitude"  : float(latitude),
            "longitude" : float(longitude)},
        "zoom" : zoom,
        "room_list" : room_list,
        "subway_list" : [{
            "name"      : subway.name,
            "latitude"  : float(subway.latitude),
            "longitude" : float(subway.longitude)
            } for subway in subway_list],
        "univ_list" : [{
            "name"      : univ.name,
            "latitude"  : float(univ.latitude),
            "longitude" : float(univ.longitude)
            } for univ in univ_list]
        }
    return results

def get_room_list(room_id):
    
    if room_id == 0:
        return {"results" : []}
    
    home_list = [Home.objects.get(id = id) for id in room_id]
    
    room_list = [{
        "id"               : home.id,
        "image_url"        : [image.image_url for image in home.image_set.select_related().all()],
        "sale_type"        : home.saleinformation_set.select_related().first().sale_type.name,
        "deposit"          : int(home.saleinformation_set.select_related().first().deposit),
        "monthly_pay"      : int(home.saleinformation_set.select_related().first().monthly_pay),
        "room_type"        : home.room_type.name,
        "exclusive_m2"     : float(home.roominformation_set.select_related().first().exclusive_m2),
        "maintenance_cost" : int(home.additionalinformation_set.select_related().first().maintenance_cost)
        }
        if home.saleinformation_set.select_related().first().sale_type.name == '월세'
        else
        {
        "id"               : home.id,
        "image_url"        : [image.image_url for image in home.image_set.select_related().all()],
        "sale_type"        : home.saleinformation_set.select_related().first().sale_type.name,
        "deposit"          : int(home.saleinformation_set.select_related().first().deposit),
        "monthly_pay"      : None,
        "room_type"        : home.room_type.name,
        "exclusive_m2"     : float(home.roominformation_set.select_related().first().exclusive_m2),
        "maintenance_cost" : int(home.additionalinformation_set.select_related().first().maintenance_cost)
        } for home in home_list]
    
    return {"results" : room_list}