from decimal import Decimal
from math    import pi
from django.db import connection, reset_queries
from django.db.models import Q

from rooms.models  import (Gu, Dong)
from search.models import Amenity
from .const        import (CODES, EARTH_MEAN_RADIUS, ZOOM_DICT)

def get_mapview_results(q : Q, **center_and_zoom : dict) -> dict:
    
    zoom      = center_and_zoom["zoom"]
    latitude  = center_and_zoom["center"]["latitude"]
    longitude = center_and_zoom["center"]["longitude"]
    view_size = ZOOM_DICT[zoom]['view_size']
    
    BOX_SIZE = ZOOM_DICT[zoom]['box_size']
    MIN_LAT  = latitude  - Decimal(view_size / EARTH_MEAN_RADIUS * (180/pi))
    MAX_LAT  = latitude  + Decimal(view_size / EARTH_MEAN_RADIUS * (180/pi))
    MIN_LNG  = longitude - Decimal(view_size * 0.625 / EARTH_MEAN_RADIUS * (180/pi))
    MAX_LNG  = longitude + Decimal(view_size * 0.625 / EARTH_MEAN_RADIUS * (180/pi))
    reset_queries()
    subway_list = [{
        "name"      : subway.name,
        "latitude"  : subway.latitude,
        "longitude" : subway.longitude,
        } for subway in Amenity.objects.filter(
            longitude__range = (MIN_LAT, MAX_LAT),
            latitude__range   = (MIN_LNG, MAX_LNG),
            amenity_type__name = "지하철역")
        ]
    subway_query_count = len(connection.queries)
    reset_queries()
    
    univ_list = [{
        "name"      : univ.name,
        "latitude"  : univ.latitude,
        "longitude" : univ.longitude,
        } for univ in
            Amenity.objects.filter(
                latitude__range    = (MIN_LAT, MAX_LAT), 
                longitude__range   = (MIN_LNG, MAX_LNG),
                amenity_type__name = "대학교")
            ]
    univ__query_count = len(connection.queries)
    reset_queries()
    
    if BOX_SIZE == "구":
        model = Gu
    elif BOX_SIZE == "동":
        model = Dong
    else: # 추가 구현 필요 -> zoom 단계가 16이상일 때 modeling 변경 및 결과 로직 추가
        model = Dong
        
    circles = [{
        "name"      : model.name,
        "latitude"  : float(model.latitude),
        "longitude" : float(model.longitude),
        "count"    : len(model.rooms.filter(q))
        } for model in
            model.objects.filter(
                latitude__range  = (MIN_LAT, MAX_LAT), 
                longitude__range = (MIN_LNG, MAX_LNG))
            ]
    circle_query_count = len(connection.queries)
    reset_queries
    results = {
        "circle_query_count" : circle_query_count,
        "subway_query_count" : subway_query_count,
        "univ__query_count" : univ__query_count,
        "code"        : CODES["OK"],
        "circles"     : circles,
        "center"      : {
            "latitude"  : float(latitude),
            "longitude" : float(longitude),
            },
        "subway_list" : subway_list,
        "univ_list"   : univ_list,
        "zoom"        : zoom,
        }
    
    return results