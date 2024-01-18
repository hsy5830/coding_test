select A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD

from APPOINTMENT A
inner join PATIENT P
    on A.pt_no = P.pt_no
inner join DOCTOR D
    on A.mddr_id = D.dr_id
    
where date_format(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
    and A.mcdp_cd = 'CS'
    and A.APNT_CNCL_YN != 'Y'
    
order by A.APNT_YMD