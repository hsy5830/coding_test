select concat('/home/grep/src/', B.board_id, '/', file_id, file_name, file_ext)

from USED_GOODS_BOARD B
inner join USED_GOODS_FILE F
    on B.board_id = F.board_id

where B.board_id = (select board_id
                 from USED_GOODS_BOARD
                 order by views desc
                 limit 1)

order by file_id desc

