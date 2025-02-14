# SQLD 2과목 PART 3

---

## DML(Data Manipulation Language)

- 데이터의 삽입(insert), 수정(update), 삭제(delete), 병합(merge)
- <span style='color:pink'>저장(commit) 혹은 취소(rollback) 반드시 필요</span>

### INSERT

- 테이블에 행을 삽입할 때 사용
- <SPAN STYLE='COLOR:PINK'>한 번에 한 행만 입력 가능(SQL Server, 여러 행 동시 삽입 가능)</SPAN>
- 하나의 컬럼에는 한 값만 삽입 가능
- <SPAN STYLE='COLOR:PINK'>컬럼별 데이터타입과 사이즈에 맞게 삽입</SPAN>
- INTO 절에 컬럼명을 명시하여 일부 컬럼만 입력 가능 <SPAN STYLE='COLOR:PINK'>작성하지 않은 컬럼은 NULL이 입력됨</SPAN>
- 전체 컬럼에 대한 데이터 입력시 테이블명 뒤의 컬럼명 생략 가능

```SQL
INSERT INTO 테이블 VALUES(값1, 값2, ...) -- 전체 컬럼의 값을 입력
INSERT INTO 테이블(컬럼1, 컬럼2, ...) VALUES(값1, 값2, ...) -- 선택한 컬럼만 데이터 입력
```

### UPDATE

- 데이터 수정할 때 사용
- 컬럼 단위 수행
- 다중 컬럼 수정 가능

  1. 단일컬럼 수정

  ```SQL
  UPDATE 테이블명
  SET 수정할컬럼명 = 수정값
  WHERE 조건;
  ```

  2. 다중컬럼 수정
     2-1) 방법1

  ```SQL
  UPDATE 테이블명
  SET 수정컬럼명 = 수정값1, 수정컬럼명2 = 수정값2, ...
  WHERE 조건;
  ```

  2-2) 방법2

  ```SQL
  UPDATE 테이블명
  SET (수정컬럼명1, 수정컬럼명2, ...) = (SELECT 수정값1, 수정값2, ...)
  WHERE 조건
  ```

### DELETE

- 데이터를 삭제할 때 사용
- 행 단위 실행

```SQL
DELETE [FROM] 테이블명
[WHERE 조건]
```

### MERGE

- 데이터 병합
- 참조 테이블과 동일하게 맞추는 작업(참조테이블의 데이터 입력, 참조테이블의 값으로 수정 등)

```SQL
MERGE INTO 테이블명
USING 참조테이블
ON (연결조건)   -- 괄호 필수
WHEN MATCHED THEN
    UPDATE    --UPDATE 테이블명 생략
    SET 수정 내용   -- COL1 = 1과 같은 형식
    DELETE (조건)   -- 괄호 생략 가능
WHEN NOT MATCHED THEN
    INSERT VALUES(값1, 값2, ...)
```

---

## TCL(Transaction Control Language)

- 트랜잭션 제어어로 COMMIT, ROLLBACK이 포함됨
- <SPAN STYLE='COLOR:PINK'>DML에 의해 조작된 결과를 작업단위(트랜잭션) 별로 제어하는 명령어</SPAN>
- DML 수행 후 트랜잭션을 정상 종료하지 않는 경우 LOCK 발생할 수 있음

* 잠금(LOCK)
  - 트랜잭션이 수앻하는 동안 <SPAN STYLE='COLOR:PINK'><U>특정 데이터에 대해서 다른 트랜잭션이 동시에 접근하지 못하도록 제한</U></SAPN>
  - 잠금이 걸린 데이터는 잠금을 실행한 트랜잭션만이 접근 및 해제 가능(관리자 권한 계정 제외)

### 트랜잭션

-트랜잭션은 데이터베이스의 <SPAN STYLE='COLOR:PINK'>논리적 연산 단위(하나의 연속적인 업무 단위)</SPAN>

- 하나의 트랜잭션에는 하나 이상의 SQL 문장이 포함
- 분할할 수 없는 최소의 단위
- <SPAN STYLE='COLOR:PINK'>ALL OR NOTHING 개념(모두 COMMIT 하거나 ROLLBACK 처리 해야 함)</SPAN>

* 특성

