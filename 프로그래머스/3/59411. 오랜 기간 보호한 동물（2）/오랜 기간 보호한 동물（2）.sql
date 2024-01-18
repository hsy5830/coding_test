select I.animal_id, I.name

from ANIMAL_OUTS O
left join ANIMAL_INS I
    on O.animal_id = I.animal_id
    
order by datediff(O.datetime, I.datetime) desc

limit 2