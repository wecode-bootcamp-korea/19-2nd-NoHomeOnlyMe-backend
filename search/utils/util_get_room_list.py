from django.db.models import Q

from .            import CODES, ZOOM_DICT
from rooms.models import *

def get_room_list(circle_id : int, zoom : int) -> dict:
    
    box_size = ZOOM_DICT[zoom]["box_size"]
    if box_size == "구":
        q = Q(gu_id = circle_id) # 추가 구현 필요 -> 실제 서비스에서는 "구" 단위의 매물 리스트 정보 제공을 하지 않음
    if box_size == "동":
        q = Q(dong_id = circle_id)
    if type(box_size) == int: # 추가 구현 필요 -> zoom 단계가 16이상일 때 rectangle section modeling 변경 및 결과 로직 추가 
        q = Q(dong_id = circle_id)
    
    room_list = Room.objects.filter(q)
    
    try:
        room_contants = [{
            "deposit"          : float((sale_info := room.sale_info.first()).deposit),
            "title"            : room.description.title,
            "exclusive_m2"     : float(room.room_info.exclusive_m2),
            "id"               : room.id,
            "image"            : room.images.order_by("sequence").first().image_url,
            "maintenance_cost" : int(room.additional_info.maintenance_cost),
            "monthly_pay"      : float(sale_info.monthly_pay),
            "room_type"        : room.room_type.name,
            "sale_type"        : sale_info.sale_type.name,
            } for room in room_list]
        
        return {
            "CODE"      : CODES["OK"],
            "room_list" : room_contants,
            }
    
    except Exception:
        return {
            "CODE"      : CODES["INVALID KEYWORD"],
            "room_lost" : []
        }