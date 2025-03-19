-- programmers: 특정 형질을 가지는 대장균 찾기

SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA A
WHERE 1=1
    AND (GENOTYPE & 2) != 2
    AND ((GENOTYPE & 4) = 4 OR (GENOTYPE & 1) = 1);
    -- 왼쪽부터 0010(=2)번 비트는 없어야 하고,
    -- 0001(=1)번 0100(=4)번 비트는 있어야 함