-- programmers: 멸종위기의 대장균 찾기

-- 임시 테이블 생성
WITH RECURSIVE generations AS (
    -- 최초 부모가 없는 대장균 개체는 1세대
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 재귀적으로 각 개체의 자식을 찾아 세대를 계산
    SELECT E.ID, E.PARENT_ID, G.GENERATION + 1
    FROM ECOLI_DATA E
    JOIN generations G
    ON E.PARENT_ID = G.ID
)

-- 자식이 없는 개체들을 찾고 세대별로 카운트
SELECT COUNT(*) AS COUNT, G.GENERATION
FROM generations G
WHERE NOT EXISTS (
    SELECT 1
    FROM ECOLI_DATA CHILD
    WHERE CHILD.PARENT_ID = G.ID
)
GROUP BY G.GENERATION
ORDER BY G.GENERATION;