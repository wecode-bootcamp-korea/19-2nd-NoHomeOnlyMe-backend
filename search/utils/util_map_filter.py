from decimal import Decimal

from django.db.models import Q

def filter_keyword(q : Q, **filter_keyword : dict) -> Q:
    
    if room_type := filter_keyword["room_type"]:
        room_types = room_type.split(',')
        
        q |= Q(room_type__name__in = room_types)
    
    if sale_type := filter_keyword["sale_type"]:
        sale_types = sale_type.split(',')
        
        q |= Q(saleinformation__sale_type__name__in = sale_types)
    
    if deposit := filter_keyword["deposit"] and filter_keyword["deposit"].find(',') != -1:
        deposit_list = deposit.split(',')
        MIN_DEPOSIT  = Decimal(min(deposit_list))
        MAX_DEPOSIT  = Decimal(max(deposit_list))
        
        q |= Q(saleinformation__deposit__range = (MIN_DEPOSIT, MAX_DEPOSIT))
        
    if monthly_pay := filter_keyword["monthly_pay"] and filter_keyword["monthly_pay"].find(',') != -1:
        monthly_pay_list = monthly_pay.split(',')
        MIN_MONTHLY_PAY  = Decimal(min(monthly_pay_list))
        MAX_MONTHLY_PAY  = Decimal(max(monthly_pay_list))
        
        q |= Q(saleinformation__monthly_pay__range = (MIN_MONTHLY_PAY, MAX_MONTHLY_PAY))
    
    if maintenance_cost := filter_keyword["maintenance_cost"] and filter_keyword["maintenance_cost"].find(',') != -1:
        maintenance_cost_list = maintenance_cost.split(',')
        MIN_MAINTENANCE_COST  = Decimal(min(maintenance_cost_list))
        MAX_MAINTENANCE_COST  = Decimal(max(maintenance_cost_list))
        
        q |= Q(additionalinformation__maintenance_cost__range = (MIN_MAINTENANCE_COST, MAX_MAINTENANCE_COST))
    
    if exclusive_m2 := filter_keyword["exclusive_m2"] and filter_keyword["exclusive_m2"].find(',') != -1:
        exclusive_m2_list = exclusive_m2.split(',')
        MIN_EXCLUSIVE_M2  = Decimal(min(exclusive_m2_list))
        MAX_EXCLUSIVE_M2  = Decimal(max(exclusive_m2_list))
        
        q |= Q(roominformation__exclusive_m2__range = (MIN_EXCLUSIVE_M2, MAX_EXCLUSIVE_M2))
        
    return q