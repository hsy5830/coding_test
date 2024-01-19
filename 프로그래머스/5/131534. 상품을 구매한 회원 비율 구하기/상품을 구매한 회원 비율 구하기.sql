select year(O.sales_date) as YEAR,
    month(O.sales_date) as MONTH,
    count(distinct U.user_id) as PUCHASED_USERS,
    round(count(distinct U.user_id)/(select count(*) from user_info where year(joined) = 2021), 1)as PUCHASED_RATIO
from USER_INFO as U
right join ONLINE_SALE as O
    on U.user_id = O.user_id
where year(U.joined) = 2021
group by YEAR, MONTH
order by YEAR, MONTH