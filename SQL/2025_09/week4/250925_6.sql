-- solvesql: 세 명이 서로 친구인 관계 찾기

WITH ab AS (
    SELECT E1.user_a_id, E1.user_b_id, E2.user_b_id AS user_c_id
    FROM edges AS E1
    JOIN edges AS E2
        ON E1.user_b_id = E2.user_a_id
),
ac AS (
    SELECT ab.user_a_id, ab.user_b_id, ab.user_c_id
    FROM ab
    JOIN edges AS E3
        ON ((ab.user_a_id = E3.user_a_id AND ab.user_c_id = E3.user_b_id)
         OR (ab.user_a_id = E3.user_b_id AND ab.user_c_id = E3.user_a_id))
)

SELECT *
FROM ac
WHERE user_a_id < user_b_id
AND user_b_id < user_c_id
AND 3820 IN (user_a_id, user_b_id, user_c_id)