select hour(datetime), count(*)
from animal_outs
where hour(datetime) between 9 and 19
group by hour(datetime)
order by 1