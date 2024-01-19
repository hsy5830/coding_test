select P.product_id, P.product_name, sum(O.amount * P.price) as total_sales

from FOOD_ORDER O
inner join FOOD_PRODUCT P
    on O.product_id = P.product_id
    
where date_format(O.produce_date, '%Y-%m') = '2022-05' 

group by 1, 2

order by 3 desc, 1