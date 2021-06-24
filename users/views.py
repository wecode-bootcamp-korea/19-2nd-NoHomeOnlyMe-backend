import jwt
import requests
import json

from django.views import View
from django.http  import JsonResponse

from mysettings import SECRET_KEY, ALGORITHM
from .models    import User

class KakaoSignInView(View):
    def post(self, request):
        try:  
            data = json.loads(request.body)
            
            access_token  = data['access_token']
            url           = 'https://kapi.kakao.com/v2/user/me'
            header        = {'Authorization' : f'Bearer {access_token}'}
            response      = requests.post(url, headers=header).json()
            user, created = User.objects.get_or_create(
                                user_code    = response['id'],
                                name         = response['properties']['nickname'],
                                )
            access_token  = jwt.encode({'user_code' : user.user_code}, SECRET_KEY['secret_key'], ALGORITHM)
            return JsonResponse(
                    {
                        'message'      : 'SUCCESS', 
                        'access_token' : access_token,
                        'is_new'       : created
                    }, status=200
                )
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        except Exception as e:
            return JsonResponse({'message' : e}, status=400)