select H.history_id,
    case when datediff(H.end_date, H.start_date) + 1 < 7 then round(daily_fee * (datediff(H.end_date, H.start_date) + 1))
    when datediff(H.end_date, H.start_date) + 1 < 30 then round(daily_fee * (datediff(H.end_date, H.start_date) + 1) * (100 - (select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where duration_type = '7일 이상' and car_type = '트럭')) / 100)
    when datediff(H.end_date, H.start_date) + 1 < 90 then round(daily_fee * (datediff(H.end_date, H.start_date) + 1) * (100 - (select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where duration_type = '30일 이상' and car_type = '트럭')) / 100)
    else round(daily_fee * (datediff(H.end_date, H.start_date) + 1) * (100 - (select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where duration_type = '90일 이상' and car_type = '트럭')) / 100)
    end as FEE

from CAR_RENTAL_COMPANY_RENTAL_HISTORY H
inner join CAR_RENTAL_COMPANY_CAR C
    on H.car_id = C.car_id

where car_type = '트럭'

order by 2 desc, 1 desc