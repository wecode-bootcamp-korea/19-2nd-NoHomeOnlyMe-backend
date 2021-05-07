from rooms.models import Room

def get_room_list(room_id):
    
    if not room_id:
        return {"results" : []}
    
    room_list = [Room.objects.get(id = id) for id in room_id]
    
    result = [{
        "id"               : room.id,
        "image_url"        : [image.image_url for image in room.image_set.select_related().all()],
        "sale_type"        : room.saleinformation_set.select_related().first().sale_type.name,
        "deposit"          : int(room.saleinformation_set.select_related().first().deposit),
        "monthly_pay"      : int(room.saleinformation_set.select_related().first().monthly_pay),
        "room_type"        : room.room_type.name,
        "exclusive_m2"     : float(room.roominformation_set.select_related().first().exclusive_m2),
        "maintenance_cost" : int(room.additionalinformation_set.select_related().first().maintenance_cost)
        }
        if room.saleinformation_set.select_related().first().sale_type.name == '월세'
        else
        {
        "id"               : room.id,
        "image_url"        : [image.image_url for image in room.image_set.select_related().all()],
        "sale_type"        : room.saleinformation_set.select_related().first().sale_type.name,
        "deposit"          : int(room.saleinformation_set.select_related().first().deposit),
        "monthly_pay"      : None,
        "room_type"        : room.room_type.name,
        "exclusive_m2"     : float(room.roominformation_set.select_related().first().exclusive_m2),
        "maintenance_cost" : int(room.additionalinformation_set.select_related().first().maintenance_cost)
        } for room in room_list]
    
    return {"results" : result}