-- programmers: 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기

SELECT A.EMP_NO, A.EMP_NAME,
    CASE
        WHEN AVG(SCORE) >= 96 THEN 'S'
        WHEN AVG(SCORE) >= 90 THEN 'A'
        WHEN AVG(SCORE) >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN AVG(SCORE) >= 96 THEN A.SAL * 0.2
        WHEN AVG(SCORE) >= 90 THEN A.SAL * 0.15
        WHEN AVG(SCORE) >= 80 THEN A.SAL * 0.1
        ELSE 0
    END AS BONUS

FROM HR_EMPLOYEES AS A
JOIN HR_GRADE AS B
ON A.EMP_NO = B.EMP_NO
GROUP BY A.EMP_NO
ORDER BY A.EMP_NO