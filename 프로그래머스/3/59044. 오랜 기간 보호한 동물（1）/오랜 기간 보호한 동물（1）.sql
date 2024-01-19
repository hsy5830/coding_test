select I.name, I.datetime

from ANIMAL_INS I
left join ANIMAL_OUTS O
    on I.animal_id = O.animal_id
    
where O.animal_id is null

order by I.datetime

limit 3