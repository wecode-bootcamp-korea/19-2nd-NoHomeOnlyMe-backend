import json
import datetime

from django.test import TestCase
from django.test import Client

from users.models  import User
from homes.models  import *
from search.models import Amenity, AmenityType

class RoomDetailTest(TestCase):

    def setUp(self):
        User.objects.create(
            id           = 1,
            name         = "이없방",
            email        = "lee@nohome.com",
            password     = "1111",
            phone_number = "01011112222",
        )
        RoomType.objects.create(
            id   = 1,
            name = "원룸",
        )
        HouseType.objects.create(
            id   = 1,
            name = "단독주택",
        )
        GuType.objects.create(
            id        = 1,
            name      = "강남구",
            latitude  = "37.4959854",
            longitude = "127.0664091",
        )
        DongType.objects.create(
            id        = 1,
            name      = "개포동",
            latitude  = "37.4827409",
            longitude = "127.055737",
            gu_type   = GuType.objects.get(id=1),
        )
        Home.objects.create(
            id           = 1,
            name         = "골든강남빌",
            road_address = "서울특별시 강남구 테헤란로 427",
            dong         = "510",
            ho           = "705",
            latitude     = "37.4804644",
            longitude    = "127.048616",
            created_at   = datetime.datetime.now(),
            house_type   = HouseType.objects.get(id=1),
            legalcode    = DongType.objects.get(id=1),
            room_type    = RoomType.objects.get(id=1),
            user         = User.objects.get(id=1),
        )
        Home.objects.create(
            id           = 2,
            name         = "세종빌딩",
            road_address = "서울특별시 종로구 세종대로23길 54",
            latitude     = "37.5718397",
            longitude    = "126.9733018",
            created_at   = datetime.datetime.now(),
            house_type   = HouseType.objects.get(id=1),
            legalcode    = DongType.objects.get(id=1),
            user         = User.objects.get(id=1),
        )
        SaleType.objects.create(
            id   = 1,
            name = "월세",
        )
        SaleInformation.objects.create(
            id          = 1,
            deposit     = "12000.00",
            monthly_pay = "30.00",
            is_short    = 0,
            home        = Home.objects.get(id=1),
            sale_type   = SaleType.objects.get(id=1),
        )
        MoveInOption.objects.create(
            id   = 1,
            name = "즉시 입주"
        )
        RoomInformation.objects.create(
            id               = 1,
            supply_pyeong    = 10,
            supply_m2        = "33.0003",
            exclusive_pyeong = 9,
            exclusive_m2     = "29.7777",
            building_story   = 19,
            floor            = 10,
            heating_type     = "개별난방",
            move_in_option   = MoveInOption.objects.get(id=1),
            move_in_date     = datetime.datetime.now(),
            home             = Home.objects.get(id=1)
        )
        AdditionalInformation.objects.create(
            id               = 1,
            maintenance_cost = "10.00",
            is_agreement     = 0,
            parking_fee      = "3.00",
            home             = Home.objects.get(id=1),
        )
        AdditionalOption.objects.create(
            id   = 1,
            name = "주차여부",
        )
        AdditionalOption.objects.create(
            id   = 2,
            name = "반려동물",
        ),
        AdditionalOption.objects.create(
            id   = 3,
            name = "엘리베이터",
        )
        CheckAdditionalOption.objects.create(
            id                     = 1,
            is_able                = 1,
            additional_information = AdditionalInformation.objects.get(id=1),
            additional_option      = AdditionalOption.objects.get(id=1),
        )
        CheckAdditionalOption.objects.create(
            id                     = 2,
            is_able                = 0,
            additional_information = AdditionalInformation.objects.get(id=1),
            additional_option      = AdditionalOption.objects.get(id=2),
        )
        CheckAdditionalOption.objects.create(
            id                     = 3,
            is_able                = 1,
            additional_information = AdditionalInformation.objects.get(id=1),
            additional_option      = AdditionalOption.objects.get(id=3),
        )
        Image.objects.create(
            id        = 1,
            image_url = "http://1",
            sequence  = 1,
            home      = Home.objects.get(id=1),
        )
        Image.objects.create(
            id        = 2,
            image_url = "http://2",
            sequence  = 2,
            home      = Home.objects.get(id=1),
        )
        AmenityType.objects.create(
            id   = 1,
            name = '편의점'
        )
        AmenityType.objects.create(
            id   = 2,
            name = '지하철역'
        )
        AmenityType.objects.create(
            id   = 3,
            name = '대학교'
        )
        Amenity.objects.create(
            id           = 1,
            name         = 'GS25',
            road_address = '대한민국 어딘가',
            legalcode    = DongType.objects.get(id=1),
            latitude     = "37.4753923",
            longitude    = "127.048661",
            type         = AmenityType.objects.get(id=1)
        )
        Amenity.objects.create(
            id           = 2,
            name         = '선릉역',
            road_address = '선정릉 옆',
            legalcode    = DongType.objects.get(id=1),
            latitude     = "37.4750195",
            longitude    = "127.0527091",
            type         = AmenityType.objects.get(id=2)
        )
        Amenity.objects.create(
            id           = 3,
            name         = '연세대학교',
            road_address = '대한민국 어딘가',
            legalcode    = DongType.objects.get(id=1),
            latitude     = "37.4741753",
            longitude    = "127.0532359",
            type         = AmenityType.objects.get(id=3)
        )

    def tearDown(self):
        User.objects.all().delete()
        RoomType.objects.all().delete()
        HouseType.objects.all().delete()
        GuType.objects.all().delete()
        DongType.objects.all().delete()
        Home.objects.all().delete()
        SaleType.objects.all().delete()
        SaleInformation.objects.all().delete()
        MoveInOption.objects.all().delete()
        RoomInformation.objects.all().delete()
        AdditionalInformation.objects.all().delete()
        AdditionalOption.objects.all().delete()
        CheckAdditionalOption.objects.all().delete()
        Image.objects.all().delete()
        AmenityType.objects.all().delete()
        Amenity.objects.all().delete()

    def test_room_detail_get_not_found(self):
        client = Client()
        response = client.get('/room/3394842')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), (
            {
                'MESSAGE': 'NOT_FOUND'
            }
        ))

    def test_room_detail_get_success(self):
        client = Client() 
        response = client.get("/room/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'RESULT': {
                    'home_id': 1,
                    'detail_header': {
                        'room_type': '원룸',
                        'name': '골든강남빌',
                        'sale_type': '월세', 
                        'deposit': '1억2000', 
                        'monthly_pay': 30, 
                        'exclusive_m2': 29.7777, 
                        'exclusive_pyeong': 9, 
                        'month_total_cost': 43, 
                        'user_name': '이없방'
                    },
                    'detail_info': {
                        'floor': 10, 
                        'building_story': 19, 
                        'exclusive_m2': 29.7777, 
                        'supply_m2': 33.0003, 
                        'exclusive_pyeong': 9, 
                        'supply_pyeong': 10, 
                        'heating_type': '개별난방', 
                        'parking': True, 
                        'pet': False, 
                        'elevator': True, 
                        'move_in_date': '즉시 입주', 
                        'house_type': '단독주택'
                    },
                    'detail_images': [{
                        'url': 'http://1'
                        }, {
                        'url': 'http://2'
                        }],
                    'maps': {
                        'road_address': '서울특별시 강남구 테헤란로 427',
                        'center': {
                            'latitude': 37.4804644,
                            'longitude': 127.048616
                        },
                        'convenience_store': [
                            {
                                'latitude': 37.4753923, 
                                'longitude': 127.048661
                            }
                        ],
                        'subway': [
                            {
                                'latitude': 37.4750195, 
                                'longitude': 127.0527091
                            }
                        ],
                        'university': [
                            {
                                'latitude': 37.4741753,
                                'longitude': 127.0532359
                            }
                        ]},
                        'other_rooms': []
                    }
                }
        )

