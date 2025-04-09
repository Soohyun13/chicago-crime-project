import streamlit as st
import contextlib #컨텍스트 관리 위한
import io #입출력 관리 위한
import os #환경 변수 관리 위한
import plotly.express as px

import pandas as pd #데이터 분석 라이브러리
from langchain_community.chat_models import ChatOllama #챗모델 모듈
from langchain_community.embeddings import OllamaEmbeddings #임베딩 모듈
from langchain_core.output_parsers import StrOutputParser #출력 파서 모듈
from langchain_core.prompts import ChatPromptTemplate #프롬프트 템플릿 모듈
from langchain_core.runnables import RunnablePassthrough #실행 가능한 파이썬 코드 모듈
from langchain_experimental.tools.python.tool import PythonAstREPLTool #파이썬 코드 실행 모듈

# Ollama 모델 설정
llm = ChatOllama(model="llama3.1:8b")
embeddings = OllamaEmbeddings(model="llama3.1:8b")

# 데이터 불러오기
df = pd.read_csv("rag_ready_data.csv", low_memory=False)
data = df.drop(columns='Arrest')
target = df['Arrest']

df_chicago = data
df_chicago['Arrest'] = target

# 변수명 저장
df_name = "df_chicago"
df_columns = ", ".join(df_chicago.columns)

# 시스템 프롬프트 작성
system_message = "당신은 타이타닉 데이터를 분석하는 데이터 분석가입니다.\n"
system_message += f"주어진 DataFrame에서 데이터를 출력하여 주어진 질문에 답할 수 있는 파이썬 코드를 작성하세요. {df_name} DataFrame에는 액세스할 수 있습니다.\n"
system_message += f"`{df_name}` DataFrame에는 다음과 같은 열이 있습니다: {df_columns}\n"
system_message += "각 열의 의미:\n"
system_message += "- Date: 사건이 발생한 날짜\n"
system_message += "- Block: 사건이 발생한 주소\n"
system_message += "- Primary Type: IUCR 코드의 주요 범죄 유형\n"
system_message += "- Description: IUCR 코드의 세부 범죄 유형\n"
system_message += "- Location Description: 사건이 발생한 장소의 설명\n"
system_message += "- Arrest: 체포 여부(True = 체포됨, False = 체포되지 않음)\n"
system_message += "- Beat: 사건이 발생한 경찰 순찰 구역\n"
system_message += "- District: 사건이 발생한 경찰서 관할 구역\n"
system_message += "- Community Area: 사건이 발생한 커뮤니티 지역\n"
system_message += "- Latitude: 사건이 발생한 위치의 위도\n"
system_message += "- Longitude: 사건이 발생한 위치의 경도\n"
system_message += "데이터는 이미 로드되어 있으므로 데이터 로드 코드를 생략해야 합니다."

message_with_data_info = [
    ("system", system_message),
    ("human", "{question}"),
]

# 프롬프트 템플릿 생성
prompt_with_data_info = ChatPromptTemplate.from_messages(message_with_data_info)

# 코드 생성 체인 구성
code_gen_chain = (
    {"question": RunnablePassthrough()}
    | prompt_with_data_info
    | llm
    | StrOutputParser()
)

# 코드 파서 함수 정의
def python_code_parser(input: str) -> str:
    processed_input = input.replace("```python", "```").strip()
    parsed_input_list = processed_input.split("```")
    
    if len(parsed_input_list) == 1:
        return processed_input
    
    parsed_code_list = []
    for i in range(1, len(parsed_input_list), 2):
        parsed_code_list.append(parsed_input_list[i])
    
    return "\n".join(parsed_code_list)

# 코드 파서 체인 구성
code_gen_chain_with_parser = (
    code_gen_chain
    | python_code_parser
)

# 코드 실행 함수 정의
def run_code(input_code: str):
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(input_code, {"df_chicago": df_chicago})
    except Exception as e:
        print(f"Error: {e}", file=output)
    return output.getvalue()

