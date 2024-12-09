### 데이터 전처리의 개념:
데이터를 분석 및 처리에 적합한 형태로 만드는 과정

### 데이터 전처리 단계
데이터 수집 -> 데이터 정제 -> 데이터 축소 -> 데이터 변환

전처리 예시 :
중복값 제거, 결측치 보정, 데이터 연계/통합, 데이터 구조 변경(차원 변경), 데이터 벡터화 등

다뤄야하는 데이터는 보통 결측치(Missing Data)를 포함하고 있는 경우가 많은데 이를 처리하는 방법으로는 2가지가 존재    
1. 결측치가 있는 데이터를 제거하는 방식
2. 결측치를 어떤 값으로 대체하는 방식
if 결측치가 수치형 데이터인 경우 4가지  방식
  1. 특정 값을 지정 but 결측치가 많은 경우 모두 같은 값으로 대체한다면 데이터의 분산이 실제보다 작아지는 문제 발생
  2. 평균, 중앙값으로 대체, but 결측치 많은 경우 데이터의 분산이 실제보다 작아지는 문제
  3. 다른 데이터 이용해 예측값으로 대체
  4. 시계열 특성을 가진 데이터의 경우 앞뒤 데이터를 통해 결측치를 대체
  ex. 기온을 측정하는 센서 데이터에서 결측치가 발생할 경우, 전후 데이터 평균으로 보완

  ## t-test
정의 : 모집단의 분산이나 표준편차를 알지 못할 때 모집단을 대표하는 표본으로부터 추정된 분산이나 표준편차를 가지고 검정
![t 값(t-value)](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDVfMTA3/MDAxNTMzNDcxMjM4NjQ2.B6f20nL7PdZcRhjQ4qBSgFH1IRVcIyPqL3JFtJ2lmaAg.KFkhU_-c1gh1umHksNQtFFcPNlOz0inVR9ikG7JjViEg.JPEG.sendmethere/t%EA%B0%92-3.jpg?type=w800)

t값 : t값이란 t검정에 이용되는 검정통계량으로, 두 집단의 차이의 평균(X)을 표준오차(SE)로 나눈 값    
**즉, [표준오차]와 [표본평균사이의 차이]의 비율**

t분포(t-distribution):
평균이 0, 좌우 대칭을 이루며, 

+++
t분포 내용 및 그래프 추가 예정


참고 :
(https://velog.io/@gseung/F-09-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%B2%98%EB%A6%AC-%EA%B8%B0%EB%B2%95)

(https://m.blog.naver.com/sendmethere/221333164258)
