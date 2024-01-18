select distinct H.car_id, C.car_type, round(C.daily_fee * 30 * (100 - P.discount_rate)/100) as FEE

from CAR_RENTAL_COMPANY_RENTAL_HISTORY H
inner join CAR_RENTAL_COMPANY_CAR C
    on H.car_id = C.car_id
inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    on C.car_type = P.car_type
    
where P.duration_type = '30일 이상'
    and C.car_type in ('SUV', '세단')
    and C.car_id not in (select car_id
                       from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                       where date_format(start_date, '%Y-%m') = '2022-11'
                         or date_format(end_date, '%Y-%m') = '2022-11'
                         or (date_format(start_date, '%Y-%m') <= '2022-11' 
                            and date_format(end_date, '%Y-%m') >= '2022-11'))
    
    and round(C.daily_fee * 30 * (100 - P.discount_rate)/100) >= 500000
    and round(C.daily_fee * 30 * (100 - P.discount_rate)/100) < 2000000
    
    
    # and (start_date >= '2022-12-01' or end_date < '2022-11-01')
    
order by FEE desc, C.car_type, H.car_id desc