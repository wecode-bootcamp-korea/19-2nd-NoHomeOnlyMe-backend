import jwt

from django.http.response import (Http404, HttpResponseBadRequest)
from django.shortcuts import get_object_or_404

from users.models import User
from mysettings   import (SECRET_KEY, ALGORITHM)

def sign_in_required(func):
    def wrap(self, request):
        try:
            if not (access_token := request.COOKIES.get("access_token")):
                return HttpResponseBadRequest("Invalid Token")
            
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms = ALGORITHM)
            user         = get_object_or_404(User, id = payload["user_id"])
            request.user = user
            
            return func(self, request)
        
        except jwt.DecodeError:
            return HttpResponseBadRequest("Invalid Token")
        
    return wrap