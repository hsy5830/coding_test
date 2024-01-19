select O.animal_id, O.name

from ANIMAL_INS I
right join ANIMAL_OUTS O
    on I.animal_id = O.animal_id
    
where I.animal_id is null
    
order by 1