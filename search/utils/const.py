from decimal import Decimal

# 초기 지도 정보 디폴트 값
DEFAULT_MAP_POINT = {
    "center" : {
        "latitude"  : Decimal("37.5554418"),
        "longitude" : Decimal("126.9361192")
        },
    "zoom" : 13
    }

EARTH_MEAN_RADIUS = 6371000

# zoom 값에 따라 필요한 정보
ZOOM_DICT = {
    12 : {"scale" : 5000, "box_size" : '구', "view_size" : 80000},
    13 : {"scale" : 3000, "box_size" : '구', "view_size" : 48000},
    14 : {"scale" : 1000, "box_size" : '동', "view_size" : 16000},
    15 : {"scale" : 500,  "box_size" : '동', "view_size" : 8000},
    16 : {"scale" : 300,  "box_size" : 450, "view_size" : 4800},
    17 : {"scale" : 100,  "box_size" : 250, "view_size" : 1600}, 
    18 : {"scale" : 50,   "box_size" : 120, "view_size" : 800},
    19 : {"scale" : 30,   "box_size" : 60,  "view_size" : 480}
    }

INITIATE_ZOOM = {
    "amenity"   : 16,
    "dong"      : 14,
    "gu"        : 12,
    }

CODES = {
        "OK"                 : 200,
        "INVALID KEYWORD"    : 400,
        "RESOURCE NOT FOUND" : 404,
    }