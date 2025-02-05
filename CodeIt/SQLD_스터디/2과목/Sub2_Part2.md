# SQLD 2과목 PART 2

## SQL 활용

### 서브쿼리(Subquery)

- <span style='color:pink'><U>하나의 SQL 문 안에 포함된 또 다른 SQL 문을 의미</U></span>
- 반드시 <span style='color:pink'><U>괄호로 묶어야 함</U></span>

![서브쿼리관련](https://thebook.io/img/006977/168.jpg)

### 서브쿼리 종류(동작 방식에 따른)

1. UN-CORRELATED(비연관) 서브쿼리

- 서브쿼리에 메인쿼리(외부쿼리) 테이블의 컬럼을 가지고 있지 않은 형태의 서브 쿼리
- 서브쿼리가 메인쿼리의 값을 참조하지 않고 독립적으로 실행함
- 서브쿼리는 한번만 실행됨

2. CORRELATED(연관) 서브쿼리

- 서브쿼리에 메인쿼리(외부쿼리) 테이블의 컬럼을 가지고 있는 형태의 서브쿼리
- 서브쿼리가 메인쿼리의 컬럼을 참조하고 있기 때문에 서브쿼리의 실행이 메인쿼리와 독립적이지 않음
- <SPAN STYLE='COLOR:PINK'>메인 쿼리의 각 행에 대해 서브쿼리가 실행됨</SPAN>

### 서브쿼리 종류(위치에 따른)

| 위치              | 이름                             |
| ----------------- | -------------------------------- |
| SELECT절          | 스칼라 서브쿼리(Scalar Subquery) |
| FROM절            | 인라인 뷰(Inline view)           |
| WHERE절, HAVING절 | 중첩 서브쿼리(Nested Subquery)   |

+GROUP BY절과 기타 DML절(INSERT, DELETE, UPDATE)절도 가능함

1. 스칼라 서브쿼리

- 서브쿼리 결과를 하나의 컬럼처럼 사용하기 위해 주로 사용 -<SPAN STYLE ='COLOR:PINK'>SELECT 절에 사용되는 쿼리로, 마치 하나의 컬럼처럼 표현하기 위해 사용</SPAN>(단, 하나의 출력 대상만 표현 가능)
- 각 행마다 스칼라 서브쿼리 결과가 하나여야 함(단일행 서브쿼리 형태)
- 조인의 대체 연산
- 스칼라 서브쿼리를 사용한 조인 처리 시 OUTER JOIN이 기본(값이 없더라도 생략되지 않고 NULL로 출력됨)

예제) EMP 의 각 직원의 사번, 이름과 부서이름을 출력(부서 이름을 스칼라 서브쿼리로)

```SQL
SELECT EMPNO, ENAME
    (SELECT DNAME
    FROM DEPT D
    WHERE D.DEPNO = E.DEPNO) AS DNAME
FROM EMP E
WHERE DEPNO = 10;
```

2. 인라인 뷰

- 서브쿼리 결과를 테이블처럼 사용하기 위해 주로 사용
- <SPAN STYLE='COLOR:PINK'>쿼리 안의 뷰의 형태로, 테이블처럼 조회할 데이터를 정의하기 위해 사용</SPAN>
- 테이블명이 존재하지 않기 때문에 다른 테이블과 조인 시 **반드시 테이블 별칭을 명시**해야함
- <SPAN STYLE='COLOR:PINK'>서브쿼리에서 출력되는 결과를 메인 쿼리의 어느 절에서도 사용할 수 있음</SPAN>
- 인라인 뷰의 결과는 메인 쿼리 테이블과 조인할 목적으로 주로 사용
- 모든 비교 연산자 사용 가능

예제) EMP 테이블에서 부서별 최대 급여자를 출력하되, 최대 급여와 함깨 출력

```SQL
SELECT E.EMPNO, E.ENAME, I.MAX_SAL
FROM EMP E, (SELECT DEPNO, MAX(SAL) AS MAX_SAL
            FROM EMP
            GROUP BY DEPNO) I
WHERE E.DEPNO = I.DEPNO
AND E.SAL = I.MAX_SAL;
```

3.  WHERE절 서브쿼리

