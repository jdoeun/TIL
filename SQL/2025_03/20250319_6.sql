-- programmers: 12세 이하인 여자 환자 목록 출력하기

SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE GEND_CD LIKE 'W' AND AGE <= 12
ORDER BY AGE DESC, PT_NAME;