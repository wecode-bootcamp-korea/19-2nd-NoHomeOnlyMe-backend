from decimal import Decimal

from django.db.models     import Q
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.views         import View

from search.utils  import (CODES, get_mapview_results, filter_keyword, DEFAULT_MAP_POINT, search_keyword)

class MapView(View):
    def get(self, request):
        try:
            
            center = request.GET.get("center")
            zoom   = request.GET.get("zoom")
            q      = Q()
            
            if center and zoom:
                if center.find(",") == -1:
                    return HttpResponseBadRequest("Worng center form")
                
                lat, lng  = center.split(",")
                center_and_zoom = {
                    "code"   : CODES["OK"],
                    "center" : {
                        "latitude"  : Decimal(lat),
                        "longitude" : Decimal(lng),
                        },
                    "zoom"   : int(zoom),
                    }
                if request.GET.get("keyword"):
                    center_and_zoom = search_keyword(request.GET.get("keyword"))
                
                filter_values = {
                    "room_type"        : request.GET.get('room_type'),
                    "sale_type"        : request.GET.get('sale_type'),
                    "deposit"          : request.GET.get('deposit'),
                    "monthly_pay"      : request.GET.get('monthly_pay'),
                    "maintenance_cost" : request.GET.get('maintenance_cost'),
                    "exclusive_m2"     : request.GET.get('exclusive_m2'),
                    }
                
                filtering_result = filter_keyword(q, **filter_values)
                
                if center_and_zoom["code"] == 200:
                    return JsonResponse(get_mapview_results(filtering_result, **center_and_zoom),
                                        status = CODES["OK"])
                
                elif center_and_zoom["code"] == 400:
                    return HttpResponseBadRequest("INVALID KEYWORD")
                
                elif center_and_zoom["code"] == 404:
                    return HttpResponseNotFound("RESOURCE NOT FOUND")
            
            if not center and not zoom:
                center_and_zoom = {
                    "center" : {
                        "latitude"  : DEFAULT_MAP_POINT["center"]["latitude"],
                        "longitude" : DEFAULT_MAP_POINT["center"]["longitude"],
                        },
                    "zoom"   : DEFAULT_MAP_POINT["zoom"],
                    }
                
                return JsonResponse(get_mapview_results(q, **center_and_zoom),
                                    status = CODES["OK"])
            
            if not center or not zoom:
                return HttpResponseBadRequest("NO zoom or coords")
            
        except Exception as e:
            HttpResponse(f"{e}", status = 400)