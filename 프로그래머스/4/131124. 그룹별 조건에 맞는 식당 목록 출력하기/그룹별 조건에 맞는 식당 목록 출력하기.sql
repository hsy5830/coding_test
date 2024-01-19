select M.member_name, R.review_text, date_format(R.review_date, '%Y-%m-%d') as review_date

from REST_REVIEW R
inner join MEMBER_PROFILE M
    on R.member_id = M.member_id

where M.member_id = (select member_id
                      from REST_REVIEW
                    group by 1
                    order by count(*) desc
                    limit 1)

order by 3, 2