- 가장 일반적인 쿼리로 비교 상수 자리에 값을 전달하기 위한 목적으로 주로 사용(상수항의 대체)
  3-1) 단일행 서브쿼리

  - 서브쿼리 결과가 1개의 행만 리턴되는 형태

  | 연산자 | 의미        |
  | ------ | ----------- |
  | =      | 같다        |
  | <>     | 같지 않다   |
  | >      | 크다        |
  | >=     | 크거나 같다 |
  | <      | 작다        |
  | <=     | 작거나 같다 |

  ```SQL
  SELECT EMPNO, ENAME, SAL
  FROM EMP
  WHERE SAL > (SELECT AVG(SAL)
      FROM EMP);
  ```

  3-2) 다중행 서브쿼리

  - 서브쿼리 결과가 여러 행을 리턴하는 형태
  - 비교 연산자는 사용 불가
  - 서브쿼리 결과를 한 행으로 요약하거나 다중행 서브쿼리 연산자를 사용하여 해결

  -다중행 서브쿼리 연산자

  | 연산자     | 의미                                    |
  | ---------- | --------------------------------------- |
  | IN         | 같은 값을 찾음                          |
  | >ANY       | 최소값을 반환함                         |
  | <ANY       | 최대값을 반환함                         |
  | <ALL       | 최소값을 반환한                         |
  | >ALL       | 최대값을 반환함                         |
  | EXISTS     | 서브쿼리가 하나 이상의 결과 반환시 TRUE |
  | NOT EXISTS | 서브쿼리가 결과를 반환하지 않으면 TRUE  |

  ```SQL
  SELECT NAME
  FROM EMP3
  WHERE DEPTNO IN (SELECT DEPTNO
                  FROM DEP3
                  WHERE LOC = 'SEOUL');
  ```

  #### ALL VS ANY

  ```
  > ALL(200,300) : 최대값(300)보다 큰 행들 반환
  < ALL(200,300) : 최소값(200)보다 작은 행들 반환
  > ANY(200,300) : 최소값(200)보다 큰 행들 반환
  < ANY(200,300) : 최대값(300)보다 작은 행들 반환
  ```

  ```SQL
  SELECT EMPNO, ENAME, SAL
  FROM EMP
  WHERE SAL > (SELECT MIN(SAL)
              FROM EMP
              WHER DEPNO = 10);
  ```

  위 아래 결과는 동일함

  ```SQL
  SELECT EMPNO, ENAME, SAL
  FROM EMP
  WHERE SAL > ANY(SELECT SAL
              FROM EMP
              WHER DEPNO = 10);
  ```

  #### EXISTS / NOT EXISTS 연산자

  - 서브쿼리 조건에 따라 메인쿼리의 출력 결과가 달라짐
  - 서브쿼리 SELECT 절의 출력 형태는 중요하지 않음
  - 연관 서브쿼리를 사용하여 연관 조건의 결과에 따라 메인쿼리 출력을 제한할 수 있음

  | 연산자     | 특징                                                 |
  | ---------- | ---------------------------------------------------- |
  | EXISTS     | 서브쿼리 결과가 하나라도 존재하면 메인쿼리 출력      |
  | NOT EXISTS | 서브쿼리 결과가 존재하지 않으면 메인쿼리 데이터 출력 |

  3-3) 다중컬럼 서브쿼리

  - 서브쿼리 결과가 여러 컬럼을 리턴하는 형태
  - 메인쿼리와 비교하는 컬럼이 2개 이상이 형태
  - 대소 비교 조건 전달 불가

  3-4) 상호연관 서브쿼리

  - <span style='color:pink'>메인쿼리와 서브쿼리 간의 비교를 수행하는 형태</span>
  - 비교할 집단이나 조건은 서브쿼리에 명시되어야 함
  - 서브쿼리가 메인쿼리의 컬럼을 참조하고 있기 때문에, 메인쿼리 실행 시 서브쿼리가 항상 실행되는 형태

  ```SQL
  SELECT EMPNO, ENAME, SAL, DEPNO
  FROM EMP E1
  WHERE SAL > (SELECT AVG(SAL)
               FROM EMP E2
               WHERE E1.DEPNO = E2.DEPNO
               GROUP BY DEPNO);
  ```

### 서브 쿼리 주의 사항

- 특별한 경우를 제외하고는 서브 쿼리절에 ORDER BY 절 사용 불가
- 단일 행 서브쿼리와 다중 행 서브쿼리에 따라 연산자 선택이 중요

## 집합 연산자

### 집합 연산자

