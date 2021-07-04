import requests
import json
import csv
import os
import sys
import django
from random import *
import re
from decimal import Decimal

os.chdir(".")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nohomeonlyme.settings")
django.setup()

from rooms.models  import *
from users.models  import *
from search.models import *

def rev_geocode(coords):
    key = {
        "X-NCP-APIGW-API-KEY-ID" : "6q6clfil2e",
        "X-NCP-APIGW-API-KEY"    : "L5cw6GqrDPSiD1AkyXzYFazYoeMeEmVS56vzPuMx"
        }

    lat  = coords['lat']
    long = coords['long']

    req_url   = f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords={long},{lat}&sourcecrs=EPSG:4326&orders=roadaddr,legalcode,addr&output=json"

    response = requests.get(req_url, headers = key)

    res = json.loads(response.content)
    
    return res

def geocode(address):
    key = {
        "X-NCP-APIGW-API-KEY-ID" : "6q6clfil2e",
        "X-NCP-APIGW-API-KEY"    : "L5cw6GqrDPSiD1AkyXzYFazYoeMeEmVS56vzPuMx"
        }
    
    response = requests.get(
        f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}",
        headers = key
        )
    
    res = json.loads(response.content)
    
    try:
        coords = {'longitude' : res['addresses'][0]['x'], 'latitude' : res['addresses'][0]['y']}
        return coords
    
    except IndexError:
        coords = {'longitude' : "127.0000000", 'latitude' : "37.0000000"}
        return coords

# room_types = ['원룸', '투룸/쓰리룸', '오피스텔', '아파트']
# for room_type in room_types:
#     RoomType.objects.create(
#         name = room_type
#     )
# building_type = ['단독주택', '다가구주택', '빌라/연립/다세대', '상가주택']
# for building_type in building_type:
#     BuildingType.objects.create(
#         name = building_type
#     )
# sale_types = ['월세', '전세', '매매']
# for sale_type in sale_types:
#     SaleType.objects.create(
#         name = sale_type
#     )
# amenity_types = ["어린이집", "유치원", "초등학교", "중학교", "고등학교", "대학교", "편의점", "지하철역", "경찰서", "카페", "관공서", "은행"]
# for amenity_type in amenity_types:
#     AmenityType.objects.create(
#         name = amenity_type
#     )

# gus = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']

# for gu in gus:
#     coords = geocode(gu)
#     Gu.objects.create(
#         name      = gu,
#         latitude  = '37.00000',
#         longitude = '127.00000'
#     )

txtfile = open("nohome/seoul_address.txt", 'r')
rows = txtfile.readlines()

room = [] # 집

bank    = [] # 은행
subway  = [] # 지하철
police  = [] # 경찰서
com_cen = [] # 관공서

kindergarden = [] # 유치원
day_care     = [] # 어린이집
ele_school   = []
mid_school   = []
high_school  = []
univ         = []
i = 1

