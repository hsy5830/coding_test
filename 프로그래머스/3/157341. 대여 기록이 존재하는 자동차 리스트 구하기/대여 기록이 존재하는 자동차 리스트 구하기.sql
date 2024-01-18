select car_id

from CAR_RENTAL_COMPANY_CAR

where car_id in (select distinct car_id
                from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                where month(start_date) = 10)
    and car_type = '세단'
    
order by 1 desc