- SELECT문 결과를 하나의 집합으로 간주, 그 <SPAN STYLE = 'COLOR:PINK'>집합에 대한 합집합, 교집합, 차집합 연산</SPAN>
- SELECT문과 SELECT문 사이에 집합 연산자 정의
- <SPAN STYLE='COLOR:PINK'>두 집합의 컬럼이 동일하게 구성되어야 함(각 컬럼의 데이터 타입과 순서 일치 필요)</SPAN>
- 전체 집합의 데이터 타입과 컬럼명은 첫번째 집합에 의해 결점됨

#### 합집합

- 두 집합의 총 합(접체)출력
- UNION과 UNION ALL 사용 가능

1\_) UNION

- 중복된 데이터는 한번만 출력
- <SPAN STYLE='COLOR:PINK'>중복된 데이터를 제거하기 위해 내부적으로 정렬 수행</SPAN>
- <SPAN STYLE='COLOR:PINK'>중복된 데이터가 없을 경우는 UNION 사용 대신 UNION ALL사용</SPAN>(불필요한 정렬 발생할 수 있으므로)

2\_) UNION ALL

- 중복된 데이터도 전체 출력

#### 교집합

- **두 집합 사이에 INTERSECT**
- 두 집합의 교집합(공통으로 있는 행)출력

#### 차집합

- **두 집합 사이에 MINUS 전달**
- **두 집합의 차집합(한 쪽 집합에만 존재하는 행)출력**
- A-B와 B-A는 다르므로 <SPAN STYLE='COLOR:PINK'>**집합의 순서 주의!**</SPAN>

### 집합 연산자 사용시 주의 사항

1. 두 집합의 컬럼 수 일치
2. 두 집합의 컬럼 순서 일치
3. 두 집합의 각 컬럼의 데이터 타입 일치
4. 각 컬럼의 사이즈는 달라도 됨
5. <U>개별 SELECT문에 ORDER BY 전달 불가(GROUP BY 전달 가능)</U>

## 그룹 함수

### 그룹함수

- 숫자함수 중 여러 값을 전달하여 하나의 요약 값을 출력하는 다중행 함수
- 수학/통계 함수들(기술통계 함수)
- GROUP BY 절에 의해 그룹별 연산 결과를 리턴함
- <SPAN STYLE='COLOR:PINK'>반드시 한 컬럼만 전달</SPAN>
- <U>NULL은 무시하고 연산</U>

#### COUNT

- 테이블의 행의 수를 세는 함수
- 인수 : \* 또는 하나의 표현식
- 문자, 숫자, 날짜 컬럼 모두 전달 가능
- NMULL은 세지 않는다
- COUNT(\*)은 항상 모든 행의 수를 출력

#### AVG

- 평균 출력
- 숫자 컬럼만 전달 가능
- <SPAN STYLE='COLOR:PINK'>NULL을 제외한 대상의 평균을 리턴하므로 전체 대상 평균 연산 시 주의</SPAN>

#### MAX/MIN

- 최대/최소 출력
- <SPAN STYLE='COLOR:PINK'>**날짜, 숫자, 문자 모두 가능(오름차순 순서대로 최소,최대 출력)**</SPAN>

#### VARIANCE/STDDEV

- 분산과 표준편차
- 표준편차는 분산의 루트값

#### GROUP BY FUNCTION

- GROUP BY 절에 사용하는 함수
- <SPAN STYLE='COLOR:PINK'>여러 GROUP BY 결과를 동시에 출력(합집합)하는 기능</SPAN>
- 그룹핑 할 그룹을 정의 (전체 소계 등)

1\_) GROUPING SETS(A,B,...)

- <SPAN STYLE='COLOR:PINK'>A별, B별 그룹 연산 결과 출력</SPAN>
- <SPAN STYLE='COLOR:PINK'>나열 순서 중요하지 않음</SPAN>
- 기본 출력에 전체 <SPAN STYLE='COLOR:PINK'>총계는 출력되지 않음</SPAN>
- NULL 혹은 () 사용하여 전체 총 합 출력 가능

2\_)ROLLUP(A,B)

- <SPAN STYLE='COLOR:PINK'>A별, (A,B)별, 전체 그룹 연산 결과 출력</SPAN>
- <SPAN STYLE='COLOR:PINK'>나열 순서 중요함</SPAN>
- 기본적으로<SPAN STYLE='COLOR:PINK'>전체 총 계가 출력됨</SPAN>

3\_) CUBE(A,B)

