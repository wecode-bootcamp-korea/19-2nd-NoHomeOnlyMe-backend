from typing import Sequence
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

from homes.models import *
from users.models import *
from search.models import *

def rev_geocode(coords):
       key = {"X-NCP-APIGW-API-KEY-ID" : "6q6clfil2e",
              "X-NCP-APIGW-API-KEY"    : "L5cw6GqrDPSiD1AkyXzYFazYoeMeEmVS56vzPuMx"}

       lat = coords['y']
       long = coords['x']

       req_url   = f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords={long},{lat}&sourcecrs=EPSG:4326&orders=roadaddr,legalcode,addr&output=json"

       response = requests.get(req_url, headers = key)

       res = json.loads(response.content)
       
       return res

def geocode(address):
       key = {"X-NCP-APIGW-API-KEY-ID" : "6q6clfil2e",
              "X-NCP-APIGW-API-KEY"    : "L5cw6GqrDPSiD1AkyXzYFazYoeMeEmVS56vzPuMx"}
       
       response = requests.get(f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}", headers = key)
       
       res = json.loads(response.content)
       try:
              coords = {'longitude' : res['addresses'][0]['x'], 'latitude' : res['addresses'][0]['y']}
              return coords
       except IndexError:
              coords = {'longitude' : "127.0000000", 'latitude' : "37.0000000"}
              return coords
       

# with open("db_backups/home_addresses.csv", newline = '') as csv_open:
#        data_reader = csv.reader(csv_open)
       
#        with open("db_backups/seoul_gu_addresses.csv", newline = '') as gu:
#               gu_list = csv.reader(gu)
              
              # # 구 입력
              # for gu in gu_list:
              #        GuType.objects.create(
              #               name = gu[2],
              #               latitude = gu[4],
              #               longitude = gu[3]
              #              )
              
              # 동 입력
              # for row in data_reader:
              #        gu_name = row[0].split(' ')[1]
              #        dong_name = row[1]
              #        if not DongType.objects.filter(name = dong_name).exists():
              #               coords = geocode(dong_name)
              #               DongType.objects.create(
              #                      name = dong_name,
              #                      latitude = coords["latitude"],
              #                      longitude = coords["longitude"],
              #                      gu_type_id = GuType.objects.get(name=gu_name).id
              #                      )
              
              
              # for home in data_reader:
                     
              #        Home.objects.create(
              #               name = home[2],
              #               road_address = home[0],
              #               latitude = home[4],
              #               longitude = home[3],
              #               legalcode_id = DongType.objects.get(name=home[1]).id
                            
              #        )
# a = Amenity.objects.filter(type_id = 1)
# a.delete()
# a = geocode("서울 구로구 천왕동")
# print(a)

# DongType.objects.create(
#        name = '천왕동',
#        latitude = a['latitude'],
#        longitude = a['longitude'],
#        gu_type_id = GuType.objects.get(name = '구로구').id
# )
# with open("db_backups/subway_addresses.csv") as convenience_open:
#        data_reader = csv.reader(convenience_open)
#        for row in data_reader:
                       
#               Amenity.objects.create(
#                      name = row[2],
#                      road_address = row[0],
#                      latitude = row[4],
#                      longitude = row[3],
#                      legalcode_id = DongType.objects.get(name = row[1]).id,
#                      type_id = AmenityType.objects.get(name='지하철역').id
#               )
              
              
# # coords = geocode('율현동')
# # DongType.objects.create(
# #        name = '율현동',
# #        latitude = coords['latitude'],
# #        longitude = coords['longitude'],
# #        gu_type_id = GuType.objects.get(name = '강남구').id
# # )

# for home in Home.objects.all():
#        id = randrange(1,6)
#        home.room_type_id = id
#        home.save()
       
# images = ["https://www.google.com/search?q=free+image+about+beautiful+house&rlz=1C5CHFA_enKR923KR923&sxsrf=ALeKk03auz2LhWZ9HsBIpYR_KxaoisCkKQ:1620346318430&tbm=isch&source=iu&ictx=1&fir=dAB3t4pBTWvFnM%252CXK8DUNClm8MVmM%252C_&vet=1&usg=AI4_-kQrGrb4xoWKd4Kj8n5PMmHQcSbc8w&sa=X&ved=2ahUKEwi8iOS1pLbwAhVGa94KHXVrAjwQ9QF6BAgPEAE#imgrc=dAB3t4pBTWvFnM",
#  "https://images.unsplash.com/photo-1565297032488-90722f09db62?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdXRpZnVsJTIwaG91c2V8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
#  "https://images.unsplash.com/photo-1512915922686-57c11dde9b6b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8YmVhdXRpZnVsJTIwaG91c2V8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
#  "https://images.unsplash.com/photo-1522050212171-61b01dd24579?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8YmVhdXRpZnVsJTIwaG91c2V8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
#  "https://images.unsplash.com/photo-1566908829550-e6551b00979b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1649&q=80",
#  "https://images.unsplash.com/photo-1531971589569-0d9370cbe1e5?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fGJlYXV0aWZ1bCUyMGhvdXNlfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
#  "https://images.unsplash.com/photo-1568092775154-7fa176a29c0f?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjN8fGJlYXV0aWZ1bCUyMGhvdXNlfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
#  "https://images.unsplash.com/photo-1515541369882-f47fa81d1454?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzF8fGJlYXV0aWZ1bCUyMGhvdXNlfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"]
# i = 1
# for image in images:
#     Image.objects.create(
#         image_url = image,
#         sequence = 1,
#         home_id = i
#     )
#     i += 1