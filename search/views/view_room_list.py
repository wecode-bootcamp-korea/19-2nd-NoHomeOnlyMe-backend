from django.http.response import JsonResponse
from django.views         import View

from search.utils import get_room_list

class RoomListView(View):
    def get(self, request):
        try:
            if not request.GET.get('room_id'):
                room_id = 0
                
                return JsonResponse(get_room_list(room_id), status = 200)
            
            room_id = request.GET.get('room_id').split(',')
            return JsonResponse(get_room_list(room_id), status = 200)
        
        except KeyError:
            return JsonResponse({"message" :  "Keyerror"}, status = 400)
        
        except Exception as e:
            return JsonResponse({"message" :  e}, status = 400)