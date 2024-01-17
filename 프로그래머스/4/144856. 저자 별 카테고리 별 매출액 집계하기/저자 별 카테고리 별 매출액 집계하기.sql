select A.author_id, A.author_name, B.category,
    sum(B.PRICE * BS.SALES) as total_sales

from book B
inner join author A
    on B.author_id = A.author_id
inner join book_sales BS
    on B.book_id = bs.book_id
    
where date_format(BS.sales_date, '%Y-%m') = '2022-01'

group by A.author_id, A.author_name, B.category

order by 1, 3 desc