- 원자성(atomicity) : 트랜잭션 정의된 연산들 모두 성공적으로 실행되던지 아니면 전혀 실행되지 않은 상태로 남아 있어야 함
- 일관성(consistency) : 트랜잭션 실행 전 데이터베이스 내용이 잘못되어 있지 않다면 트랜잭션 실행 이후에도 데이터베이스 내용의 잘못이 있으면 안 됨
- 고립성(isolation) : 트랜잭션 실행도중 다른 트랜잭션의 영향을 받아 잘못된 결과를 만들어서는 안 됨
- 지속성(durability) : 트랜잭션이 성공적으로 수행되면 갱신한 데이터베이스 내용이 영구적으로 저장

### COMMIT

- 입력, 수정, 삭제한 데이터에 이상이 없을 경우 데이터를 저장하는 명령어
- 한 번 COMMIT을 수행하면 <SPAN STYLE='COLOR:PINK'><U>COMMIT 이전에 수행한 DML은 모두 저장되며 되돌릴 수 없음</U></SPAN>
- ORACLE은 DDL 시 AUTO COMMIT(23c버전부터 비활성화 가능)이지만 SQL Server는 AUTO COMMMIT 비활성화 설정 가능

### ROLLBACK

- 테이블 내 입력한 데이터나 수정한 데이터, 삭제한 데이터에 대해 변경을 취소하는 명령어
- 데이터베이스에 저장하지 않고 <SPAN STYLE='COLOR:PINK'><U>최종 COMMIT 지점/ 변경 전/ 특정 SAVEPOINT 지점으로 원복됨</U></SPAN>
- <SPAN STYLE='COLOR:PINK'><U>최종 COMMIT 시점 이전까지 ROLLBACK 가능</U></SPAN>
- SAVEPOIINT를 설정하여 최종 COMMIT 시점이 아닌, 그 이후의 원하는 시점으로의 원복 가능

* <U>SAVEPOINT</U>

- **트랜잭션 내에서 롤백을 부분적으로 수행하기 위해 사용되는 지점을 지정하는데 사용**
- **사용자가 원하는 위치에 원하는 이름으로 설정 가능**
- **ROLLBACK TO savepoint_name으로 원하는 지점으로 원복 가능(단, COMMIT 이전으로는 원복 불가)**

---

## DDL(Data Definition Language)

- 데이터 정의어
- <SPAN STYLE='COLOR:PINK'>데이터 구조 정의(객체 생성, 삭제, 변경) 언어</SPAN>
- CREATE(객체 생성),ALTER(객체 변경),DROP(객체 삭제), TRUNCATE(데이터 삭제)
- <SPAN STYLE='COLOR:PINK'>AUTO COMMIT(명령어 수행하면 즉시 저장,원복 불가)</SPAN>

### CREATE

- 테이블이나 인덱스와 같은 <SPAN STYLE='COLOR:PINK'><U>객체를 생성하는 명령어</U></SPAN>
- 테이블 생성 시 테이블명, 컬럼명, 컬럼순서, 컬럼크기, 컬럼의 데이터타입 정의 필수
- 테이블 생성 시 각 컬럼의 제약조건 및 기본값은 생략 가능
- <SPAN STYLE='COLOR:PINK'><U>테이블 생성 시 소유자 명시 가능(생략 시 명령어 수행 계정 소유)</U></SPAN>
- 숫자컬럼의 경우 컬럼 사이즈 생략 가능(날짜 컬럼은 사이즈 명시 X)

문법 1

```SQL
CREATE TABLE [소유자.]테이블명(
  컬럼1 데이터타입 [DEFAULT 기본값] [제약조건],
  컬럼2 데이터타입 [DEFAULT 기본값] [제약 조건],
  ...
);
```

문법 2

```SQL
CREATE TALBE 테이블명
AS
SELECT * FROM 복제테이블명;
```

\*\* 특징

- 복제테이블의 컬럼명과 컬럼의 데이터 타입이 복제됨
- SELECT문에서 컬럼별칭 사용 시 컬럼별칭 이름으로 생성
- CREATE문에서 컬럼명 변경 가능
- NULL 속성도 복제됨
- 테이블에 있는 **제약조건, INDEX 등은 복제되지 않음**

#### 데이터 타입

