# SQL문 정리

> 코딩테스트 및 백엔드 DB SQL문 공부 및 정리

## SELECT (조회)
```SQL
-- 이론
SELECT * FROM 테이블명; # 전체 컬럼 조회
SELECT 컬럼1, ... FROM 테이블명; # 일부 컬럼 조회
SELECT 컬럼1 AS 별칭 FROM 테이블명; # 별칭을 설정하여 조회
SELECT 컬럼1 FROM 테이블명 WHERE 조건; # 조건에 만족하는 데이터 조회

-- Example
SELECT * FROM ANIMAL_INS;
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS;
SELECT NAME AS 이름 FROM ANIMAL_INS;
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE ANIMAL_TYPE = 'DOG';
```

---

### : SELECT - 정렬 : ORDER BY
```SQL
-- 이론
SELECT * FROM 테이블명; # 정렬 X
SELECT * FROM 테이블명 ORDER BY 컬럼1 ASC[생략가능]; # 오름차순(기본 값)
SELECT * FROM 테이블명 ORDER BY 컬럼1 DESC; # 내림차순

SELECT * FROM 테이블명 ORDER BY 컬럼1, 컬럼2, ...; # 여러 컬럼으로 정렬
SELECT * FROM 테이블명 WHERE 조건 ORDER BY 컬럼1;
SELECT * FROM 테이블명 WHERE 조건 ORDER BY 컬럼번호1, 컬럼번호2, ...; # 컬럼 번호로 정렬

-- Example
SELECT * FROM ANIMAL_INS ORDER BY AGE ASC;
SELECT * FROM ANIMAL_INS ORDER BY AGE DESC;
SELECT * FROM ANIMAL_INS ORDER BY AGE DESC, NAME; # AGE 내림차순, NAME 오름차순 정렬
```

---

### : SELECT - 상위 N개 : LIMIT
```SQL
-- 이론
SELECT * FROM 테이블명 LIMIT 개수;

-- Example
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;
```

---

### : SELECT - 데이터 갯수 : COUNT
```SQL
-- 이론
SELECT COUNT(컬럼) FROM 테이블명;
SELECT COUNT(컬럼) AS COUNT FROM 테이블명;

-- Example
SELECT COUNT(NAME) AS COUNT FROM ANIMAL_INS;
```

---

### : SELECT - 최대, 최소 값, 합계 : MAX, MIN, SUM
```SQL
-- 이론
SELECT MAX(컬럼) FROM 테이블명;
SELECT MIN(컬럼) FROM 테이블명;
SELECT SUM(컬럼) FROM 테이블명;

-- 중복 제거
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NOT NAME IS NULL;
```

---

### : SELECT - 그룹화 : GROUP BY, HAVING
```SQL
-- 이론
SELECT 컬럼 FROM 테이블명 GROUP BY 그룹화할 컬럼;
SELECT 컬럼 FROM 테이블명 WHERE 조건 GROUP BY 그룹화할 컬럼; # 조건 처리 후 그룹화
SELECT 컬럼 FROM 테이블명 GROUP BY 그룹화할 컬럼 HAVING 조건; # 컬럼 그룹화 후 조건 처리
SELECT 컬럼 FROM 테이블명 WHERE 조건 GROUP BY 그룹화할 컬럼 HAVING 조건; # 조건 처리 후 그룹화 후 조건 처리
SELECT 컬럼 
FROM 테이블명 
WHERE 조건 
GROUP BY 그룹화할 컬럼
HAVING 조건
ORDER BY 컬럼1, ... ASC[OR DESC];
```

---

### : SELECT - 시간 : NOW, DATE, DATEDIFF, TIMESTAMPDIFF, DATE_ADD, DATE_SUB, 추출
```SQL
-- 이론
SELECT NOW();
SELECT DATE_ADD(기준 날짜, INTERVAL);
SELECT DATE_SUB(기준 날짜, INTERVAL);

DAY(기준 날짜);
MONTH(기준 날짜);
YEAR(기준 날짜);
SECOND(기준 날짜);
MINUTE(기준 날짜);
HOUR(기준 날짜);

DATEDIFF(날짜1, 날짜2); # 날짜1 - 날짜2
TIMESTAMPDIFF(단위, 날짜1, 날짜2);

-- Example
SELECT DATE_ADD(NOW(), INTERVAL 1 SECOND[MINUTE, HOUR, DAY, MONTH, YEAR]);
```

---

## INSERT (삽입)
```SQL
-- 이론
INSERT INTO 테이블명(컬럼1, 컬럼2, ...) # 일부 컬럼
VALUES (값1, 값2, ...), (값1, 값2, ...); # 다수 추가

-- Example
INSERT INTO ANIMAL_INS(NAME, DATETIME)
VALUES ('ROOKIE', '2021-03-11'), ('RIER', '2021-03-04');;
```

---

## UPDATE (수정)
```SQL
-- 이론
UPDATE 테이블명 SET 컬럼1 = 수정값1, ...
WHERE 조건;

-- Example
UPDATE ANIMAL_INS SET NAME = '록시'; # 테이블 전체 수정
UPDATE ANIMAL_INS SET NAME = '록시' WHERE ANIMAL_ID = 0313; # 테이블 일부 수정
```

---

## DELETE (삭제)
```SQL
-- 이론
DELETE FROM 테이블명 WHERE 조건;

-- Example
DELETE FROM ANIMAL_INS; # 테이블 전체 삭제
DELETE FROM ANIMAL_INS WHERE ANIMAL_ID = 0313; # 테이블 일부 데이터 삭제
```

