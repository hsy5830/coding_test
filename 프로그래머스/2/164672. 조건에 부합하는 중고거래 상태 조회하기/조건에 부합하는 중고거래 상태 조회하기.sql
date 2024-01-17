select board_id, writer_id, title, price,
    case when status = 'SALE' then '판매중'
         when status = 'RESERVED' then '예약중'
         when status = 'DONE' then '거래완료'
    end as status
from USED_GOODS_BOARD
where date_format(CREATED_DATE, '%Y-%m-%d') = '2022-10-05'
order by 1 desc