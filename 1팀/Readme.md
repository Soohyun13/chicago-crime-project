# 🧠 시카고 마약 범죄 예측 및 영향 요인 분석

> **멋쟁이사자처럼 데이터 분석 4기 파이널 프로젝트**  
> 시카고 범죄 데이터를 활용하여 마약 범죄 발생을 예측하고, 공간적/사회적 요인을 분석하는 머신러닝 기반 프로젝트

---

## 📌 프로젝트 개요

본 프로젝트는 시카고에서 발생한 다양한 범죄 중 **마약 범죄(Drug-related Crime)**를 중심으로 발생 요인을 분석하고,  
머신러닝 기반 예측 모델을 구축하여 **범죄 위험 예측과 공간 기반 대응 전략 수립**에 기여하고자 합니다.

---

## 🎯 목표

- 2001~2017년 시카고 범죄 데이터를 바탕으로 **마약 범죄 발생 예측 모델을 구축**  
- 공간·시간·장소 유형 등 다양한 요인이 **마약 범죄 발생과 어떤 관련이 있는지 검정 및 시각화**  
- **Streamlit 기반 대시보드 및 챗봇 UI 구현**을 통해 실제 활용 가능성 확보

---

## 📂 데이터 개요

- **출처**: Chicago Police Department’s CLEAR (Citizen Law Enforcement Analysis and Reporting) System  
- **범위**: 2001년 ~ 2017년 범죄 발생 정보 약 7백만 건  
- **주요 컬럼**:  
  - `Primary Type`, `Description` (범죄 유형 및 상세)  
  - `Date`, `Year` (범죄 발생 시점)  
  - `District`, `Community Area`, `Ward`, `Block`, `Latitude`, `Longitude` (공간 정보)  
  - `Arrest`, `Domestic` (체포 여부, 가정폭력 여부)  

---

## 🛠 사용 기술

- **언어/환경**: Python, Jupyter Notebook  
- **데이터 처리**: pandas, numpy  
- **시각화**: matplotlib, seaborn, folium  
- **통계 분석**: scipy (카이제곱 검정, Cramér’s V)  
- **모델링**: scikit-learn (RandomForest, XGBoost, LightGBM), Voting (Ensemble)  
- **대시보드 구현**: Streamlit + LLaMA 기반 RAG 챗봇

---

## 🔍 분석 및 모델링 과정

### 1. 데이터 전처리
- `Ward`, `Community Area` 등 결측치 약 70만 건 → `Block` 기준 최빈값 보간 + 위경도 기반 보정  
- 이상치 처리 (`Year` 오류 → 보정, 위경도 서울 외 지역 → 제거)  
- 중복 데이터 약 170만 건 제거

### 2. 통계 분석
- 요일, 시간대, 장소유형 등과 마약 범죄 간 연관성 검정 (카이제곱 + Cramér’s V)  
- 장소유형 중에서는 **Street, Sidewalk 등 외부공간에서 마약 범죄가 집중**됨 확인

### 3. 머신러닝 모델링
- 주요 모델: RandomForest, XGBoost, LightGBM → Voting 기반 앙상블  
- **하이퍼파라미터 튜닝 (XGBoost 기준)**:
  - `max_depth`: 10  
  - `learning_rate`: 0.05  
  - `n_estimators`: 1000
- **성능 지표 (XGBoost 기준)**:
  - Accuracy: **0.93**
  - Precision: **0.70**
  - Recall: **0.71**
  - F1-score: **0.71**

### 4. 대시보드 및 챗봇 구현
- 날짜/범죄유형/지도 기반 필터링 → Streamlit UI 구현  
- LLaMA 기반 RAG 챗봇과 연동하여 **사용자 질의응답 시스템 구축**

---

## 📈 성과

- **실제 적용 가능한 마약 범죄 예측 모델 확보** (F1-score 0.71)  
- 통계 검정과 머신러닝 분석을 병행하여, **해석 가능한 예측 모델 설계**
- 사용자 친화적 대시보드 + 챗봇 구축으로 **현업 적용성 증대**

---

## 🙌 팀원

- 김수현 외 3인

---

## 🗂 브랜치 & 파일 구조

```bash
📦 1팀 브랜치/
├── README.md                             # 프로젝트 설명 문서
│
├── 📁 공통/
│   ├── Final_pj_1팀_통합_코드.ipynb       # 전체 워크플로우 종합
│   ├── Final_pj_1팀_머신러닝.ipynb        # 예측 모델링 및 성능 평가
│   └── Final_pj_1팀_시각화_및_가설_입증.ipynb  # 통계 분석 및 시각화
│
└── 📁 김수현/
    └── final_pj_김수현_전처리부터_머신러닝까지_개인_코드.ipynb
