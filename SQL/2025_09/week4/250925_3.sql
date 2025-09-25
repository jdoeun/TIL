-- solvesql: 전국 카페 주소 데이터 정제하기

SELECT
    SUBSTRING_INDEX(address, ' ', 1) AS sido,
    SUBSTRING_INDEX(SUBSTRING_INDEX(address, ' ', 2), ' ', -1) AS sigungu,
    COUNT(DISTINCT cafe_id) AS cnt
FROM cafes
GROUP BY sido, sigungu
ORDER BY 3 DESC