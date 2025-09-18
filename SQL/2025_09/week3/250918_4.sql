-- solvesql: 멘토링 짝꿍 리스트

select mentee.employee_id as mentee_id,
  mentee.name as mentee_name,
  mentor.employee_id as mentor_id,
  mentor.name as mentor_name
from employees mentee
left join employees mentor
  on mentor.join_date <= '2019-12-31' -- 멘토 없는 멘티도 있어야 함
  and mentee.department != mentor.department
where mentee.join_date between '2021-10-01' and '2021-12-31'
order by mentee_id, mentor_id