select food_type, rest_id, rest_name, favorites
from (
    select *, 
           rank() over (partition by food_type order by favorites desc) as f_rank
    from rest_info) rest_info_rank
where f_rank = 1
order by food_type desc