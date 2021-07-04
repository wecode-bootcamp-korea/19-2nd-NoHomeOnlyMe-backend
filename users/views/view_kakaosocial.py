import requests, bcrypt

from django.http.response import HttpResponseBadRequest
from django.views         import View

from users.utils  import publish_all_token
from users.models import User

class KakaoSocialView(View):
    
    def post(self, request):
        try:  
            
            authorization  = request.headers.get("Authorization")
            
            url      = "https://kapi.kakao.com/v2/user/me"
            header   = {"Authorization" : f"Bearer {authorization}"}
            response = requests.get(url, headers = header).json()
            
            if response.get("code") == -401:
                return HttpResponseBadRequest(f"{response['msg']}")
            
            user, created = User.objects.get_or_create(
                kakao_code = response["id"],
                name       = response["properties"]["nickname"],
                email      = response["kakao_account"]["email"]
                )
            
            if created:
                res = publish_all_token(user.id)
                res.status = 201
                return res
            
            return publish_all_token(user.id)
            
        except KeyError:
            return HttpResponseBadRequest("KEY_ERROR")