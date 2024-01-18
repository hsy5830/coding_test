select F.flavor

from (select flavor, sum(total_order) as f_order
           from FIRST_HALF
           group by flavor) F
inner join (select flavor, sum(total_order) as j_order
           from JULY
           group by flavor) J           
on F.flavor = J.flavor

order by F.f_order + J.j_order desc

limit 3