| 데이터 타입 | 설명                                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| CHAR(n)     | 고정형 문자 타입으로 사이즈 전달 필수, 사이즈만큼 확정형 데이터가 입력됨(빈자리수는 공백으로 채워짐) |
| VARCHAR2(n) | 기본형 문자타입으로 사이즈 전달 필수, 사이즈보다 작은 문자값이 입력되더라도 입력값 그대로 유지       |
| NUMBER(p,s) | 숫자형 타입으로 자리수 생략 가능, 소수점 자리 제한 시 s전달(p는 총 자리수)                           |
| DATE        | 날짜타입으로 사이즈 전달 불가                                                                        |

### ALTER

- 테이블 구조 변경(컬럼명, 컬럼 데이터 타입, 컬럼 사이즈, default 값, 컬럼삭제, 컬럼추가, 제약조건)
- 컬럼순서 변경 불가(재생성으로 해결)

1. 컬럼 추가

- 새로 추가된 컬럼위치는 맨 마지막(절대 중간 위치에 추가 불가)
- 컬럼 추가 시 데이터타입 필수, default값, 제약 조건을 명시할 수 있음
- <SPAN STYLE='COLOR:PINK'><U>여러 컬럼 동시 추가 가능(반드시 괄호 사용)</U></SPAN>

```SQL
ALTER TABLE 테이블명 ADD 컬럼명 데이터타입 [DEFAULT] [제약조건];
```

\*\* 주의!

> - 동시에 여러 컬럼을 추가할 경우 반드시 괄호와 함께 전달!
> - 컬럼 추가시 MOT NULL 속성 전달 불가(컬럼 추가 시 모두 NULL인 값을 갖고 추가되므로)
> - 컬럼 추가시 DEFAULT를 선언하면 MOT NULL속성을 갖는 컬럼 추가 가능

2. 컬럼(속성) 변경

- 컬럼 사이즈, 데이터타입, default 값 변경 가능
- 여러 컬럼 동시 변경 가능

```SQL
ALTER TABLE 테이블명 MODIFY(컬럼명 DEFAULT 값)
```

1)컬럼사이즈 변경

- 컬럼 사이즈 증가는 항상 가능
- 컬럼 사이즈 축소는 데이터 존재 여부에 따라 제한(데이터가 있는 경우 데이터의 최대 사이즈만큼 축소 가능)
- <SPAN STYLE='COLOR:PINK'><U>동시 변경 가능(반드시 괄호 필요)</SPAN> 2)데이터 타입 변경
- <SPAN STYLE='COLOR:PINK'><U>빈 컬럼일 경우 데이터 타입 변경 가능</U></SPAN>
- <SPAN STYLE='COLOR:PINK'><U>CHAR, VARCHAR 타입일 경우 데이터가 있어도 서로 변경 가능</U></SPAN>
  3)DEFAULT 값 변경
- DEFAULT 값이란 <SPAN STYLE='COLOR:PINK'><U>특정 컬럼에 값이 생략될 경우(입력 시 언급되지 않을 경우) 자동으로 부여되는 값</U></SPAN>
- INSERT 시 DEFAULT값이 선언된 컬럼에 NULL을 직접 입력할 때는 DEFAULT 값이 아닌 NULL이 입력됨</U></SPAN>
- 이미 데이터가 존재하는 테이블에 DEFAULT 값 선언 시 <U>기존 데이터 수정 안 됨(이후 입력된 데이터부터 적용)</SPAN>
- DEFAULT 값 해제 시 DEFAULT 값을 NULL로 선언

3. 컬럼이름 변경

- 항상 가능
- <SPAN STYLE='COLOR:PINK'><U>동시에 여러 컬럼 이름 변경 불가(괄호 전달 불가)</U></SPAN>
- ALTER...RENAME 명령어로 처리

```SQL
ALTER TABLE TABLE_NAME RENAME COLUMN 기존컬럼명 TO 새컬럼명;
```

4. 컬럼 삭제

- <SPAN STYLE='COLOR:PINK'><U>데이터 존재 여부와 상관없이 언제나 가능</U></SPAN>
- RECYCLEBIN에 남지X(FLASHBACK으로 복구 불가)
- <SPAN STYLE='COLOR:PINK'><U>동시 삭제 불가</U></SPAN>

### DROP

- 객체(테이블, 인덱스 등) 삭제
- DROP 후에는 조회 불가

```SQL
DROP TABLE 테이블명 [PURGE];
-- PURGE로 테이블 삭제시 RECYCLEBIN에서 조회 불가
```

### TRUNCATE

