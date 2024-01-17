select category, sum(sales) as total_sales
from book_sales BS
left join book B
    on BS.book_id = B.book_id
where date_format(sales_date, '%Y-%m') = '2022-01'
group by category
order by category