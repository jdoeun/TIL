-- programmers: 특정 세대의 대장균 찾기

SELECT A.ID
FROM ECOLI_DATA AS A, ECOLI_DATA AS B, ECOLI_DATA AS C
WHERE C.PARENT_ID IS NULL
    AND C.ID = B.PARENT_ID
    AND B.ID = A.PARENT_ID
GROUP BY A.ID
ORDER BY A.ID;