- 구조 남기고 데이터만 즉시 삭제, 즉시 반영(AUTO COMMIT)
- RECYCLEBIN에 남지 않음

```SQL
TRUNCATE TABLE 테이블명;
```

### DELETE/DROP/TRUNCATE 차이

- DELETE : 데이터 일부 또는 전체 삭제, 롤백 가능
- TRUNCATE : 데이터 전체 삭제만 가능(일부 삭제 불가), 즉시 반영(롤백 불가)
- DROP : 데이터와 구조를 동시 삭제, 즉시 반영(롤백 불가)

---

## 제약 조건

- 데이터 무결성을 위해 각 컬럼에 생성하는 데이터의 제약 장치
- 테이블 생성 시 정의 가능, 컬럼 추가 시 정의 가능, 이미 생성된 컬럼에 제약조건만 추가 가능

### 1 .PRIMARY KEY(기본키)

- 유일한 식별자(각 행을 구별할 수 있는 식별자 기능)
- 중복 허용 X, NULL 허용 X => UNIQUE + NOT NULL
- 특정 컬럼에 PRIMARY KEY생성하면 NOT NULL 속성 자동 부여(CTAS로 테이블 복사 시 복사되지 X)
- 하나의 테이블에 여러 기본키를 생성할 수 없음
- 하나의 기본키를 여러 컬럼을 결합하여 생성할 수 있음
- PRIMARY KEY 생성 시 자동으로 UNIQUE INDEX 생성

  1)테이블 생성 시 제약조건 생성

```SQL
CREATE TABLE 테이블명(
  컬럼1 데이터타입 [DEFAULT 기본값] [[CONSTRAINT 제약조건명] 제약조건종류],
  컬럼2 데이터타입 [DEFAULT 기본값] [[CONSTRAINT 제약조건명] 제약조건종류],
  ...
  [[CONSTRAINT 제약조건명] 제약조건종류]
);
```

2)컬럼 추가 시 제약 조건 생성

```SQL
ALTER TABLE 테이블명
ADD 컬럼명 데이터타입 [DEFAULT 기본값] [[CONSTRAINT 제약조건명] 제약조건종류];
```

3)이미 생성된 컬럼에 제약조건만 추가

```SQL
ALTER TABLE 테이블명 ADD [CONSTRAINT 제약조건명] 제약조건 종류;
```

3)제약조건 삭제

```SQL
ALTER TABLE 테이블명 DROP CONSTRAINT 제약조건명;
```

### 2. UNIQUE

- 중복을 허용하지 ㅇ낳음
- <SPAN STYLE='COLOR:PINK'><U>NULL은 허용</U></SPAN>
- UNIQUE INDEX 자동 생성

### 3. NOT NULL

- 다른 제약조건과 다르게 컬럼의 특징을 나타냄 => CTAS로 복제시 따라감
- 컬럼 생성 시 NOT NULL을 선언하지 않으면 Nullable 컬럼으로 생성됨
- 이미 만들어진 컬럼에 <SPAN STYLE='COLOR:PINK'><U>NOT NULL 선언 시 제약조건 생성이 아닌 컬럼 수정(MODIFY)으로 해결</U></SPAN>

### 4. FOREIGN KEY

- <SPAN STYLE='COLOR:PINK'><U>참조테이블의 참조 컬럼에 있는 데이터를 확인하면서 본 테이블 데이터를 관리할 목적으로 생성</U></SPAN>
- <SPAN STYLE='COLOR:PINK'><U>반드시 참조(부모)테이블의 참조 컬럼(REFERENCE KEY)이 사전에 PK 혹은 UNIQUE KEY를 가져야 함</U></SPAN>

```SQL
CREATE TABLE 테이블명(
  컬럼1 데이터타입 [DEFAULT 값] REFERENCES 참조테이블(참조키),
  ...
);
```

#### FOREIGN KEY 옵션(생성 시 정의, 변경 불가 -> 재생성)

1. ON DELETE CASCADE : 부모 데이터 삭제 시 자식 데이터 함께 삭제
2. ON DELETE SET NULL : 부모 데이터 삭제 시 자식 데이터의 참조값은 NULL로 수정

### 5. CHECK

- 직접적으로 데이터의 값 제한(양수,(1,2,3,4) 중 하나)

#### 기타 오브젝트

1)뷰(VIEW)

- 저장공간을 가지지는 않지만 테이블처럼 조회 및 수정할 수 있는 객체

