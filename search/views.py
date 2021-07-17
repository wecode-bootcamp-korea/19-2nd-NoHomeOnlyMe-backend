import re
import json

from random  import shuffle
from decimal import Decimal

from django.http.response import JsonResponse
from django.views         import View
from django.db.models     import Q

from .models       import Amenity, AmenityType
from homes.models  import DongType, GuType, Home
from .get_response import get_response, get_room_list
from mysettings    import DEFAULT_MAP_POINT, SEARCH_ZOOM_INIT, ZOOM_DICT

class MapView(View):
    def get(self, request):
        try:
            if not request.GET.get('center') and not request.GET.get('zoom'):
                latitude    = DEFAULT_MAP_POINT['center']["latitude"]
                longitude   = DEFAULT_MAP_POINT['center']["longitude"]
                zoom        = DEFAULT_MAP_POINT["zoom"]
                q           = Q()
                
                return JsonResponse(get_response(latitude, longitude, zoom, q), status = 200)
            
            coords           = request.GET.get('center')
            zoom             = int(request.GET.get('zoom'))
            room_type        = request.GET.get('room_type')
            sale_type        = request.GET.get('sale_type')
            deposit          = request.GET.get('deposit')
            monthly_pay      = request.GET.get('monthly_pay')
            maintenance_cost = request.GET.get('maintenance_cost')
            exclusive_m2     = request.GET.get('exclusive_m2')
            
            if coords.find(',') != -1:
                lat, lng  = coords.split(',')
                latitude  = Decimal(lat)
                longitude = Decimal(lng)
            
            q = Q()
            if room_type:
                room_types = room_type.split(',')
                q |= Q(room_type__name__in = room_types)
            
            if sale_type:
                sale_types  = sale_type.split(',')
                q |= Q(saleinformation__sale_type__name__in = sale_types)
                
            if deposit and deposit.find(',') != -1:
                deposit_list = deposit.split(',')
                MIN_DEPOSIT  = Decimal(min(deposit_list))
                MAX_DEPOSIT  = Decimal(max(deposit_list))
                q |= Q(saleinformation__deposit__range = (MIN_DEPOSIT, MAX_DEPOSIT))
                
            if monthly_pay and monthly_pay.find(',') != -1:
                monthly_pay_list = monthly_pay.split(',')
                MIN_MONTHLY_PAY  = Decimal(min(monthly_pay_list))
                MAX_MONTHLY_PAY  = Decimal(max(monthly_pay_list))
                q |= Q(saleinformation__monthly_pay__range = (MIN_MONTHLY_PAY, MAX_MONTHLY_PAY))
            
            if maintenance_cost and maintenance_cost.find(',') != -1:
                maintenance_cost_list = maintenance_cost.split(',')
                MIN_MAINTENANCE_COST  = Decimal(min(maintenance_cost_list))
                MAX_MAINTENANCE_COST  = Decimal(max(maintenance_cost_list))
                q |= Q(additionalinformation__maintenance_cost__range = (MIN_MAINTENANCE_COST, MAX_MAINTENANCE_COST))
            
            if exclusive_m2 and exclusive_m2.find(',') != -1:
                exclusive_m2_list = exclusive_m2.split(',')
                MIN_EXCLUSIVE_M2  = Decimal(min(exclusive_m2_list))
                MAX_EXCLUSIVE_M2  = Decimal(max(exclusive_m2_list))
                q |= Q(roominformation__exclusive_m2__range = (MIN_EXCLUSIVE_M2, MAX_EXCLUSIVE_M2))
            
            search            = request.GET.get('search')
            compiler_gutype   = re.compile('^[가-힣]+구$')
            compiler_dongtype = re.compile('^[가-힣]+동$')
            compiler_subway   = re.compile('^[가-힣]+역$')
            compiler_univ     = re.compile('^[가-힣]+[대학교]$')
            
            if search:
                if re.match(compiler_dongtype, search):
                    legalcode = DongType.objects.get(name = search)
                    latitude  = Decimal(legalcode.latitude)
                    longitude = Decimal(legalcode.longitude)
                    zoom      = SEARCH_ZOOM_INIT['dong_type']
                    
                    return JsonResponse(get_response(latitude, longitude, zoom, q), status = 200)
                
                elif re.match(compiler_subway, search):
                    amenity   = Amenity.objects.get(name__contains = search, amenity_type = AmenityType.objects.get(name='지하철역'))
                    latitude  = Decimal(amenity.latitude)
                    longitude = Decimal(amenity.longitude)
                    zoom      = SEARCH_ZOOM_INIT["amenity"]
                    
                    return JsonResponse(get_response(latitude, longitude, zoom, q), status = 200)
                
                elif re.match(compiler_univ, search):
                    words     = list(search)
                    q        &= Q(name__contains__in = words)
                    amenity   = Amenity.objects.filter(q, type = AmenityType.objects.get(name='대학교')).first()
                    latitude  = Decimal(amenity.latitude)
                    longitude = Decimal(amenity.longitude)
                    zoom      = SEARCH_ZOOM_INIT["amenity"]
                    
                    return JsonResponse(get_response(latitude, longitude, zoom, q), status = 200)
                
                elif re.match(compiler_gutype, search):
                    search = search.replace('구', '')
                    if Amenity.objects.filter(name__contains = search).exists:
                        search    = search.replace('구', '')
                        amenity   = Amenity.objects.filter(name__contains = search).first()
                        latitude  = Decimal(amenity.latitude)
                        longitude = Decimal(amenity.longitude)
                        zoom      = SEARCH_ZOOM_INIT["amenity"]
                    else:
                        legalcode = GuType.objects.get(name = search).dong_type_set.select_related().first()
                        latitude  = Decimal(legalcode.latitude)
                        longitude = Decimal(legalcode.longitude)
                        zoom      = SEARCH_ZOOM_INIT["dong_type"]
                    
                    return JsonResponse(get_response(latitude, longitude, zoom, q), status = 200)
                
                else:
                    return JsonResponse({"message" : "Invalid search word"}, status = 400)
                
            return JsonResponse(get_response(latitude, longitude, zoom, q), status = 200)
    
        except Exception as e:
            print(e)
            return JsonResponse({"message" : e}, status = 400)

class RoomListView(View):
    def get(self, request):
        try:
            if not request.GET.get('room_id'):
                room_id = list(range(1, len(Home.objects.all())))
                
                return JsonResponse(get_room_list(room_id[:200]), status = 200)
            
            room_id = request.GET.get('room_id').split(',')
            return JsonResponse(get_room_list(room_id), status = 200)
        
        except KeyError:
            return JsonResponse({"message" :  "Keyerror"}, status = 400)
        
        except Exception:
            return JsonResponse({"message" :  "something error"}, status = 400)