---

## CASE
```SQL
-- 이론
SELECT 
    CASE 
        WHEN 조건
        THEN 반환 값
        WHEN 조건
        THEN 반환 값
        ELSE 조건에 부합하지 않을 시의 반환값
    END
FROM 테이블명;

-- Example
SELECT IDX,
    CASE
        WHEN ANIMAL_TYPE = 'DOG'
        THEN '강아지'
        WHEN ANIMAL_TYPE = 'CAT'
        THEN '고양이'
        ELSE '다른 동물'
    END AS 종류
FROM ANIMAL_INS;
```

---

## WHERE: 조건 / 연산자
### 비교 연산자
- `=` : 같다
- `!=, <>` : 다르다
- `>, <` : 크다, 작다
- `>=, <=` : 크거나 같다, 작거나 같다

### 논리 연산자
- `AND, &&` : AND
- `OR, ||` : OR
```SQL
SELECT 컬럼 FROM 테이블명 WHERE 컬럼1 = 값1 AND 컬럼2 = 값2;
SELECT 컬럼 FROM 테이블명 WHERE 컬럼1 = 값1 OR 컬럼2 = 값2;
```

### 기타 연산자
- `IN(값1, 값2, ...)` : 안에 해당하는 값이 있는 경우
```SQL
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE ANIMAL_TYPE IN ('DOG', 'CAT');
```

- `NOT IN(값1, 값2, ...)` : 안에 해당하는 값이 없는 경우
```SQL
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE ANIMAL_TYPE NOT IN ('DOG', 'CAT');
```

- `BETWEEN A AND B` : A 이상 B 이하의 값
```SQL
SELECT NAME, AGE FROM ANIMAL_INS WHERE AGE BETWEEN 5 AND 10;
```

- `LIKE('값%'), LIKE('%값'), LIKE('%값%')` : 값이 처음, 끝, 앞뒤 모두 포함된 경우
```SQL
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE NAME LIKE 'ROOKIE%';
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE NAME LIKE '%ROOKIE';
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE NAME LIKE '%ROOKIE%';
```

- `NOT LIKE('값%'), NOT LIKE('%값'), NOT LIKE('%값%')` : 값이 처음, 끝, 앞뒤 모두 포함 안된 경우
```SQL
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE NAME NOT LIKE 'ROOKIE%';
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE NAME NOT LIKE '%ROOKIE';
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE NAME NOT LIKE '%ROOKIE%';
```

- `IS NULL` : NULL인 경우
```SQL
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE ANIMAL_TYPE IS NULL;
```

- `IFNULL` : 만약 NULL일 경우 처리
```SQL
SELECT IFNULL(NAME, 'UNKNOWN') FROM ANIMAL_INS; 
```

- `IS NOT NULL` : NULL이 아닌 경우
```SQL
SELECT NAME, ANIMAL_TYPE FROM ANIMAL_INS WHERE ANIMAL_TYPE IS NOT NULL;
```

---

## JOIN (매우 중요 ***)
### LEFT JOIN : 부분 집합
```SQL
-- 이론
SELECT 컬럼
FROM 테이블1
LEFT JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼;

-- Example

```

### RIGHT JOIN : 부분 집합
```SQL
-- 이론
SELECT 컬럼
FROM 테이블1
RIGHT JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼;

-- Example

```

### INNER JOIN : 교집합
```SQL
-- 이론
SELECT 컬럼
FROM 테이블1
INNER JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼;

-- Example

```

### OUTER JOIN : 합집합
```SQL
-- 이론
SELECT 컬럼
FROM 테이블1
FULL OUTER JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼;

-- Example

```

### CROSS JOIN : 곱집합
```SQL
-- 이론
SELECT 컬럼
FROM 테이블1
CROSS JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼;

-- Example

```

### SELF JOIN : 자기 자신과의 곱집합
```SQL
-- 이론
SELECT 컬럼
FROM 테이블1
FULL OUTER JOIN 테이블2
ON 테이블1.컬럼 = 테이블2.컬럼;

-- Example

```

---

## WITH RECURSIVE : 가상 테이블
```SQL
-- 이론
WITH RECURSIVE 가상테이블명 AS *서브쿼리

*서브쿼리 : (
    SELECT 0 AS HOUR # 초기값
    UNION ALL # 위 쿼리와 아래 쿼리의 값을 연산
    SELECT HOUR + 1 FROM 가상테이블명 # 하나씩 불러서 +1 연산 수행
    WHERE 조건 # 반복을 멈추는 용도
)

SELECT 컬럼1, ... FROM 가상테이블명;

-- Example
WITH RECURSIVE CTE AS (
    SELECT 0 AS HOUR #초기값 설정
    UNION ALL #위 쿼리와 아래 쿼리의 값을 연산
    SELECT HOUR + 1 FROM CTE #하나씩 불려 나감
    WHERE HOUR < 23 #반복을 멈추는 용도
)

SELECT CTE.HOUR, COUNT(HOUR(OUTS.DATETIME)) AS COUNT
FROM CTE
LEFT JOIN ANIMAL_OUTS AS OUTS
ON CTE.HOUR = HOUR(OUTS.DATETIME)
GROUP BY CTE.HOUR


```


## TABLE 기타 접근용
```SQL
-- 이론
SHOW TABLES
CREATE 테이블명
ALTER 테이블명
DROP 테이블명
...

```

---

## DATABASE 접근용
```SQL
-- 이론
CREATE 데이터베이스명
ALTER 데이터베이스명
...

-- Example

```
