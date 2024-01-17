-- 코드를 입력하세요
select car_id, if(group_concat(availability) like '%대여중%', '대여중', '대여 가능')
from (SELECT distinct car_id,
    case
        when '2022-10-16' between start_date and end_date then '대여중'
        else '대여 가능'
    end as availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY) t1
group by car_id
order by 1 desc