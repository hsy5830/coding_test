-- 코드를 입력하세요
SELECT U.user_id, U.nickname, sum(price) as TOTAL_SALES
from USED_GOODS_BOARD B
inner join USED_GOODS_USER U
    on B.writer_id = U.user_id
where status = 'DONE'
group by U.user_id having sum(price) >= 700000
order by 3