- <SPAN STYLE='COLOR:PINK'>A별, (A,B)별, 전체 그룹 연산 결과 출력됨</SPAN>
- 그룹으로 묶을 대상의 나열 순서 중요하지 않음
- 기본적으로 전체 총 계가 출력됨

## 윈도우 함수

### WINDOW FUNCTION

- <SPAN STYLE ='COLOR:PINK'>서로 다른 행의 비교나 연산을 위해 만든 함수</SPAN>
- GROUP BY를 쓰지 않고 그룹 연산 가능
- LAG, LEAD, SUM, AVG, MIN, MAX, COUNT, RANK

```SQL
SELECT 윈도우함수([대상]) OVER ([PARTITION BY 컬럼]
                              [ORDER BY 컬럼 AS|DESC]
                              [ROWS|RANGE BETWEEN A AND B]);
```

> PARTITION BY절 : 출력할 총 데이터 수 변화 없이 그룹연산 수행할 GROUP BY 컬럼  
> ORDER BY절 :

    - RANK의 경우 필수(정렬 컬럼 및 정렬 순서에 따라 순위 변화)
    - SUM, AVG, MIN, MAX, COUNT 등은 누적값 출력 시 사용

ROWS|RANGE BETWEEN A AND B

- 연산 범위 설정
- ORDER BY 절 필수

<SPAN STYLE='COLOR:PINK'>PARTITION BY, ORDER BY, ROWS 절 전달 순서 중요(ORDER BY를 PARTITON BY 전에 사용 불가)</SPAN>

예제) 그룹함수 오류(윈도우 함수가 필요한 이유)

```SQL
SELECT EMPNO, ENAME, SAL, DEPNO, SUM(SAL)
  FROM EMP
```

### 그룹 함수의 형태

- SUM,COUNT,AVG,MIN,MAX 등
- <SPAN STYLE='COLOR:PINK'>OVER절을 사용하여 윈도우 함수로 사용 가능</SPAN>
- 반드시 연산할 대상을 그룹함수의 입력값으로 전달

| 함수           | 의미                               |
| -------------- | ---------------------------------- |
| SUM OVER       | 전체 총 합, 그룹별 총 합 출력 가능 |
| AVG OVER       | SUM과 동일하게 사용                |
| MIN/MAX OVER() | SUM과 동일하게 사용                |
| COUNT          | SUM과 동일하게 사용                |

### 윈도우 함수 연산 대상 및 범위

ROWS|RANGE BETWEEN A AND B

<SPAN STYLE='COLOR:PINK'> \*\* 윈도우 함수의 연산 범위 : 집계 연산 시 행의 범위 설정 가능</SPAN>

1\_) 연산 대상(ROWS, RANGE 차이)

1. ROWS : 값이 같더라도 각 행씩 연산
2. RANGE : 같은 값의 경우 하나의 RANGE로 묶어서 동시 연산(DEFAULT)

2\_) BETWEEN A AND B

> A\_) 시작점 정의

    - CURRENT ROW : 현재행부터
    - UNBOUNDED PRECEDING : 처음부터(DEFAULT)
    - N PRECEDING : N 이전부터

> B\_) 마지막 시점 정의

    - CURRENT ROW : 현재행까지(DEFAULT)
    - UNBOUNDED FOLLOWING : 마지막까지
    - N FOLLOWING : N 이후까지

3\_) 특징

1. BETWEEN A : AND B 가 생략된 것으로 B는 DEFAULT 값인 CURRENT ROW가 적용된다.

## 순위 관련 함수

1. **RANK(순위)**

   1-1) RANK WITHIN GROUP

   > - <SPAN STYLE='COLOR:PINK'>특정값에 대한 순위 확인</SPAN>
   > - 윈도우함수가 아닌 일반함수

   예제) EMP에서 급여가 3000이면 전체 급여 순위가 얼마?

   ```SQL
   SELECT RANK(3000) WITHIN GROUP(ORDER BY SAL DESC) AS RANK_VALUE
   FROM EMP;
   ```

   1-2) RANK() OVER()

   > - <SPAN STYLE='COLOR:PINK'>전체 중/특정 그룹 중 값의 순위 확인</SPAN>
   > - <SPAN STYLE='COLOR:PINK'>ORDER BY 절 필수</SPAN>
   > - 순위를 구할 대상을 ORDER BY 절에 명시(여러 개 나열 가능)
   > - 그룹 내 순위 구할 시 PARTITION BY절 사용

   예제) 각 지원 이름, 부서번호, 급여, 부서별 급여 순위(큰 순서대로)

   ```SQL
   SELECT ENAME, DEPNO, SAL,
        RANK() OVER (PARTITION BY DEPNO ORDER BY SAL DESC) AS RANK1
   FROM EMP;
   ```

   1-3) DENSE_RANK

   > - <SPAN STYLE='COLOR:PINK'>누적 순위</SPAN>
   > - 값이 같을 때 <SPAN STYLE='COLOR:PINK'>동일한 순위 부여 후 다음 순위가 바로 이어지는 순위 부여 방식</SPAN>

   1-4) ROW_NUMBER

   > - <SPAN STYLE='COLOR:PINK'>연속된 행 번호</SPAN>
   > - 동일한 순위를 인정하지 않고 <SPAN STYLE='COLOR:PINK'>단순히 순서대로 나열한대로의 순서 값 리턴</SPAN>

