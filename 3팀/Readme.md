# 🕵️‍♀️ 시카고 범죄 예측 프로젝트

>  시카고 범죄 데이터를 통해 언제, 어디서, 어떤 범죄가 발생했는지를 분석하고  
> 그 상황에서 **체포가 이루어질 가능성**을 예측해보는 AI 프로젝트입니다.


---


## 📌 프로젝트 개요

시카고는 미국 내에서 범죄 발생률이 높지만, 체포율은 약 25%로 매우 낮습니다.  
이에 따라, 저희는 **범죄 발생 당시의 시간, 장소, 유형 등의 정보를 활용하여 체포 가능성을 예측**해보는 프로젝트를 진행했습니다.

이를 통해 **어떤 조건에서 체포가 더 잘 이루어지는지 파악**하고,  
**경찰의 대응 전략을 효과적으로 설계하는 데 도움이 되는 모델**을 개발하는 것을 목표로 삼았습니다.


---

## 🗂️ 사용 데이터 출처

- [🔗 Chicago Crime Open Data (data.cityofchicago.org)](https://data.cityofchicago.org/)
- [🔗 Kaggle - Crimes in Chicago](https://www.kaggle.com/datasets/chicago/crime)

---

## 🛠️ 사용 기술 스택

| 분류       | 라이브러리 / 도구                             | 설명 |
|------------|-----------------------------------------------|------|
| 📦 데이터 처리 | `pandas`, `numpy`                            | 데이터 로딩, 전처리, 통계 분석 |
| 🌍 공간 분석 | `geopandas`, `shapely`, `folium`              | 공간 데이터 처리 및 지도 시각화 |
| 📊 시각화   | `matplotlib`, `folium`, `GeoJsonTooltip`      | 그래프 및 인터랙티브 지도 시각화 |
| 🧠 머신러닝 | `scikit-learn`, `RandomForestClassifier`      | 체포 여부 분류 예측 모델 |
| 🧪 평가     | `accuracy_score`, `classification_report`     | 모델 성능 평가 지표 |
| 🧰 기타     | `LabelEncoder`, `train_test_split`            | 범주형 처리 및 데이터 분할 |
| ☁️ 협업 및 실행 | `Google Colab`                             | 코드 실행 및 팀원 간 실시간 협업 |
---

## 🧹 전처리 요약

- 날짜 및 시간 형식 변환 (`MM/DD/YYYY` → `YYYY-MM-DD`)
- 결측치 제거 및 처리: `Location Description`, `Community Area` 등
- 주요 컬럼 정리: `Primary Type`, `Arrest`, `Community Area`, `Date`
- 범죄 유형 필터링: 상위 10개 유형 기준 분석
- 불필요 컬럼 제거: `Case Number`, `ID`, `FBI Code` 등
- `Community Area` 매핑을 위한 GeoJSON 정제 및 병합

---

## 🔍 주요 기능 및 분석 내용

- 📊 시간대별 / 요일별 범죄 발생 패턴 분석
- 🗺️ 지역별 범죄 유형 시각화 
- 🎯 체포 가능성 예측 모델 개발 (분류 모델)
- 📈 통계 기반 인사이트 도출 (카이제곱 검정, Cramér’s V 등)

---

---
## 📈 결과 요약

- ⏰ **시간대별 분석**  
  오후 시간대에 범죄 발생 비율이 상대적으로 높았으며,  
  **상업지구에서는 절도**, **외곽 주거지역에서는 폭력 범죄**가 중심적으로 발생했습니다.  
  → 이에 따라 **순찰 시간과 지역별 맞춤형 전략 수립의 필요성**이 도출되었습니다.

- 🔍 **체포율 분석**  
  범죄 유형에 따라 체포율의 격차가 뚜렷하게 나타났습니다.  
  - 단속 중심 범죄(매춘, 마약, 도박): 체포율 **99%**  
  - 피해자 중심 범죄(절도, 재산 손괴, 성범죄): 체포율 **5~15%**  
  → **범죄 특성에 따른 수사 전략의 차별화** 필요성이 확인되었습니다.

- 🤖 **머신러닝 모델 성능**  
  Random Forest 모델을 활용한 체포 여부 예측에서 **정확도 86~89%**를 달성했습니다.  
  → 이는 **자원의 효율적 분배**, **고위험 지역 선제 대응** 등 정책 설계에 활용 가능성이 있습니다.

---
📝 Google Slides 발표자료
---
## 👥 팀원 및 역할

본 프로젝트는 전 과정에 걸쳐 모든 팀원이 함께 협업하며 완성한 결과물입니다.  
특히 데이터 전처리, 머신러닝 모델링, 시각화, 발표자료 제작을 함께 수행했으며,  
아래는 각자의 주요 활동 중심 정리입니다:

| 이름 | 주요 활동 |
|:----:|:-----------|
| **조성준** | 머신러닝 모델 구현, 발표자료 발표 |
| **류진수** | 데이터 전처리 과정 전반 중심 기여 |
| **박선우** | 머신러닝 모델링, 시각화, 발표자료 정리, 추론 통계 분석 |
| **박효은** | 발표자료 구성, 지도 시각화, EDA 분석 중심 기여 |

<br>
<br>





## 참고 자료

</aside>

### **Boundaries - Community Areas (current)**

[Community Areas (current)](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6)

[Community Areas (github)](https://github.com/RandomFractals/ChicagoCrimes/blob/master/data/chicago-community-areas.geojson)

### **Boundaries - Wards (2003-2015)**

[Wards(2003-2015)](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Wards-2003-2015-/xt4z-bnwh)

### Boundaries - Wards (2023-)

[Wards(2023-)](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Wards-2023-/p293-wvbd/about_data)

### Community Area Name

[Community Area (github)](https://github.com/dssg/411-on-311/blob/master/data/chicago-community-areas.csv?utm_source=chatgpt.com)

### 범죄 유형 (강력범죄 분류 시 참고 자료)

[Chicago_Police_Department_-_Illinois_Uniform_Crime_Reporting__IUCR__Codes.pdf](attachment:45dd7bd5-95dc-48a3-acea-db33461438f1:Chicago_Police_Department_-_Illinois_Uniform_Crime_Reporting__IUCR__Codes.pdf)

https://data.cityofchicago.org/api/views/c7ck-438e/rows.pdf

https://data.cityofchicago.org/Public-Safety/Chicago-Police-Department-Illinois-Uniform-Crime-R/c7ck-438e/data_preview

[Chicago_Police_Department_-_Illinois_Uniform_Crime_Reporting__IUCR__Codes_20250327.csv](attachment:dcaa1088-a993-4100-b2cf-5339ba05de59:Chicago_Police_Department_-_Illinois_Uniform_Crime_Reporting__IUCR__Codes_20250327.csv)

### 통계청 자료(2008) (흉악범죄 분류 시 참고 자료)

[2008_11_3+증가하는+'흉악범죄'.pdf](attachment:b71bd4b6-b82e-4ba6-bf78-4b9829c92171:2008_11_3증가하는흉악범죄.pdf)

### 시카고 경찰서 위치

[CHICAGO Police Stations](https://data.cityofchicago.org/Public-Safety/Police-Stations/z8bn-74gv/about_data)

### 캐나다 Crime Severity Index (CSI)

[85-004-x2009001-eng.pdf](attachment:a630a130-9aff-4e80-9b6b-e58e6fd6924a:85-004-x2009001-eng.pdf)

### 영국 Cambridge Crime Harm Index (CCHI)

[The_Cambridge_Crime_Harm_Index_Measuring_Total_Har.pdf](attachment:15aea057-7974-442e-b21b-7e985cb662dd:The_Cambridge_Crime_Harm_Index_Measuring_Total_Har.pdf)

### 미국 연방 양형 지침 (US Sentencing Guidelines, USSG)

[GLMFull.pdf](attachment:92eb753c-6f3f-4407-bd94-9785fa68d2f6:GLMFull.pdf)