for row in rows[1:]:
    i += 1
    row  = row.split("|")
    name = row[15]
    gu   = row[3]
    dong = row[17]
    
    # if not Dong.objects.filter(name = dong, gu__name = gu).exists():
    #     coords = geocode(gu + ' ' + dong)
    #     Dong.objects.create(
    #         name      = dong,
    #         gu        = Gu.objects.get(name = gu),
    #         latitude  = coords["latitude"],
    #         longitude = coords["longitude"]
    #         )
    if name:
        road_address  = row[1] + ' ' + row[3] + ' ' + row[8] + ' ' + row[11]
        if row[12] != '0':
            road_address  = row[1] + ' ' + row[3] + ' ' + row[8] + ' ' + row[11] + '-' + row[12]
        
        regal_address = row[1] + ' ' + row[3] + ' ' + row[17] + ' ' + row[21]
        if row[23] != '0':
            regal_address = row[1] + ' ' + row[3] + ' ' + row[17] + ' ' + row[21] + '-' + row[23]
        
        if re.search(re.compile('아파트'), name):
            room.append({
                "name"          : name,
                "road_address"  : road_address,
                "regal_address" : regal_address,
                "gu"            : gu,
                "dong"          : dong,
                "room_type"     : "아파트",
                "building_type" : "다가구주택",
                "latitude"      : "37.00000",
                "longitude"     : "127.00000"})
        if re.search(re.compile('빌'), name):
            if not re.search(re.compile('빌딩'), name):
                if re.search(re.compile('빌라'), name):
                    room.append({
                    "name"          : name,
                    "road_address"  : road_address,
                    "regal_address" : regal_address,
                    "gu"            : gu,
                    "dong"          : dong,
                    "room_type"     : "투룸/쓰리룸",
                    "building_type" : "빌라/연립/다세대",
                    "latitude"      : "37.00000",
                    "longitude"     : "127.00000"})
                else:
                    room_type = choice(["원룸", "투룸/쓰리룸"])
                    room.append({
                    "name"          : name,
                    "road_address"  : road_address,
                    "regal_address" : regal_address,
                    "gu"            : gu,
                    "dong"          : dong,
                    "room_type"     : room_type,
                    "building_type" : "빌라/연립/다세대",
                    "latitude"      : "37.00000",
                    "longitude"     : "127.00000"})
        if re.search(re.compile('오피스텔'), name):
            room.append({
                    "name"          : name,
                    "road_address"  : road_address,
                    "regal_address" : regal_address,
                    "gu"            : gu,
                    "dong"          : dong,
                    "room_type"     : "오피스텔",
                    "building_type" : "상가주택",
                    "latitude"      : "37.00000",
                    "longitude"     : "127.00000"})
        if re.search(re.compile('유치원'), name):
            day_care.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "유치원",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })

        if re.search(re.compile('어린이집'), name):
            kindergarden.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "어린이집",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('초등학교'), name):
            ele_school.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "초등학교",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('중학교'), name):
            mid_school.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "중학교",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('고등학교'), name):
            high_school.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "고등학교",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('대학교'), name):
            univ.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "대학교",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('파출소'), name) or re.search(re.compile('경찰서'), name):
            police.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "경찰서",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('은행'), name):
            bank.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "은행",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('주민센터'), name):
            com_cen.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "관공서",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
        if re.search(re.compile('역'), name):
            subway.append({
                "name"         : name,
                "road_address" : road_address,
                "amenity_type" : "지하철역",
                "gu"           : gu,
                "dong"         : dong,
                "latitude"     : "37.00000",
                "longitude"    : "127.0000"
            })
amenity = [bank, police, com_cen, kindergarden, day_care, ele_school, mid_school, high_school, univ]

txtfile.close()

room_query = [] # 집
amenity_query = []

for room in room:
    coords = geocode(room["road_address"])
    room_query.append(Room(
                name          = room["name"],
                road_address  = room["road_address"],
                regal_address = room["regal_address"],
                gu            = Gu.objects.get(name = room["gu"]),
                dong          = Dong.objects.get(name = room["dong"], gu__name = room["gu"]),
                room_type     = RoomType.objects.get(name = room["room_type"]),
                building_type = BuildingType.objects.get(name = room["building_type"]),
                latitude      = coords["latitude"],
                longitude     = coords["longitude"]
            ))

for amenity in amenity:
    coords = geocode(amenity["road_address"])
    amenity_query.append(
        Amenity(
            name         = amenity["name"],
            road_address = amenity["road_address"],
            amenity_type = AmenityType.objects.get(name = amenity["amenity_type"]),
            gu           = Gu.objects.get(name = amenity["gu"]),
            dong         = Dong.objects.get(name = amenity["dong"], gu__name = amenity["gu"]),
            latitude     = coords["latitude"],
            longitude    = coords["longitude"]
            )
        )

Room.objects.bulk_create(room_query)
Amenity.objects.bulk_create(amenity_query)