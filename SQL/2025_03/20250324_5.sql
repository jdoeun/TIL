-- programmers: 잡은 물고기의 평균 길이 구하기

SELECT ROUND(AVG(IFNULL(LENGTH, 10)),2) AS AVERAGE_LENGTH
FROM FISH_INFO;