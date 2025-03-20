-- programmers: 대장균의 크기에 따라 분류하기 1

SELECT ID,
    CASE
        WHEN
            SIZE_OF_COLONY > 1000 THEN "HIGH"
        WHEN
            SIZE_OF_COLONY > 100 THEN "MEDIUM"
        ELSE
            "LOW"
    END AS SIZE

FROM ECOLI_DATA
ORDER BY ID;