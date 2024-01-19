select I.animal_id, I.animal_type, I.name

from ANIMAL_INS I
left join ANIMAL_OUTS O
    on I.animal_id = O.animal_id
    
where I.SEX_UPON_INTAKE like '%Intact%'
    and O.SEX_UPON_OUTCOME not like '%Intact%'
    
order by 1