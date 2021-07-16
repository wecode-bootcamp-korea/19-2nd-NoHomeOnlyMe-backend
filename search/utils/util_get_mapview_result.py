from decimal import Decimal
from math    import pi

from django.db.models import Q

from .             import (CODES, EARTH_MEAN_RADIUS, ZOOM_DICT)
from rooms.models  import (Gu, Dong)
from search.models import Amenity

def get_mapview_results(q : Q, **center_and_zoom : dict) -> dict:
    
    zoom      = center_and_zoom["zoom"]
    latitude  = center_and_zoom["center"]["latitude"]
    longitude = center_and_zoom["center"]["longitude"]
    view_size = ZOOM_DICT[zoom]["view_size"]
    box_size  = ZOOM_DICT[zoom]["box_size"]
    min_lat   = latitude  - Decimal(view_size / EARTH_MEAN_RADIUS * (180/pi))
    max_lat   = latitude  + Decimal(view_size / EARTH_MEAN_RADIUS * (180/pi))
    # 16:9 화면 비에 맞춘 lat/lng 제한 설정
    min_lng   = longitude - Decimal(view_size * 0.625 / EARTH_MEAN_RADIUS * (180/pi))
    max_lng   = longitude + Decimal(view_size * 0.625 / EARTH_MEAN_RADIUS * (180/pi))
    
    subway_list = [{
        "amenity_id" : subway.id,
        "latitude"   : subway.latitude,
        "longitude"  : subway.longitude,
        "name"       : subway.name,
        } for subway in Amenity.objects.filter(
            latitude__range    = (min_lat, max_lat),
            longitude__range   = (min_lng, max_lng),
            amenity_type__name = "지하철역"
            )
        ]
    
    univ_list = [{
        "amenity_id" : univ.id,
        "latitude"   : univ.latitude,
        "longitude"  : univ.longitude,
        "name"       : univ.name,
        } for univ in Amenity.objects.filter(
            latitude__range    = (min_lat, max_lat), 
            longitude__range   = (min_lng, max_lng),
            amenity_type__name = "대학교"
            )
        ]
    
    if box_size == "구":
        model = Gu
    elif box_size == "동":
        model = Dong
    else: # 추가 구현 필요 -> zoom 단계가 16이상일 때 rectangle section modeling 변경 및 결과 로직 추가
        model = Dong
        
    circles = [
        {
            "count"     : len(model.rooms.filter(q)),
            "circle_id" : model.id,
            "latitude"  : float(model.latitude),
            "longitude" : float(model.longitude),
            "name"      : model.name,
            } for model in model.objects.filter(
                latitude__range  = (min_lat, max_lat), 
                longitude__range = (min_lng, max_lng)
                )
            ]
    
    results = {
        "code"        : CODES["OK"],
        "center"      : {
            "latitude"  : float(latitude),
            "longitude" : float(longitude),
            },
        "circles"     : circles,
        "subway_list" : subway_list,
        "univ_list"   : univ_list,
        "zoom"        : zoom,
        }
    
    return results