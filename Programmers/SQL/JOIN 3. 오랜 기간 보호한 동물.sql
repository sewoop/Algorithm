-- 코드를 입력하세요
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS AS INS
LEFT JOIN ANIMAL_OUTS AS OUTS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE OUTS.DATETIME IS NULL
ORDER BY INS.DATETIME, OUTS.DATETIME
LIMIT 3