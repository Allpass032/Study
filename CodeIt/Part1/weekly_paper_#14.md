group by와 having 절의 공통
- 어떠한 열의 범주를 기준으로 이에 해당하는 행에 대해 요약하는 경우가 많은데 이 때 사용하는 구문이 group by와  having구문이다.

1. group by절
- group by 명령어의 경우 특정 컬럼을 기준으로 그룹화 할 수 있다
- 그룹화를 하면 조회된 데이터의 통계를 내기 위한 집계함수(count,avg,sum,max,min etc)를 사용하기에 용이
- group by절을 통해 그룹화한 열이 반드시 select 절 안에 포함되어 있어야 한다.
- ,를 사용하여 group by절의 기준에 두 가지 열을 사용할 수도 있음

2. having절
- group by절과 where 절을 함께 상요하면 쿼리 실행 순서에 따라 원하는 결과가 안 나올 수 있음. 그럴 경우 대신 group by 절을 사용할 때에는 having 절을 뒤에 작성해 조건문을 만들어 주면 됨
- 차이?라기엔 having절은 반드시 group by와 함께 사용되며, group by에 조건을 줄 때 where이 아닌 having만 사용 가능

-? 그렇다면 select from where group by 인데 순서의 차이인가?

데이터 베이스에서 null값이란 무엇이고 이를 처리하는 mysql함수는?
- 위키 백과의 정의 : 'Null 또는 NULL은 구조적 질의언어(SQL)에서 데이터베이스 내의 데이터 값이 존재하지 않는다는 것을 지시하는 데 사용되는 특별한 표시어(special marker)이다'
- 즉, 데이터가 존재하지 않는다는 것 & 알 수 없는 값

- 검색에서의 null : 조건절에 IS NULL이나 IS NOT NULL 이외의 조건절은 잘못된 조건절이다. 여기서 주의하지 말아야 할 것은 IS NULL구문을 쓰면 인덱스가 사용불가인 거지 잘못된 경우가 아니다.
- 함수에서의 NULL : NVL, NVL2는 오라클에서 대표적인 NULL 관련 함수이다. 해당 컬럼의 값이 NULL이면 특정 값으로 치환해야 하는 경우
- nvl(컬럼, null이면 치환할 값)
- nvl2(컬럼, null이 아니면 치환할 값, null이면 치환할 값)

- ? ifull vs mvl의 차이?

- https://limkydev.tistory.com/146
- https://khdscor.tistory.com/53
