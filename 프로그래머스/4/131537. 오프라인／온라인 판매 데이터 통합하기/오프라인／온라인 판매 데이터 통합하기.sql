(select date_format(SALES_DATE, '%Y-%m-%d') as sales_date, PRODUCT_ID, USER_ID, SALES_AMOUNT
from online_sale
where date_format(sales_date, '%Y-%m') = '2022-03'
)

union

(select date_format(SALES_DATE, '%Y-%m-%d') as sales_date, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
from offline_sale
where date_format(sales_date, '%Y-%m') = '2022-03'
)

order by SALES_DATE, PRODUCT_ID, USER_ID