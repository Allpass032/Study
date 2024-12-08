# p값 & 1종 오류와 2종 오류

## 내용에 앞서서    
- 통계는 기술통계와 추론통계로 구분되고 그 중 추론통계는 통계량을 사용하여 검정을 하는 것이다.
- 검정하고자 하는 주제가 곧 가설(Hypothesis)이다.

### 알고 있으면 좋은 정의 및 내용

---

#### 1. 가설, 독립변수, 종속변수

---

- 가설(Hypothesis) :  
    - 검정하고자 하는 주제
    - 연구문제에 대한 잠정적 결론
    - 둘 혹은 그 이상의 변수들 간의 관계에 대한 잠정적 결론

- 독립변수(Independent Variable) :  
  - 다른 변수에 영향을 받지 않는 변수 
  - 실험자가 직접 변경하는 변수 
  - 종속 변수에 영향을 주는 변수
  - 원인변수(Explanatory Variable), 예측변수(Predictor Variable)라고도 불림

- 종속변수(Dependant variable) : 
  - 종속적인 변수 
  - 독립변수에 영향을 받아서 변화하는 변수
  - 연구자가 마음대로 조정할 수 있는 변수
  - 반응변수(Response Variable), 결과(Outcome Variable)라고도 불림

+ 기타변수: 기타 여러 가지 원인으로 관찰 중인 변수    

> **즉, 독립(원인)변수로 인해서 어떤 종속(결과)변수가**    
**어떤 결과를 보이는지 보려고 한다.**

> (eg.) 예를 들면 오늘 날씨에 대한 기분을 조사하려고 한다면    
오늘 날씨가 독립변수, 기분이 종속변수가 된다.

<!-- #### 2. 데이터 분석에 있어 목적성에 대한 분류

  1. 기술적 분석(Descriptive Analytics):     
    - 과거나 현재에 어떤 일이 일어났는지를 파악하기 위한 분석.
    - 데이터의 분포, 추세 등을 분석하여 상황을 모니터링

  2. 진단적 분석(Diagnostic Analytics):    
    - 과거나 현재에 발생한 사건의 원인을 밝히기 위한 분석
    - 데이터 간의 관계를 분석하여 인과관계를 찾는다.
  
  3. 예측 분석(Predictive Analytics):    
    - 기계학습 모델 등을 사용하여, 미래에 어떤 일이 어느 정도의 확률로 일어날지를 예측한다.
    - 현재는 알 수 없는 결과의 가능성을 파악한다.
  
  4. 처방적 분석(Prescriptive Analytics):    
    - 예측되는 미래의 결과를 위해 어떻게 하면 좋을지 처방하기 위한 분석
    - 제한된 자원을 효과적으로 활용하여 최적의 성과를 낼 수 있도록 방향을 도출한다.

▲ 위 내용은 아직 완벽하게 이해 못 함(가트너 분석 단계 모델)

기본적인 데이터 확인 수준의 기술적 분석부터, 방향성까지 제시하는 처방적 분석이 있는 것을 알 수 있음 -->

<!-- > 기술적 분석을 재외하고는 모두 가설 설정이 필요함!
> 데이터 간의 인과관계를 밝히는 진단적 분석도 '변수 A와 변수 B는 관계가 있을/ 업을 것이다'라는 가설이 필요함
> 예측 분석과 처방적 분석도 어떤 요소의 변수가 발생할 일, 성과 등에 얼마만큼의 영향을 미칠 것이라는 가설을 설정하여 가설검정을 하는 프로세스로 데이터 분석이 진행됨 -->

---

#### 2. 통계적 가설 검정, 귀무가설, 대립가설

---

통계학 가설 검정의 궁극적인 목표:    
 기존의 주장이 옳은지 아니면 새로운 연구나 분석을 통한 주장이 맞는지를 검정하는 것!

>이를 위해 기존의 주장과 새로운 주장에 대한 두 가지 가설이 필요하게 되는데 여기서 **귀무가설, 대립가설**의 개념이 등장

귀무가설(Null hypothesis) :     
 - H<sub>0</sub>으로 표기    
 - 새로이 증명하고자 하는 가설과 반대되는 가설
 - 집단 간 차이가 없거나 변수의 영향력이 없는 상태를 의미    
 - 무죄 추정의 원칙과 같이 충분한 증거가 있기 전까지는    
  귀무가설이 옳은 것으로 가정    

