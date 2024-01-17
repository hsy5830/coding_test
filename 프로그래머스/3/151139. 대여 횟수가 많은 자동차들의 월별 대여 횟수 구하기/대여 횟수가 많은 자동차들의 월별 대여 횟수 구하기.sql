-- 코드를 입력하세요
select month, car_id, records

from (SELECT month(start_date) as month,
            car_id,
            count(*) as records,
            sum(count(*)) over (partition by car_id) as c_records

from CAR_RENTAL_COMPANY_RENTAL_HISTORY

where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'

group by month, car_id) t1

where c_records >= 5

order by 1, 2 desc
