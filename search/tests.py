import datetime

from decimal import Decimal
from django.db import reset_queries
from django.http import response

from django.test import TestCase, Client

from homes.models  import *
from search.models import Amenity, AmenityType
from users.models  import User

class MapApiTest (TestCase):
    def setUp(self):
        User.objects.create(
            name         = "john",
            email        = "johnywhisky@wecode.com",
            password     = "1234qwer",
            phone_number = "01012345678",
        )
        RoomType.objects.create(
            name = "어떤방",
        )
        HouseType.objects.create(
            name = "어떤집",
        )
        GuType.objects.create(
            name      = "어떤구",
            latitude  = Decimal("37.50622013"),
            longitude = Decimal("127.0534443"),
        )
        DongType.objects.create(
            name      = "어떤동",
            latitude  = "37.50622013",
            longitude = "127.0534443",
            gu_type   = GuType.objects.get(name = '어떤구')
        )
        Home.objects.create(
            id           = 1,
            name         = "곧 무너질 것같은 아파트",
            road_address = "서울특별시 강남구 테헤란로 427",
            dong         = "123",
            ho           = "456",
            latitude     = Decimal("37.50622013"),
            longitude    = Decimal("127.0534443"),
            created_at   = datetime.datetime.now(),
            house_type   = HouseType.objects.get(name = '어떤집'),
            legalcode    = DongType.objects.get(name = "어떤동"),
            room_type    = RoomType.objects.get(name = "어떤방"),
            user         = User.objects.get(email = "johnywhisky@wecode.com"),
        )
        AmenityType.objects.create(
            name = '대학교'
        )
        Amenity.objects.create(
            name         = '어떤 대학교',
            road_address = '대한민국 어딘가',
            legalcode    = DongType.objects.get(name = "어떤동"),
            latitude     = Decimal("37.50622013"),
            longitude    = Decimal("127.0534443"),
            type         = AmenityType.objects.get(name = "대학교")
        )
        AmenityType.objects.create(
            name = '어떤지하철역'
        )
        Amenity.objects.create(
            name         = "어떤 지하철",
            road_address = '대한민국 어딘가',
            legalcode    = DongType.objects.get(name="어떤동"),
            latitude     = Decimal("37.50622013"),
            longitude    = Decimal("127.0534443"),
            type         = AmenityType.objects.get(name='어떤지하철역')
        )
        MoveInOption.objects.create(
            name = '어떤옵션'
        )
        RoomInformation.objects.create(
            supply_pyeong    = 10,
            supply_m2        = Decimal('33.0003'),
            exclusive_pyeong = 9,
            exclusive_m2     = Decimal('29.7777'),
            building_story   = 19,
            floor            = 10,
            heating_type     = '개별난방',
            move_in_option   = MoveInOption.objects.get(name='어떤옵션'),
            move_in_date     = datetime.datetime.now(),
            home             = Home.objects.get(name = '곧 무너질 것같은 아파트')
        )
        SaleType.objects.create(
                name = "어떤월세",
            )
        SaleInformation.objects.create(
            deposit     = Decimal("12000.00"),
            monthly_pay = Decimal("30.00"),
            is_short    = 0,
            home        = Home.objects.get(name='곧 무너질 것같은 아파트'),
            sale_type   = SaleType.objects.get(name='어떤월세'),
        )
        AdditionalInformation.objects.create(
                    maintenance_cost = Decimal("12.34"),
                    is_agreement     = 0,
                    parking_fee      = Decimal("3.00"),
                    home             = Home.objects.get(name='곧 무너질 것같은 아파트'),
                )
        AdditionalOption.objects.create(
            name = "어떤옵션1",
        )
        AdditionalOption.objects.create(
            name = "어떤옵션2",
        ),
        AdditionalOption.objects.create(
            name = "어떤옵션3",
        )
        CheckAdditionalOption.objects.create(
            is_able                = 1,
            additional_information = AdditionalInformation.objects.get(home__name = '곧 무너질 것같은 아파트'),
            additional_option      = AdditionalOption.objects.get(name = "어떤옵션1"),
        )
        CheckAdditionalOption.objects.create(
            is_able                = 0,
            additional_information = AdditionalInformation.objects.get(home__name = '곧 무너질 것같은 아파트'),
            additional_option      = AdditionalOption.objects.get(name = "어떤옵션2"),
        )
        CheckAdditionalOption.objects.create(
            id                     = 3,
            is_able                = 1,
            additional_information = AdditionalInformation.objects.get(home__name = '곧 무너질 것같은 아파트'),
            additional_option      = AdditionalOption.objects.get(name = "어떤옵션3"),
        )
        Image.objects.create(
            image_url = "http://1",
            sequence  = 1,
            home      = Home.objects.get(name = "곧 무너질 것같은 아파트"),
        )
        Image.objects.create(
            image_url = "http://2",
            sequence  = 2,
            home      = Home.objects.get(name = "곧 무너질 것같은 아파트"),
        )
        
    def tearDown(self):
        User.objects.all().delete()
        RoomType.objects.all().delete()
        HouseType.objects.all().delete()
        GuType.objects.all().delete()
        DongType.objects.all().delete()
        Home.objects.all().delete()
        Amenity.objects.all().delete()
        AmenityType.objects.all().delete()
        MoveInOption.objects.all().delete()
        RoomInformation.objects.all().delete()
        SaleType.objects.all().delete()
        SaleInformation.objects.all().delete()
        AdditionalInformation.objects.all().delete()
        AdditionalOption.objects.all().delete()
        AdditionalRoomOption.objects.all().delete()
        CheckAdditionalOption.objects.all().delete()
        Image.objects.all().delete()
        
    def test_get_defalut_map(self):
        response = Client().get('/search/map')
        
        print('test 1 : 첫 화면 로드')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "center" : {
                "latitude"  : 37.5554418,
                "longitude" : 126.9361192
                },
            "zoom" : 13,
            "room_list" : [{
                "name"      : "어떤구",
                "latitude"  : 37.50622013,
                "longitude" : 127.0534443,
                "room_id" : [1]
                }],
            "subway_list" : [],
            "univ_list" : []
            })
        
    def test_get_filter(self):
        response = Client().get('/search/map?deposit=100000000,150000000')
        
        print('\ntest 2 : filter 적용')
        self.assertEqual(response.json(), {
            "center" : {
                "latitude"  : 37.1234567,
                "longitude" : 127.1234567
                },
            "zoom" : 13,
            "room_list" : [{
                "name"      : "어떤구",
                "latitude"  : 37.50622013,
                "longitude" : 127.0534443,
                "room_id" : [1]
                }],
            "subway_list" : [],
            "univ_list" : []
            })
        
    def test_get_search(self):
        response = Client().get('/search/map?search=강남구')
        
        print('\ntest 3 : search 적용')
        self.assertEqual(response.json(),{
            "center" : {
                "latitude"  : 37.5554418,
                "longitude" : 126.9361192
                },
            "zoom" : 13,
            "room_list" : [{
                "name"      : "어떤구",
                "latitude"  : 37.50622013,
                "longitude" : 127.0534443,
                "room_id" : [1]
                }],
            "subway_list" : [],
            "univ_list" :  [{
                'latitude': 37.50622013,
                'longitude': 127.0534443,
                'name': '어떤 대학교'}]
        })
        
    def test_get_all(self):
        response = Client().get('/search/map?center=37.1234567,127.1234567&zoom=14&search=어대&exclusive_m2=0,500')
        
        print('\ntest 4 : 모두 적용')
        self.assertEqual(response.json(),{
            "center" : {
                "latitude"  : 37.50622013,
                "longitude" : 127.0534443
                },
            "zoom" : 16,
            "room_list" : [{
                "name"      : "어떤구",
                "latitude"  : 37.50622013,
                "longitude" : 127.0534443,
                "room_id" : [1]
                }],
            "subway_list" : [],
            "univ_list" : [{
                'name': '어떤 대학교',
                'latitude': 37.50622013,
                'longitude': 127.0534443,
                }]
        })