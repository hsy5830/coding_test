set @h = -1;
with hour_table as (
    select @h := @h + 1 as hour
    from information_schema.tables
    limit 24
)

select hour_table.hour, if(h_count.hour is null, 0, h_count.count) as count
from hour_table 
left join (
    select hour(datetime) as hour, count(*) as count

    from ANIMAL_OUTS

    group by hour(datetime)

    order by 1
) h_count
on hour_table.hour = h_count.hour