\*\*뷰(VIEW)의 종류

- 단순뷰 : 하나의 테이블 조회 뷰(VIEW) -복합뷰 : 둘 이상의 테이블 조인 뷰(VIEW)

```SQL
CREATE [OR REPLACE] VIEW 뷰이름
AS
조회쿼리;

-- 뷰 삭제
DROP VIEW 뷰명;
```

2)시퀀스(SEQUENCE)

- 자동으로 연속적인 숫자 부여해주는 객체

```SQL
CREATE SEQUENCE 시퀀스명
INCREMENT BY      -- 증가값(DEFAULT : 1)
START WITH        -- 시작값(DEFAULT : 1)
MAXVALUE          -- 마지막값(증가시퀀스), 재사용시 시작값(감소시퀀스)
MINVALUE          -- 재사용시 시작값(증가시퀀스), 마지막값(감소시퀀스)
CYCLE | NOCYCLE   -- 시퀀스 재사용(DEFAULT : NOCYCLE)
CACHE N           -- 캐시값(DEFAULT : 20)
;
```

3)시노님(SYNONYM)

- 테이블 별칭 생성

```SQL
CREATE [OR REPLACE] [PUBLIC] SYNONYM 별칭 FOR 테이블명;
```

---

## DCL(Data Control Language)

- 데이터 제어어로 객체에 대한 권한을 부여(GRANT)하거나 회수(REVOKE)하는 기능
- <SPAN STYLE='COLOR:PINK'><U>테이블 소유자는 타계정에 테이블 조회 및 수정 권한 부여 및 회수 가능</U></SPAN>

### 권한

1. 오브젝트권한

- 테이블에 대한 권한 제어
- 테이블 소유자는 타계정에 소유 테이블에 대한 조회 및 수정 권한 부여 및 회수 가능

2. 시스템 권한

- 시스템 작업(테이블 생성 등)등을 제어
- 관리자 권한만 권한 부여 및 회수 가능

### GRANT

- 권한 부여 시 반드시 테이블 소유자나 관리자계정(SYS, SYSTEM)으로 접속하여 권한을 부여하여야 함
- <SPAN STYLE='COLOR:PINK'><U>동시에 여러 유저에 대한 권한 부여 가능</U></SPAN>
- <SPAN STYLE='COLOR:PINK'><U>동시 여러 권한 부여 가능</U></SPAN>
- 동시 여러 객체 권한 부여 불가

```SQL
GRANT 권한 ON 테이블명 TO 유저;
```

### REVOKE

- <SPAN STYLE='COLOR:PINK'><U>동시 여러 권한 회수 가능</U></SPAN>
- 이미 회수된 권한 재회수 불가
- <SPAN STYLE='COLOR:PINK'><U>동시 여러 유저로부터 권한 회수 가능</U></SPAN>

```SQL
REVOKE 권한 ON 테이블명 FROM 유저;
```

### 롤(ROLE)

- 권한의 묶음(생성 가능한 객체)
- SYSTEM 계정에서 ROLE 생성 가능

```SQL
CREATE ROLE 롤이름;
```

### 권한부여 옵션(중간관리자의 권한)

1. WITH GRANT OPTION

- WITH GRANT OPTION으로 받은 <SPAN STYLE='COLOR:PINK'><U>오브젝트 권한을 다른 사용자에게 부여할 수 있음</U></SPAN>
- 중간관리자(WITH GRANT OPTION으로 권한을 부여받는 자)가 부여한 권한은 <SPAN STYLE='COLOR:PINK'><U>중간관리자만 회수 가능</U></SPAN>
- <SPAN STYLE='COLOR:PINK'><U>중간관리자에게 부여된 권한 회수 시 제 3자에게 부여된 권한도 함께 회수됨</U></SPAN>

2. WITH ADMIN OPTION

- WITH ADMIN OPTION을 통해 부여 받은 <SPAN STYLE='COLOR:PINK'><U>시스템 권한/롤 권한을 다른 사용자에게 부여할 수 있음</U></SPAN> -중간 관리자를 거치지 않고 <SPAN STYLE='COLOR:PINK'><U>직접 회수 가능</U></SPAN>
- <SPAN STYLE='COLOR:PINK'><U>중간관리자 권한 회수 시 제 3자에게 부여된 권한도 함께 회수X(남아있음)</U></SPAN>
