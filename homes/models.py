from django.db    import models

# 매물 종류 (원룸, 투룸, 오피스텔, 아파트...)
class RoomType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "room_types"

# 건물 유형 (단독 주택, 다가구 주택, 오피스텔...)
class HouseType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "house_types"

# 주소지 구
class GuType(models.Model):
    name      = models.CharField(max_length=10)
    latitude  = models.DecimalField(max_digits=15, decimal_places=10) # 위도
    longitude = models.DecimalField(max_digits=15, decimal_places=10) # 경도

    class Meta:
        db_table = "gu_types"

# 주소지 동
class DongType(models.Model):
    name      = models.CharField(max_length=10)
    latitude  = models.DecimalField(max_digits=15, decimal_places=10) # 위도
    longitude = models.DecimalField(max_digits=15, decimal_places=10) # 경도
    gu_type   = models.ForeignKey("GuType", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "dong_types"

# 집 정보
class Home(models.Model):
    name         = models.CharField(max_length=200, null = True)
    road_address = models.CharField(max_length=500) # 도로명 주소
    legalcode    = models.ForeignKey("DongType", on_delete=models.SET_NULL, null=True) # 주소지 동
    dong         = models.CharField(max_length=10, null=True) # 동
    ho           = models.CharField(max_length=10, null=True) # 호
    room_type    = models.ForeignKey("RoomType", on_delete=models.CASCADE, null = True)
    house_type   = models.ForeignKey("HouseType", on_delete=models.SET_NULL, null=True)
    latitud      = models.DecimalField(max_digits=15, decimal_places=10) # 위도
    longitude    = models.DecimalField(max_digits=15, decimal_places=10) # 경도
    user         = models.ForeignKey("users.User", on_delete=models.CASCADE, null = True)
    created_at   = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = "homes"

# 거래 종류 (월세, 전세, 매매)
class SaleType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "sale_types"

# 거래 정보
class SaleInformation(models.Model):
    deposit     = models.DecimalField(max_digits=18, decimal_places=2) # 보증금, 전세금, 매매금
    monthly_pay = models.DecimalField(max_digits=18, decimal_places=2, null=True) # 월세
    is_short    = models.BooleanField(default=False) # 단기 거주 가능
    sale_type   = models.ForeignKey("SaleType", on_delete=models.CASCADE)
    home        = models.ForeignKey("Home", on_delete=models.CASCADE)

    class Meta:
        db_table = "sale_informations"

# 입주 가능일 옵션 (즉시 입주, 날짜 협의, 날짜 선택)
class MoveInOption(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "move_in_options"

# 방 기본 정보
class RoomInformation(models.Model):
    supply_pyeong    = models.IntegerField() # 공급 면적 평
    supply_m2        = models.DecimalField(max_digits=15, decimal_places=5) # 공급 면적 m2
    exclusive_pyeong = models.IntegerField() # 전용 면적 평
    exclusive_m2     = models.DecimalField(max_digits=15, decimal_places=5) # 전용 면적 m2
    building_story   = models.IntegerField() # 건물 층수
    floor            = models.IntegerField() # 해당 층수
    heating_type     = models.CharField(max_length=50) # 난방 종류
    move_in_option   = models.ForeignKey("MoveInOption", on_delete=models.CASCADE)
    move_in_date     = models.DateField(null=True) # 입주 날짜
    home             = models.ForeignKey("Home", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "room_informations"

# 방 추가 정보
class AdditionalInformation(models.Model):
    maintenance_cost         = models.DecimalField(max_digits=18, decimal_places=2, default=0) # 관리비
    is_agreement             = models.BooleanField(default=False) # 관리비 협의 가능 여부
    parking_fee              = models.DecimalField(max_digits=18, decimal_places=2, default=0) # 주차비
    home                     = models.ForeignKey("Home", on_delete=models.CASCADE)
    maintenance_cost_options = models.ManyToManyField("MaintenanceCostOption", through="InclusionMaintenanceCost")
    additional_options       = models.ManyToManyField("AdditionalOption", through="CheckAdditionalOption")
    room_options             = models.ManyToManyField("RoomOption", through="AdditionalRoomOption")

    class Meta:
        db_table = "additional_informations"

# 관리비 옵션 (인터넷, 유선TV, 청소비, 수도세...)
class MaintenanceCostOption(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "maintenance_cost_options"

# 방 추가 정보 + 관리비 옵션 M:N
class InclusionMaintenanceCost(models.Model):
    additional_information  = models.ForeignKey("AdditionalInformation", on_delete=models.CASCADE)
    maintenance_cost_option = models.ForeignKey("MaintenanceCostOption", on_delete=models.CASCADE)

    class Meta:
        db_table = "inclusion_maintenance_cost"

# 추가 정보 옵션 (주차 여부, 엘리베이터, 빌트인...)
class AdditionalOption(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "additional_options"
    
# 방 추가 정보 + 추가 정보 옵션 M:N
class CheckAdditionalOption(models.Model):
    is_able                = models.BooleanField(default=False) # 옵션 가능 여부
    additional_information = models.ForeignKey("AdditionalInformation", on_delete=models.CASCADE)
    additional_option      = models.ForeignKey("AdditionalOption", on_delete=models.CASCADE)

    class Meta:
        db_table = "check_additional_options"

# 방 옵션 (인덕션, 전자레인지, 에어컨, 세탁기...)
class RoomOption(models.Model):
    name = models.CharField(max_length=50)
     
    class Meta:
        db_table = "room_options"

# 방 추가 정보 + 방 옵션 M:N
class AdditionalRoomOption(models.Model):
    room_option            = models.ForeignKey("RoomOption", on_delete=models.CASCADE)
    additional_information = models.ForeignKey("AdditionalInformation", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "additional_room_options"

# 상세 설명 옵션
class DescriptionOption(models.Model):
    title       = models.CharField(max_length=300) # 제목
    description = models.TextField() # 상세 설명
    secret_text = models.TextField() # 비공개 메모
    home        = models.ForeignKey("Home", on_delete=models.CASCADE)

    class Meta:
        db_table = "description_options"

# 사진
class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    sequence  = models.IntegerField()
    home      = models.ForeignKey("Home", on_delete=models.CASCADE)

    class Meta:
        db_table = "images"