### LAG, LEAD

- <SPAN STYLE='COLOR:PINK'>행 순서대로 각각 이전 값(LAG), 이후 값(LEAD) 가져오기</SPAN>
- <SPAN STYLE='COLOR:PINK'>ORDER BY 절 필수</SPAN>

### FIRST_VALUE, LAST_VALUE

- 정렬 순서대로 <SPAN STYLE='COLOR:PINK'>정해진 범위에서의 처음 값, 마지막 값 출력</SPAN>
- 순서와 범위 정의에 따라 최솟값과 최댓값 리턴 가능
- PARTITION BY, ORDER BY 절 생략 가능

### NTILE

- 행을 특정 컬럼 순서에 따라 <SPAN STYLE='COLOR:PINK'>정해진 수의 그룹으로 나누기 위한 함수</SPAN>
- <SPAN STYLE='COLOR:PINK'>그룹 번호가 리턴됨</SPAN>
- <SPAN STYLE='COLOR:PINK'>ORDER BY 필수</SPAN>
- PARTITION BY를 사용하여 특정 그룹을 도 원하는 수 만큼 그룹 분리 가능
- 총 행의 수가 명확히 나눠지지 않을 때 앞 그룹의 크기가 더 크게 분리됨

## 비율관련 함수

1. RATION_TO_REPORT

- 각 값이 전체 합에서 차지하는 비율을 계산
- <SPAN STYLE='COLOR:PINK'>ORDER BY 절 사용 불가</SPAN>

2. CUME_DIST

- 해당 값보다 작거나 같은 값의 비율을 계산
- <SPAN STYLE='COLOR:PINK'>ORDER BY절 필수</SPAN>

3. PERCENT_RANK

- 주어진 값이 데이터 집합 내에서 상대적으로 어디에 위치하는지를 비율(퍼센트)로 나타내는 함수
- 0과 1 사이의 값으로 표현
- ORDER BY절 필수

> $PERCENT\,RANK = \frac{RANK-1}{(총 행 수) -1}$

## TOP N QUERY

### TOP N QUERY

- 페이징 처리를 효과적으로 수행하기 위해 사용
- <SPAN STYLE='COLOR:PINK'>전체 결과에서 특정 N개 추출</SPAN>

### TOP N 행 추출 방법

1. ROWNUM
2. RANK
3. FETCH
4. TOP N(SQL SERVER)

#### ROWNUM

- 출력된 데이터 기준으로 행 번호 부여
- 절대적인 행 번호가 아닌 가상의 번호이므로 특정 행을 지정할 수 없음(=연산 불가)
- 첫번째 행이 증가한 이후 할당되므로 '>'연산 사용 불가(0은 가능)

#### FETCH절

- <SPAN STYLE='COLOR:PINK'>출력될 행의 수를 제한하는 절</SPAN>
- ORALCLE 12C 이상부터 제공(이전 버전에는 ROWNUM 주로 사용)
- SQL-SERVER 사용 가능
- ORDER BY 절 뒤에 사용(내부 파싱 순서도 ORDER BY 뒤)

문법)

```SQL
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
OFFSET N { ROW | ROWS }
FETCH { FIRST | NEXT} N { ROW | ROWS } ONLY
```

