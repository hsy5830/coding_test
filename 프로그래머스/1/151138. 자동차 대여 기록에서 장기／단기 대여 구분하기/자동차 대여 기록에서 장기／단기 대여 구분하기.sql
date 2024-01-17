select history_id, car_id,
    date_format(start_date, '%Y-%m-%d') as start_date,
    date_format(end_date, '%Y-%m-%d') as end_date,
    case when datediff(end_date, start_date) >= 29 then '장기 대여'
    else '단기 대여'
    end as rent_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(START_DATE, '%Y-%m') = '2022-09'
order by 1 desc