# 보증금, 전세금, 매매금이 1억 이상일 경우 억 표시
def add_hundred_million(deposit):
    deposit = int(deposit)
    if deposit > 9999:
            deposit = str(deposit)[:-4] + "억" + str(deposit)[-4:]
    return deposit

# 월세가 null이 아닐 경우 int로 변환
def check_monthly_pay(monthly_pay):
    if monthly_pay:
        monthly_pay = int(monthly_pay)
    return monthly_pay