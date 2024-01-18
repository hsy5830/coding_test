select animal_id, name,
    if(SEX_UPON_INTAKE regexp 'Spayed|Neutered', 'O', 'X') as SEX_UPON_INTAKE

from animal_ins

order by 1