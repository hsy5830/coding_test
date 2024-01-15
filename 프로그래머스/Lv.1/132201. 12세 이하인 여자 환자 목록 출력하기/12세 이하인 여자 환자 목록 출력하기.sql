select pt_name, pt_no, gend_cd, age, if(tlno is null, 'NONE', tlno) as tlno
from patient
where age <= 12 and gend_cd = 'W'
order by age desc, pt_name