# 코드 실행 체인 구성
code_execute_chain = (
    code_gen_chain_with_parser |
    run_code
)

# 설명 체인 구성
analysis_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 시카고 범죄 데이터 분석 결과를 해석하고 설명하는 전문가입니다. 제공된 데이터 분석 결과를 바탕으로 사용자의 질문에 명확하게 답변해주세요."),
    ("human", "사용자 질문: {question}\n\n데이터 분석 결과: {analysis_result}")
])

explain_chain = (
    {"question": lambda x: x, "analysis_result": code_execute_chain}
    | analysis_prompt
    | llm
    | StrOutputParser()
)

# Streamlit 인터페이스 구성
st.set_page_config(page_title="시카고 범죄 RAG 분석가", layout="wide")
st.title("🏢 시카고 범죄 데이터")

tab1, tab2 = st.tabs(["❓ 질의응답", "📊 대시보드"])

with tab1:
    st.header("🔍 시카고 범죄 데이터 질문 답변기")
    user_question = st.text_input("❓ 궁금한 내용을 입력하세요:", "예) THEFT 유형의 범죄는 주로 어떤 장소에서 발생하나요?")

    if st.button("질문 실행"):
        with st.spinner("분석 중입니다..."):
            answer = explain_chain.invoke(user_question)
            st.subheader("💬 답변")
            st.write(answer)

            st.subheader("📊 원본 데이터 미리보기")
            st.dataframe(df_chicago.head(10))

with tab2:
    st.header("🔍 시카고 범죄 데이터 시각화 대시보드")

    # 범죄 유형 필터
    primary_types = df["Primary Type"].dropna().unique()
    selected_types = st.multiselect("👮‍♀️ 범죄 유형 선택", sorted(primary_types), default=sorted(primary_types)[:5])

    # Date 컬럼을 datetime으로 변환
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # 날짜 범위 필터
    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()

    start_date, end_date = st.date_input(
        "📅 날짜 범위 선택",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # 필터 적용
    filtered_df = df[
        (df["Primary Type"].isin(selected_types)) &
        (df["Date"] >= pd.to_datetime(start_date)) &
        (df["Date"] <= pd.to_datetime(end_date))
    ]

    st.success(f"🎯 필터링된 데이터 건수: {len(filtered_df):,}건")

    # 데이터 미리보기
    st.subheader("🔍 필터링된 데이터 미리보기")
    st.dataframe(filtered_df.head())

    # 범죄 유형 분포
    st.subheader("📊 선택된 범죄 유형별 발생 건수")
    type_counts = filtered_df["Primary Type"].value_counts().reset_index()
    type_counts.columns = ["Primary Type", "Count"]

    fig1 = px.bar(type_counts, x="Primary Type", y="Count", color="Primary Type", title="범죄 유형별 발생 건수")
    st.plotly_chart(fig1)

    # 월별 범죄 추이
    st.subheader("📈 월별 범죄 발생 추이")
    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M").astype(str)
    monthly_crime = filtered_df.groupby("Month").size().reset_index(name="Count")

    fig2 = px.line(monthly_crime, x="Month", y="Count", title="월별 범죄 발생 건수 추이")
    st.plotly_chart(fig2)

    # 지도 시각화
    st.subheader("🗺️ 범죄 발생 지도")
    map_df = filtered_df.dropna(subset=["Latitude", "Longitude"]).copy()

    # 1000개 샘플링
    if len(map_df) > 1000:
        map_df = df.sample(n=1000, random_state=0)

    fig3 = px.scatter_mapbox(
        map_df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Primary Type",
        hover_data=["Description", "Date", "Location Description"],
        color="Primary Type",
        zoom=10,
        height=500
    )
    
    fig3.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig3)


# 푸터
st.markdown("---")
st.caption("멋쟁이 사자처럼 데이터 분석 4기 박재홍")
