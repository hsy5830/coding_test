select MCDP_CD as '진료과코드', count(*) as '5월예약건수'

from appointment

where date_format(apnt_ymd, '%Y-%m') = '2022-05'
    # and (apnt_cncl_yn = 'N' or apnt_cncl_yn is null)

group by MCDP_CD
order by 2, 1