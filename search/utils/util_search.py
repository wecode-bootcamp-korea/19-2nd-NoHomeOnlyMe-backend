import re
from decimal import Decimal

from .             import (CODES, INITIATE_ZOOM)
from rooms.models  import (Gu, Dong)
from search.models import Amenity

def search_keyword(keyword : str) -> dict:
    
    COMPILE_GU     = re.compile("^[가-힣]+구$")
    COMPILE_DONG   = re.compile("^[가-힣]+동$")
    COMPILE_SUBWAY = re.compile("^[가-힣]+역$")
    COMPILE_UNIV1  = re.compile("^[가-힣]+[대학교]$")
    COMPILE_UNIV2  = re.compile("^[가-힣]+[대학]$")
    COMPILE_UNIV3  = re.compile("^[가-힣]+[대]$")
    
    if re.match(COMPILE_GU, keyword):
        try:
            gu = Gu.objects.get(name = keyword)
            
            return {
                "code"   : CODES["OK"],
                "center" : {
                    "latitude"  : Decimal(gu.latitude),
                    "longitude" : Decimal(gu.longitude),
                    },
                "zoom"   : INITIATE_ZOOM["gu"],
                }
        
        except Gu.DoesNotExist:
            keyword = keyword.replace("구", "")
            amenity = Amenity.objects.filter(name__contains = keyword).order_by("name").first()
            
            if not amenity:
                return {
                    "code" : CODES["RESOURCE NOT FOUND"],
                    }
    
    if re.match(COMPILE_DONG, keyword):
        try:
            dong = Dong.objects.get(name = keyword)
            
            return {
                "code"      : CODES["OK"],
                "center" : {
                    "latitude"  : Decimal(dong.latitude),
                    "longitude" : Decimal(dong.longitude),
                    },
                "zoom"      : INITIATE_ZOOM["dong"],
                }
        
        except Dong.DoesNotExist:
            return {
                "code" : CODES["INVALID KEYWORD"],
            }
    
    if re.match(COMPILE_SUBWAY, keyword):
        try:
            amenity = Amenity.objects.get(name = keyword)
            
            return {
                "code"      : CODES["OK"],
                "center" : {
                    "latitude"  : Decimal(amenity.latitude),
                    "longitude" : Decimal(amenity.longitude),
                    },
                "zoom"      : INITIATE_ZOOM["amenity"],
                }
        
        except Amenity.DoesNotExist:
            
            return {
                "code" : CODES["INVALID KEYWORD"],
            }
    
    if re.match(COMPILE_UNIV1, keyword) or re.match(COMPILE_UNIV2, keyword) or re.match(COMPILE_UNIV3, keyword) :
        keyword = keyword.rsplit("대")[0]
        
        amenity = Amenity.objects.filter(name__contains = keyword, amenity_type__name = '대학교')
        
        if not amenity:
            return {
                "code" : CODES["RESOURCE NOT FOUND"],
                }
    
        return {
            "code"      : CODES["OK"],
            "center" : {
                    "latitude"  : Decimal(amenity.latitude),
                    "longitude" : Decimal(amenity.longitude),
                    },
            "zoom"      : INITIATE_ZOOM["amenity"],
            }
    
    return {
        "code" : CODES["RESOURCE NOT FOUND"],
        }