# 🧠 시카고 마약 범죄 예측 프로젝트

> **멋쟁이사자처럼 데이터 분석 4기 파이널 프로젝트**  
> 시카고 범죄 데이터를 활용하여 마약 범죄 발생을 예측하고, 범죄 발생의 원인이 될 수 있는 요인을 분석하는 머신러닝 기반 프로젝트
>
> 진행 기간: 2025.03.24 ~ 2025.04.10 (18일)

---

## 📌 프로젝트 개요

공공의 안전을 위협하는 범죄에 대한 선제적 대응 필요성이 계속해서 높아지는 상황
<br /> 시카고에서 발생한 다양한 범죄 데이터를 기반으로, 시간대 및 발생 장소 등의 요인에 따라 분명한 발생 경향을 보이는 범죄 유형을 탐색하여
<br /> **범죄 발생의 패턴을 발견하고 머신러닝 기반 예측 모델을 구축함으로써 사회적 기여 가능성을 모색하고자 함**

---

## 🎯 목표

- 2001~2017년 시카고 범죄 데이터를 바탕으로 **마약 범죄 발생 예측 모델을 구축**  
- 공간·시간·장소 유형 등 다양한 요인이 **마약 범죄 발생과 어떤 관련이 있는지 검정 및 시각화**  
- **Streamlit 기반 대시보드 및 챗봇 UI 구현**을 통해 실제 활용 가능성 확보

---

## 📂 데이터 개요

