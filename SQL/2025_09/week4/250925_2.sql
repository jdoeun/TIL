-- solvesql: 멀티 플랫폼 게임 찾기

with plat as (
    select name,
           platform_id,
           case
               when name in ('PS3', 'PS4', 'PSP', 'PSV') then 'Sony'
               when name in ('Wii', 'WiiU', 'DS', '3DS') then 'Nintendo'
               when name in ('X360', 'XONE') then 'Microsoft'
           end as company
    from platforms
)

select distinct g.name
from games as g
join plat as p
on g.platform_id = p.platform_id
where g.year >= 2012
group by g.name
having count(distinct p.company) >= 2