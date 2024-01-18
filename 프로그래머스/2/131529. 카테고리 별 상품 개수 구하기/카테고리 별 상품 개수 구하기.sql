select left(product_code, 2) as product_code,
    count(*) as products 

from product

group by left(product_code, 2)

order by 1