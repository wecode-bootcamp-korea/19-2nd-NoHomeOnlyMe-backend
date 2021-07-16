from django.http.response import (Http404, HttpResponseBadRequest, JsonResponse)
from django.views         import View

from search.utils import CODES, get_room_list, DEFAULT_MAP_POINT, ZOOM_DICT

class RoomListView(View):
    def get(self, request):
        circle_id = request.GET.get("circle_id")
        zoom      = request.GET.get("zoom")
        
        if zoom:
            if int(zoom) not in list(ZOOM_DICT.keys()):
                zoom = DEFAULT_MAP_POINT["zoom"]
        
        if not zoom or not circle_id:
            return HttpResponseBadRequest("No circle id or zoom")
        
        circle_id = int(circle_id)
        zoom      = int(zoom)
        
        result = get_room_list(circle_id, zoom)
        if result["CODE"] == 200:
            return JsonResponse(result, status = result["CODE"])
        
        if result["CODE"] == 400:
            return HttpResponseBadRequest(f"{CODES[400]}")
        
        if result["CODE"] == 404:
            return Http404(f"{CODES[404]}")