| 각 단어  | 의미                                                                        |
| -------- | --------------------------------------------------------------------------- |
| OFFSET   | 건너뛸 행의 수                                                              |
| N        | 출력할 행의 수                                                              |
| FETCH    | 출력할 행의 수를 전달하는 구문                                              |
| FIRST    | OFFSET을 쓰지 않았을 때 처음부터 N행 출력 명령                              |
| NEXT     | OFFSET을 사용했을 경우 제외한 행 다음부터 N 행 출력 명령                    |
| ROW,ROWS | 행의 수에 따라 하나일 경우 단수, 여러값이면 복수형(특별히 구분할 필요 없음) |

## 계층형 질의

### 계층형 질의

- <SPAN STYLE='COLOR:PINK'>하나의 테이블 내 각 행끼리 관계를 가질 때, 연결고리를 통해 행과 행 사이의 계층(depth)을 표현하는 기법</SPAN>
- <SPAN STYLE='COLOR:PINK'>PRIOR의 위치에 따라 연결하는 데이터가 달라짐</SPAN>

문법)

```SQL
SELECT 컬럼명
FROM 테이블명
START WITH 시작 조건      -- 시작점을 지정하는 조건 전달
CONNECT BY [NOCYCLE] PRIOR 연결조건;  -- 시작점 기준으로 연결 데이터를 찾아가는 조건
```

** START WITH : 데이터를 출력할 시작 지정하는 조건  
** CONNECT BY PRIOR : 행을 이어나갈 조건  
\*\* NOCYCLE : 순환이 발생하면 무한 루프가 될 수 있기 때문에 이를 방지하고자 사용

### 계층형 질의 조건

1. CONNECT BY절 조건

- 계층 구조를 설정하는 조건
- START WITH 절에서 시작한 데이터로부터 부모-자식 관계를 탐색하는 규칙을 정의
- 이 조건이 성립되지 않으면, 더 이상 자식 관계를 연결하지 않음
- START WITH 절 데이터가 항상 출력됨

2. WHERE절 조건

- 전체 결과를 필터링하는데 사용
- START WITH와 CONNECT BY 로 연결된 모든 결과가 출력된 후, WHERE절 조건에 맞는 데이터만 선택하여 출력
- START WITH절 데이터가 조건에 맞지 않는 경우 생략됨

#### 계층형 질의 가상 컬럼

1. LEVEL : 각 DEPTH를 표현(시작점부터 1)
2. CONNECT_BY_ISLEAF :LEAF NODE(최하위노드) 여부(참:1, 거짓:0)

#### 계층형 질의 가상 함수

1. CONNECT_BY_ROOT 컬럼명 : 루트노드의 해당하는 컬럼값
2. SYS_CONNECT_BY_PATH(컬럼, 구분자) : 이어지는 경로 출력
3. ORDER SIBLINGS BY 컬럼 : 같은 LEVEL일 경우 정렬 수행
4. CONNECT_BY_ISCYCLE : 계층형 쿼리의 결과에서 순환이 발생했는지 여부

---

## PIVOT과 UNPIVOT

### 데이터의 구조

1. LONG DATA(Tidy data)

- 하나의 속성이 하나의 컬럼으로 정의되어 값들이 여러 행으로 쌓이는 구조
- RDBMS 의 테이블 설계 방식
- 다른 테이블과의 조인 연산이 가능한 구조

2. WIDE DATA(Cross table)

- 행과 컬럼에 유의미한 정보 전달을 목적으로 작성하는 교차표
- 하나의 속성값이 여러 컬럼으로 분리되어 표현
- RDBMS에서 WIDE형식으로 테이블 설계시 값이 추가될 때마다 컬럼이 추가돼야 하므로 비효율적
- 다른 테이블과의 조인 연산이 불가함
- 주로 데이터를 요약할 목적으로 사용

### 데이터 구조 변경

1. PIVOT : LONG -> WIDE
2. UNPIVOT : WIDE -> LONG

### PIVOT

- <SPAN STYLE='COLOR:PINK'>교차표를 만드는 기능</SPAN>
- STACK컬럼, UNSTACK컬럼, VALUE컬럼의 정의가 중요
- FROM 절에 STACK, UNSTACK, VALUE 컬럼명만 정의필요(필요 시 서브쿼리 사용하여 필요 컬럼 제한)
- PIVOT 절에 UNSTACK, VALUE 컬럼명 정의
- <SPAN STYLE='COLOR:PINK'>PIVOT절 IN 연산자에 UNSTACK컬럼 값을 정의</SPAN>
- FROM 절에 선언된 컬럼 중 PIVOT절에서 선언한 VALUE컬럼, UNSTACK 컬럼을 제외한 모든 컬럼은 STACK 컬럼이 됨

