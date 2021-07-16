import json

from django.http.response import HttpResponse
from django.views         import View
from django.shortcuts     import get_object_or_404

from users.utils  import sign_in_required
from users.models import Like
from rooms.models import Room

class LikeView(View):
    
    @sign_in_required
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        room = get_object_or_404(Room, id = data["room_id"])
        try:
            if user.like.filter(room_id = room.id).exists():
                
                user.like.get(room_id = room.id).delete()
                return HttpResponse("Like cleared", status = 204)
            
            else:
                
                user.room.add(room)
                return HttpResponse("Like added", status = 201)
        
        except Like.MultipleObjectsReturned:
            user.like.filter(room_id = room.id).delete()
            return HttpResponse("Like cleared", status = 204)