대립가설(Alternative hypothesis) :    
 - H<sub>1</sub>으로 표기
 - 귀무가설이 기각되었을 때 대안적으로 채택되는 가설

## p-value(p값)

가설을 설정한 뒤에는 귀무가설을 기각하거나 채택하기 위한 기준인 유의수준을 설정    

유의수준(Significance level) :    
 + 귀무가설이 맞거나 틀린 것을 판단하기 위한 통계값    
 ▲ 즉, 1종 오류가 발생할 확률 의미
 + 일반적으로 0.1, 0.05, 0.01 등으로 설정함.    
 + 흔히 사용하는 기준은 0.05    
 ▲ 표본의 통계치가 귀무가설과 같이 확률이 5% 미만이라는 의미    
 + 공식적인 표기 방법은 앞의 0을 뺀 P > .05로 표기

## 가설 검정
* 모집단에 대한 가설이 통계적으로 옳은가를 판별하기 위한 방법    
* 모집단에서 표본을 추출하여 얻은 표본 통계량으로 모집단의 모수가     
귀무가설과 맞지 않고 연구가설에 합당한지 판단하기 위한 평가 방법
* 귀무가설을 기각하고 대립가설을 채택하는 절차    

**가설 검정의 절차**

![가설 검정 절차](https://post-phinf.pstatic.net/MjAyMTA2MDNfOTMg/MDAxNjIyNzI2NzI0OTYy.x22pt3LSOAg9aE1hnDEaXYMZh-RsPMBxfaK6MxTzKQsg.usxC2d9D7LHWiAVyNrspqygaXjB6LVSZuyMOuSh3zU0g.PNG/ADsP_008_1.png?type=w1200)

1. 검정하고자 하는 가설을 설정    

2. 유의수준을 설정한 뒤 통계 모델을 통해     

3. 실험을 수행    
▲ 집단 간의 평균 차이를 검정하기 위해서 t-test나 ANOVA를 사용    
▲ 종속변수에 대한 독립변수의 영향력을 검정하기 위해 회귀모델을 사용 (데이터 형태와 분석 목적에 따라 알맞은 모델을 설정)

4. 검정 통계량 산출    
▲ 위와 같은 통계적 검증을 통해 유의확률, 즉 p값(p-value)이 산출됐으면, 앞에서 설정한 유의수준을 통과하는지 확인한다.

5. 대립가설 기각/채택    
▲ 만약 유의수준을 0.05로 설정했다면, p값이 0.05보다 작을 때 귀무가설을 기각하고 대립가설을 채택     
▲ 만약 p값이 유의수준보다 높게 나왔다면, 귀무가설과 같은 결과가 나올 확률이 높다는 뜻이므로 대립가설을 채택불가    

## 1종 오류와 2종 오류

![1종 오류, 2종 오류](data:image/png;base64,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)
1종 오류:    
  - 귀무가설(H<sub>0</sub>)가 실제로는 참이어서 채택해야 함에도 불구하고 표본의 오차때문에 이를 채택하지 않는 오류
  - 1종 오류가 발생할 확률은 α (알파)로 표기하고 유의수준이라고 부른다.

2종 오류:
  - 귀무가설(H<sub>0</sub>)가 거짓이라서 채택하지 말아야 하는데 표본의 오차 때문에 이를 채택하는 오류
  - 보통 β (베타)로 표기한다. 
  - 가설검정의 검정력이 커질수록 줄어들게 된다.     
  ▲ 검정력이란 귀무가설이 거짓일 떄 귀무가설을 기각할 확률
  ▲ 차이가 있을 때 차이가 있다고 올바르게 판단할 확률

> α와 β값은 서로 트레이오프 관계    
즉 표본의 크기가 동일한 상태에서 α값을 감소시키면 상대적으로 β값이 증가하고 α값을 증가시키면 β값이 감소함    
일반적으로 α(유의수준)은 0.05, 1-β(검정력)은 0.2 기준을 사용

> 제 1종 오류와 제 2종 오류를 동시에 낮추는 것은 어렵지만    
**표본의 크기를 늘린다면** α를 유지하면서 β를 줄일 수 있음


<!-- 추가할 내용 및 외적 부분:    
1. 제일 중요한 건 역시 어디서 정보를 얻었는지
2. 어떻게 보기 좋게 만들 수 있을지 
3. 그래프 및 예시가 있으면 좋을 듯 -->