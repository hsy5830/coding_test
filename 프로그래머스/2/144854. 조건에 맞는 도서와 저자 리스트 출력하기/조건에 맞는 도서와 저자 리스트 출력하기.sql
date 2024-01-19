select B.book_id, A.author_name, date_format(B.published_date, '%Y-%m-%d') as published_date

from book B
inner join author A
    on B.author_id = A.author_id
    
where B.category = '경제'

order by 3