from decimal import Decimal
from math    import pi

from rooms.models  import Gu, Dong, Room
from search.models import Amenity
from mysettings    import MEAN_EARTH_RADIUS, ZOOM_DICT

def get_map_data(latitude, longitude, zoom, q):
    
    view_size = ZOOM_DICT[zoom]['view_size']
    MIN_LAT   = latitude  - Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    MAX_LAT   = latitude  + Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    MIN_LNG   = longitude - Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    MAX_LNG   = longitude + Decimal(view_size / MEAN_EARTH_RADIUS * (180/pi))
    
    if ZOOM_DICT[zoom]['boxsize'] == '구':
        gu_list   = Gu.objects.filter(latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG))
        room_list = Room.objects.filter(q, latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG), id__lte = 600).distinct()
        result = [{
                "name"      : gu.name,
                "latitude"  : float(gu.latitude),
                "longitude" : float(gu.longitude),
                "room_id"   : [room.id for room in room_list if room.legalcode.gu_type_id == gu.id]
                } for gu in gu_list]
    
    if ZOOM_DICT[zoom]['boxsize'] == '동' or type(ZOOM_DICT[zoom]['boxsize']) == int:
        dong_list = Dong.objects.filter(latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG))
        room_list = Room.objects.filter(q, latitude__range = (MIN_LAT, MAX_LAT), longitude__range = (MIN_LNG, MAX_LNG), id__lte = 600).distinct()
        result = [{
                "name"      : dong.name,
                "latitude"  : float(dong.latitude),
                "longitude" : float(dong.longitude),
                "room_id"   : [room.id for room in room_list if room.legalcode.id == dong.id]
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
        "room_list" : result,
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