문법)

```SQL
SELECT *
FROM 테이블명 또는 서브쿼리
PIVOT (VALUE 컬럼명 FOR UNSTACK컬럼명 IN (값1,값2,값3));
```

<SPAN STYLE='COLOR:PINK'>\* 반드시 FROM 절에 STACK컬럼, UNSTACK컬럼, VALUE 컬럼 모두 명시!</SPAN>

### UNPIVOT

- WIDE 데이터를 LONG 데이터로 변경하는 문법
- STACK 컬럼: 이미 UNSTACK되어 있는 여러 컬럼을 하나의 컬럼으로 STACK시 <SPAN STYLE='COLOR:PINK'>새로 만들 컬럼이름(사용자 정의)</SPAN>
- VALUE 컬럼 : 교차표에서 셀 자리(VALUE)값을 하나의 컬럼으로 표현하고자 할 때 <SPAN STYLE='COLOR:PINK'>새로 만들 컬럼명(사용자 정의</SPAN>)
- 값1, 값2 ... : <SPAN STYLE='COLOR:PINK'>실제 UNSTACK되어 있는 컬럼 이름들</SPAN>

문법)

```SQL
SELECT *
FROM 테이블명 또는 서브쿼리
UNPIVOT (VALUE컬렴명 FOR STACK컬럼명 IN (값1, 값2,...));
```

### 정규 표현식

- <SPAN STYLE='COLOR:PINK'>문자열의 공통된 규칙을 보다 일반화하여 표현하는 방법</SPAN>
- 정규 표현식 사용 가능한 문자함수 제공(regexp_replace, regexp_substr,regexp_instr,...)

### 정규 표현식 종류

![정규표현식](https://blog.kakaocdn.net/dn/GTGrV/btsFzfEinWz/Lsv8S40A782XaDhjROq6UK/img.png)

#### REGEXP_REPLACE

- 정규식 표현을 사용한 문자열 치환 가능

문법)

> (대상, 찾을 문자열, [바꿀문자열], [검색위치], [발견횟수],[옵션])

1. 특징

- <SPAN STYLE='COLOR:PINK'>바꿀 문자열 생략 시 문자열 삭제</SPAN>
- <SPAN STYLE='COLOR:PINK'>검색 위치 생략 시 1</SPAN>
- <SPAN STYLE='COLOR:PINK'>발견 횟수 생략시 0(모든)</SPAN>

2. 옵션

- c : 대소를 구분하여 검색
- i : 대소를 구분하지 않고 검색
- m : 패턴을 다중라인으로 선언 가능

#### REGEXP_SUBSTR

- 정규식 표현식을 사용한 문자열 추출
- 옵션은 REGEXP_SUBSTR과 동일

문법)

> REGEXP_SUBSTR(대상, 패턴, [검색위치],[발견횟수],[옵션],[추출그룹])

- 특징
  - <SPAN STYLE='COLOR:PINK'>검색 위치 생략 시 1</SPAN>
  - <SPAN STYLE='COLOR:PINK'>발견 횟수 생략시 1</SPAN>
  - 추출그룹은 서브패턴을 추출 시 그 중 추출할 서브패턴 번호

#### REGEXP_INSTR

- 주어진 문자열에서 특정패턴의 시작 위치를 반환

문법)

> REGEXP_INSTR(원본, 찾을패턴,[시작위치],[발견횟수],[출력옵션],[옵션],[추출그룹])

- 출력 옵션

1. 0(default) : 문자열의 시작위치 리턴
2. 1 : 문자열의 끝위치 리턴

- 특징

1. <SPAN STYLE='COLOR:PINK'>시작위치 생략 시 처음부터 확인(기본값:1)</SPAN>
2. <SPAN STYLE='COLOR:PINK'>발견횟수 생략 시 처음 발견된 문자열 위치 리턴</SPAN>

#### REGEXP_LIKE

- 주어진 문자열에서 특정패턴을 갖는 경우 반환(WHERE절 사용만 가능)
- 옵션 REGEXP_REPLACE와 동일

문법)

> REGEXP_LIKE(원본, 찾을문자열, [옵션])

#### REGEXP_COUNT

- 주어진 문자열에서 특정패턴의 횟수를 반환
- 옵션 REGEXP_REPLACE와 동일

문법)

> REGEXP_COUNT(원본, 찾을문자 열, [옵션])
