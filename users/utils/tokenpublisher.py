import jwt

from datetime   import (datetime, timedelta)
from mysettings import SECRET_KEY, ALGORITHM

from django.http.response import HttpResponse

def publish_all_token(user_id : int)-> dict:
    
    published_time = datetime.now()
    
    res = publish_access_token(user_id, published_time)
    res.set_cookie(
        key      = "refresh_token",
        value    = jwt.encode({"user_id" : user_id}, SECRET_KEY, algorithm = ALGORITHM),
        expires  = published_time + timedelta(days = 14),
        httponly = True,
    )
    
    return res
    
def publish_access_token(user_id : int, published_time : datetime = None) -> dict:
    
    if published_time is None:
        published_time = datetime.now()
    
    res = HttpResponse("Sign In Success", status = 200)
    res.set_cookie(
        key      = "access_token",
        value    = jwt.encode({"user_id" : user_id}, SECRET_KEY, algorithm = ALGORITHM),
        expires  = published_time + timedelta(hours = 6),
        httponly = True
        )
    
    return res