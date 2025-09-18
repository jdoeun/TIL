-- solvesql: 복수 국적 메달 수상한 선수 찾기

SELECT name
FROM records r
JOIN athletes a on r.athlete_id = a.id
JOIN games g on r.game_id = g.id
WHERE medal IS NOT NULL
AND year >= 2000
GROUP BY a.id
HAVING COUNT(distinct team_id) >= 2
ORDER BY name