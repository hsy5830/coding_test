select floor(price/10000) * 10000 as price_group,
    count(*) as products
from product
group by 1
order by 1