- **출처**: [Chicago Police Department’s CLEAR (Citizen Law Enforcement Analysis and Reporting) System](https://www.kaggle.com/datasets/abhisheksinghblr/chicago-crime)
- **특징**
  - 2001년부터 2017년까지 시카고 시에서 발생한 범죄에 대한 요약 정보 데이터셋
  - 시카고 경찰청의 CLEAR 시스템(Citizen Law Enforcement Analysis and Reporting, 시민 법 집행 분석 및 보고 시스템)에서 수집되었으며, 범죄 발생 시공간 정보 및 발생 시간, 범죄 유형 등을 포함
#### 📑 주요 변수 목록

| 속성명                    | 설명                                        |
| ---------------------- | ----------------------------------------- |
| `ID`                   | 사건 기록의 고유 식별자                             |
| `Case Number`          | 시카고 경찰청 사건 번호                             |
| `Date`                 | 사건 발생 날짜 및 시간                             |
| `Block`                | 사건이 발생한 주소 (블록 단위)                        |
| `IUCR`                 | 일리노이 범죄 코드                                |
| `Primary Type`         | 주요 범죄 유형                                  |
| `Description`          | 세부 범죄 유형                                  |
| `Location Description` | 사건 발생 장소 설명                               |
| `Arrest`               | 체포 여부 (True/False)                        |
| `Domestic`             | 가정폭력 관련 여부 (True/False)                   |
| `Beat`                 | 사건 발생 경찰 비트 번호                            |
| `District`             | 사건 발생 경찰 구역 번호                            |
| `Ward`                 | 시의회 선거구 번호                                |
| `Community Area`       | 시카고 커뮤니티 지역 번호                            |
| `FBI Code`             | FBI 범죄 분류 코드                              |
| `X Coordinate`         | X 좌표 (Illinois State Plane 기준)            |
| `Y Coordinate`         | Y 좌표 (Illinois State Plane 기준) – 일부 결측 존재 |
| `Year`                 | 사건 발생 연도                                  |
| `Updated On`           | 기록이 마지막으로 갱신된 시점                          |
| `Latitude`             | 위도 (일부 조정된 위치, 결측값 존재 가능)                 |
| `Longitude`            | 경도 (일부 조정된 위치)                            |
| `Location`             | 위도와 경도가 함께 포함된 문자열 위치 정보 (`(위도, 경도)` 형식)  |

---

## 🛠 사용 기술

- **언어/환경**: Python, Jupyter Notebook  
- **데이터 처리**: pandas, numpy  
- **시각화**: matplotlib, seaborn, folium  
- **통계 분석**: scipy (카이제곱 검정, Cramér’s V)  
- **모델링**: scikit-learn (RandomForest, XGBoost, LightGBM), Voting (Ensemble)  
- **대시보드 구현**: Streamlit + LLaMA 기반 RAG 챗봇
- **문서화 및 협업**: GitHub, Notion, PowerPoint

---

## 🔍 분석 및 모델링 과정

### 1. EDA 및 전처리
- `Ward`, `Community Area` 등 결측치 약 70만 건 → `Block` 기준 최빈값 보간 + 위경도 기반 보정  
- 이상치 처리 (`Year` 오류 → 보정, 위경도 시카고 외 지역 → 제거)  
- 온전한 중복 데이터 약 170만 건 제거
- 범죄와 시간, 공간 등 다양한 요인과의 상관 관계 시각화

### 2. 통계 검정 및 인사이트 도출
- 요일, 시간대, 장소유형 등과 범죄 간 연관성 검정  
  - 요일과 마약 범죄: 마약 범죄는 요일에 따른 뚜렷한 경향성 없이 거의 고르게 발생 (p-value < 0.05, Cramér's V = 0.0354)
  - 범죄 발생 시간대와 범죄 유형: 연관성 미미 (p-value < 0.05, Cramér's V = 0.1295)
  - 범죄 발생 시간대와 체포율: 연관성 미미 (p-value < 0.05, Cramér's V = 0.0850)
  - 장소 유형과 마약 범죄: **주거지가 아닌 오픈된 외부 장소**에서 발생하는 경향 (p-value < 0.05)

### 3. 시각화

**(1) 마약 범죄는 요일에 따른 뚜렷한 경향성 없이 거의 고르게 발생**
![image](https://github.com/user-attachments/assets/d8afcb1c-bf0a-4dee-9bfa-ab71f17c803b)
- 카이제곱 검정 결과 p-value < 0.05
- 효과 크기(Cramér's V = 0.0354)는 매우 작음

<br /> **(2) 범죄 발생 시간대와 범죄 유형의 연관성은 미미**
![image](https://github.com/user-attachments/assets/6dd4226f-b4d4-4888-806d-eaa5b29c4e7b)
- 카이제곱 검정 결과 p-value < 0.05
- 효과 크기(Cramér's V = 0.1295)는 매우 작음

<br /> **(3) 범죄 발생 시간대와 체포율의 연관성은 미미**
![image](https://github.com/user-attachments/assets/39c91a26-15d1-47ac-8869-7001d3f84778)
- 카이제곱 검정 결과 p-value < 0.05
- 효과 크기(Cramér's V = 0.0850)는 매우 작음

<br /> **(4) 마약 범죄는 주로 주거지가 아닌 오픈된 외부 장소(Outdoor 카테고리의 장소)에서 발생**
![image](https://github.com/user-attachments/assets/67d3d924-abfd-4fc2-a659-c62117138d95)
- 카이제곱 검정 결과 p-value < 0.05
- 단일 변수의 분포 분석이기 때문에 변수 간 관계의 강도를 측정하지 않음

### 4. 머신러닝 모델링
- 주요 모델: RandomForest, XGBoost, LightGBM, Voting 기반 앙상블  
- **하이퍼파라미터 튜닝 (XGBoost 기준)**:
  - `max_depth`: 10  
  - `learning_rate`: 0.05  
  - `n_estimators`: 1000
- **성능 지표 (XGBoost 기준)**:
  - Accuracy: **0.93**
  - Precision: **0.70**
  - Recall: **0.71**
  - F1-score: **0.71**

### 5. 대시보드 및 챗봇 구현
- 범죄 유형/날짜 범위 기반 필터링, 월별/위치별 발생 추이 시각화 → Streamlit UI 구현  
- LLaMA 기반 RAG 챗봇과 연동하여 **사용자 질의응답 시스템 구축**

---

## 📈 성과

- **실제 적용 가능한 마약 범죄 예측 모델 확보** (F1-score 0.71)  
- 통계 검정과 머신러닝 분석을 병행하여, **해석 가능한 예측 모델 설계**
- 사용자 친화적 대시보드 + 챗봇 구축으로 **현업 적용성 증대**

---

## 🙌 팀원

- **김수현**: 시각화, 인사이트 도출 / 모델 구축 / 최종 팀 공통 코드 정리 및 취합 / 발표
- **박재홍**: 조장 / 시각화, 인사이트 도출 / 모델 구축 / LAG 시스템 및 Streamlit 기반 대시보드 구축
- **강상민**: 시각화, 인사이트 도출 / 모델 구축 / PPT 작성
- **김현태**: 시각화, 인사이트 도출 / 모델 구축

---

## 🗂 브랜치 & 파일 구조

| 브랜치     | 파일명                                         | 설명                    |
| ------- | ------------------------------------------- | --------------------- |
| `main`  | [README.md](https://github.com/Soohyun13/chicago-crime-project)                                 | 메인 프로젝트 설명 문서         |
| `team1` | [README.md](https://github.com/Soohyun13/chicago-crime-project/tree/team1/1%ED%8C%80)                                 | 동일한 설명 문서 (팀1 작업 브랜치) |
| `team1` | [공통/Final_pj_1팀_통합_코드.ipynb](https://github.com/Soohyun13/chicago-crime-project/blob/team1/1%ED%8C%80/%EA%B3%B5%ED%86%B5/Final_pj_1%E1%84%90%E1%85%B5%E1%86%B7_%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B8_%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3.ipynb)                | 전체 분석 워크플로우 종합본       |
| `team1` | [공통/Final_pj_1팀_머신러닝.ipynb](https://github.com/Soohyun13/chicago-crime-project/blob/team1/1%ED%8C%80/%EA%B3%B5%ED%86%B5/Final_pj_1%E1%84%90%E1%85%B5%E1%86%B7_%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC.ipynb)                 | 예측 모델링 및 성능 평가        |
| `team1` | [공통/Final_pj_1팀_시각화_및_가설_입증.ipynb](https://github.com/Soohyun13/chicago-crime-project/blob/team1/1%ED%8C%80/%EA%B3%B5%ED%86%B5/Final_pj_1%E1%84%90%E1%85%B5%E1%86%B7_%E1%84%89%E1%85%B5%E1%84%80%E1%85%A1%E1%86%A8%E1%84%92%E1%85%AA_%E1%84%86%E1%85%B5%E1%86%BE_%E1%84%80%E1%85%A1%E1%84%89%E1%85%A5%E1%86%AF_%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%8C%E1%85%B3%E1%86%BC.ipynb)          | 통계 분석 및 시각화           |
| `team1` | [김수현/final_pj_김수현_전처리부터_머신러닝까지_개인_코드.ipynb](https://github.com/Soohyun13/chicago-crime-project/blob/team1/1%ED%8C%80/%EA%B9%80%EC%88%98%ED%98%84/final_pj_%EA%B9%80%EC%88%98%ED%98%84_%EC%A0%84%EC%B2%98%EB%A6%AC%EB%B6%80%ED%84%B0_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EA%B9%8C%EC%A7%80_%EA%B0%9C%EC%9D%B8_%EC%BD%94%EB%93%9C.ipynb) | 개인 분석 및 모델링 작업 파일     |
