-- solvesql: 서울숲 요일별 대기오염도 계산하기

SELECT
  CASE DATE_FORMAT(measured_at, "%w")
    WHEN '0' THEN '일요일'
    WHEN '1' THEN '월요일'
    WHEN '2' THEN '화요일'
    WHEN '3' THEN '수요일'
    WHEN '4' THEN '목요일'
    WHEN '5' THEN '금요일'
    WHEN '6' THEN '토요일'
  END AS weekday,
  round(avg(no2), 4) as no2,
  round(avg(o3), 4) as o3,
  round(avg(co), 4) as co,
  round(avg(so2), 4) as so2,
  round(avg(pm10), 4) as pm10,
  round(avg(pm2_5), 4) as pm2_5
FROM
  measurements
GROUP BY
  weekday
ORDER BY
  CASE
    WHEN weekday = '월요일' THEN 1
    WHEN weekday = '화요일' THEN 2
    WHEN weekday = '수요일' THEN 3
    WHEN weekday = '목요일' THEN 4
    WHEN weekday = '금요일' THEN 5
    WHEN weekday = '토요일' THEN 6
    WHEN weekday = '일요일' THEN 7
  END