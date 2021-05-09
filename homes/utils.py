# 보증금, 전세금, 매매금이 1억 이상일 경우 억 표시
def add_hundred_million(deposit):
    amount = str(int(deposit))
    
    if int(amount) > 99999999:
        return int(amount[0:-8])
    elif int(amount) > 9999:
        return int(amount[-8:-4])
    else: 
        return int(amount[-4:])
# 월세가 null이 아닐 경우 int로 변환
def check_monthly_pay(monthly_pay):
    amount = str(int(monthly_pay))
    
    if int(amount) > 99999999:
        return int(amount[0:-8])
    elif int(amount) > 9999:
        return int(amount[-8:-4])
    else: 
        return int(amount[-4:])