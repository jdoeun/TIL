-- solvesql: 가구 판매의 비중이 높았던 날 찾기

select order_date,
       count(distinct case when category = 'Furniture' then order_id end) as furniture,
       round(
        (count(distinct case when category = 'Furniture' then order_id end) * 1.0 / count(distinct order_id)) * 100, 2
       ) as furniture_pct
from records
group by order_date
having count(distinct order_id) >= 10
    and furniture_pct >= 40
order by furniture_pct desc;