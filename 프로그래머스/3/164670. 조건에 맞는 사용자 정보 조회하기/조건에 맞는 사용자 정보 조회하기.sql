select B.writer_id, 
    U.nickname, 
    concat(U.city, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as '전체주소',
    concat(substr(U.tlno, 1, 3), '-', substr(U.tlno, 4, 4), '-', substr(U.tlno, 8, 4)) as '전화번호'

from USED_GOODS_BOARD B
inner join USED_GOODS_USER U
    on B.writer_id = U.user_id
    
group by B.writer_id having count(*) >= 3

order by B.writer_id desc