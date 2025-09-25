-- solvesql: 친구 수 집계하기

with cal as (
    select user_a_id as user_id, count(user_b_id) as cnt
    from edges
    group by user_a_id
    union all
    select user_b_id as user_id, count(user_a_id) as cnt
    from edges
    group by user_b_id
)

select users.user_id,
       ifnull(sum(cnt), 0) as num_friends
from users
left join cal on users.user_id = cal.user_id
group by user_id
order by 2 desc, 1