select animal_id, name

from animal_ins

where name regexp 'EL|El|el'
    and animal_type = 'Dog'

order by name