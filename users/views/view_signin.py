import jwt, json, bcrypt

from django.http.response import (HttpResponseForbidden, HttpResponseNotFound, HttpResponse, HttpResponseBadRequest)
from django.views         import View

from users.utils  import (publish_all_token, publish_access_token)
from users.models import User
from mysettings   import (SECRET_KEY, ALGORITHM)

class SignInView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            cookies = request.COOKIES
            
            if cookies.get("access_token"):
                return HttpResponse("Sign In Success access token exists", status = 200)
            
            if refresh_token := cookies.get("refresh_token"):
                user_id = jwt.decode(refresh_token, SECRET_KEY, algorithms = ALGORITHM)["user_id"]
                
                return publish_access_token(user_id)
            
            user = User.objects.get(email = data["email"])
            
            if not bcrypt.checkpw(data["password"].encode("utf-8"), user.password.encode("utf-8")):
                return HttpResponseForbidden("Worng password")
            
            user.is_active = True
            
            return publish_all_token(user.id)
        
        except KeyError as e:
            return HttpResponseBadRequest(f"{e} KeyError")
        
        except User.DoesNotExist:
            return HttpResponseNotFound("User Not Found")