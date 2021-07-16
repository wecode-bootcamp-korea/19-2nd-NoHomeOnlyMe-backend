from haversine import haversine

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from rooms.models  import Room
from search.models import Amenity

class RoomDetailView(View):
    def get(self, request, room_id):
        try:
            if not Room.objects.filter(id=room_id).exists():
                return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

            room = Room.objects.get(id=room_id)

            # move_in_date가 "날짜 선택"일 경우, 날짜로 표기
            move_in_date = room.roominformation_set.first().move_in_option.name
            if move_in_date == "날짜 선택":
                move_in_date = room.roominformation_set.first().move_in_date

            # house_type이 null일 때, room_type 이름 표기
            if room.house_type:
                house_type = room.house_type.name
            else:
                house_type = room.room_type.name

            MAP_DISTANCE_KM = 20

            map_center        = (float(room.latitude), float(room.longitude))
            map_latitude_min  = float(room.latitude) - 0.01 * MAP_DISTANCE_KM
            map_latitude_max  = float(room.latitude) + 0.01 * MAP_DISTANCE_KM
            map_longitude_min = float(room.longitude) - 0.015 * MAP_DISTANCE_KM
            map_longitude_max = float(room.longitude) + 0.015 * MAP_DISTANCE_KM

            amenity_filter = Amenity.objects.filter(
                Q(latitude__range=(map_latitude_min, map_latitude_max)) and
                Q(longitude__range=(map_longitude_min, map_longitude_max))
            )

            result = {
                "room_id"       : room.id,
                "detail_header" : {
                    "room_type"        : room.room_type.name,
                    "name"             : room.name,
                    "sale_type"        : room.saleinformation_set.first().sale_type.name,
                    "deposit"          : room.saleinformation_set.first().deposit,
                    "monthly_pay"      : room.saleinformation_set.first().monthly_pay,
                    "exclusive_m2"     : float(room.roominformation_set.first().exclusive_m2),
                    "exclusive_pyeong" : room.roominformation_set.first().exclusive_pyeong,
                    "month_total_cost" : (int(room.saleinformation_set.first().monthly_pay) \
                                    + int(room.additionalinformation_set.first().maintenance_cost) \
                                    + int(room.additionalinformation_set.first().parking_fee))/1000,
                    "user_name"        : room.user.name,
                },
                "detail_info"   : {
                    "floor"            : room.roominformation_set.first().floor,
                    "building_story"   : room.roominformation_set.first().building_story,
                    "exclusive_m2"     : float(room.roominformation_set.first().exclusive_m2),
                    "supply_m2"        : float(room.roominformation_set.first().supply_m2),
                    "exclusive_pyeong" : room.roominformation_set.first().exclusive_pyeong,
                    "supply_pyeong"    : room.roominformation_set.first().supply_pyeong,
                    "heating_type"     : room.roominformation_set.first().heating_type,
                    "parking"          : room.additionalinformation_set.first().checkadditionaloption_set
                                        .filter(additional_option__name__contains="주차").first().is_able,
                    "pet"              : room.additionalinformation_set.first().checkadditionaloption_set
                                        .filter(additional_option__name__contains="반려동물").first().is_able,
                    "elevator"         : room.additionalinformation_set.first().checkadditionaloption_set
                                        .filter(additional_option__name__contains="엘리베이터").first().is_able,
                    "move_in_date"     : move_in_date,
                    "house_type"       : house_type
                },
                "detail_images" : [ { "url": image.image_url } for image in room.image_set.all() ],
                "maps"          : {
                    "road_address"  : room.road_address,
                    "center"            : {
                        "latitude"  : float(room.latitude),
                        "longitude" : float(room.longitude),
                    },
                    "convenience_store" : [{
                        "latitude"  : float(amenity.latitude),
                        "longitude" : float(amenity.longitude),
                    } for amenity in amenity_filter.filter(type__name__contains="편의점")
                    if haversine(map_center, (amenity.latitude, amenity.longitude)) <= MAP_DISTANCE_KM ],
                    "subway"            : [{
                        "latitude"  : float(amenity.latitude),
                        "longitude" : float(amenity.longitude),
                    } for amenity in amenity_filter.filter(type__name__contains="지하철")
                    if haversine(map_center, (amenity.latitude, amenity.longitude)) <= MAP_DISTANCE_KM ],
                    "university"        : [{
                        "latitude"  : float(amenity.latitude),
                        "longitude" : float(amenity.longitude),
                    } for amenity in amenity_filter.filter(type__name__contains="대학교")
                    if haversine(map_center, (amenity.latitude, amenity.longitude)) <= MAP_DISTANCE_KM ],
                },
                "other_rooms"   : [],
            }

            # 동일한 유저가 올린 다른 매물
            if Room.objects.filter(user_id = room.user_id).count() > 1:
                result["other_rooms"] = [{
                    "room_id"          : other_room.id,
                    "image"            : other_room.image_set.first().image_url,
                    "room_type"        : other_room.room_type.name,
                    "sale_type"        : other_room.saleinformation_set.first().sale_type.name,
                    "deposit"          : other_room.saleinformation_set.first().deposit,
                    "monthly_pay"      : other_room.saleinformation_set.first().monthly_pay,
                    "floor"            : other_room.roominformation_set.first().floor,
                    "exclusive_m2"     : float(room.roominformation_set.first().exclusive_m2),
                    "maintenance_cost" : int(room.additionalinformation_set.first().maintenance_cost),  
                } for other_room in Room.objects.filter(id__gte = 6500, user_id = room.user_id) if other_room.id != room_id][:4]

            return JsonResponse({"RESULT": result}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"RESULT": e}, status=200)