import streamlit as st
import pandas as pd
import time

# 1. 페이지 기본 설정
st.set_page_config(page_title="AI 시험지 분석 솔루션 (시연용)", page_icon="📝", layout="wide")

# 2. 헤더 및 소개 섹션
st.title("📝 AI 기반 중·고등 시험지 자동 분석 솔루션")
st.markdown("#### 학원/학교 강사들의 시험지 분석 업무를 획기적으로 줄여주는 AI 자동화 서비스입니다.")
st.info("💡 **본 페이지는 회사 경영진 시연을 위해 제작된 프로토타입(Mock-up)입니다.** 실제 개발 시 구글 Gemini AI와 Notion DB가 연동됩니다.")

st.write("---")

# 3. 서비스 장점 설명 (컬럼 활용)
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("⏱️ 업무 시간 단축")
    st.write("수작업으로 하던 시험지 문항 분석을 AI가 10초 만에 자동으로 완료합니다.")
with col2:
    st.subheader("🧠 강력한 AI 비전")
    st.write("스마트폰으로 찍은 시험지 사진에서도 수학 수식, 표, 그래프를 완벽하게 인식합니다.")
with col3:
    st.subheader("📊 DB 자동화")
    st.write("분석된 데이터는 즉시 Notion DB에 저장되어 원장님과 강사님들이 쉽게 관리할 수 있습니다.")

st.write("---")

# 4. 시연용 UI (파일 업로드 및 가짜 로딩)
st.subheader("🚀 시연해보기")
uploaded_file = st.file_uploader("시험지 이미지나 PDF 파일을 업로드해보세요 (시연용 더미 파일 업로드 가능)", type=['png', 'jpg', 'pdf'])

if st.button("🤖 AI 분석 시작", type="primary"):
    if uploaded_file is not None:
        # 가짜 로딩 애니메이션
        with st.spinner("구글 Gemini AI가 이미지의 텍스트와 수식을 추출하고 있습니다... (약 3초 소요)"):
            time.sleep(1.5)
        with st.spinner("교육과정 데이터베이스와 교차 검증하여 난이도와 단원을 분석 중입니다..."):
            time.sleep(1.5)
        
        st.success("✨ 분석이 성공적으로 완료되었습니다! (결과는 Notion DB에 자동 저장되었습니다)")
        
        # 5. 가짜 분석 결과 출력 (대시보드 형태)
        st.subheader("📊 분석 결과 리포트")
        
        # 핵심 지표
        m1, m2, m3, m4 = st.columns(4)
        m1.metric(label="분석 과목", value="고1 수학(상)")
        m2.metric(label="총 문항 수", value="20 문항")
        m3.metric(label="예상 체감 난이도", value="중상 (상위 20%)")
        m4.metric(label="오답률 1위 예상", value="18번 문항")
        
        st.write("<br>", unsafe_allow_html=True)
        
        # 차트 및 상세 표
        chart_col, table_col = st.columns([1, 1.5])
        
        with chart_col:
            st.markdown("**📌 출제 단원 비중**")
            # 가짜 차트 데이터
            chart_data = pd.DataFrame({
                "비중(%)": [35, 25, 20, 20]
            }, index=["다항식의 연산", "방정식과 부등식", "도형의 방정식", "나머지정리"])
            st.bar_chart(chart_data)
            
        with table_col:
            st.markdown("**📌 문항별 상세 분석표**")
            # 가짜 표 데이터
            table_data = pd.DataFrame({
                "문항 번호":["1번", "2번", "3번", "4번", "5번"],
                "출제 단원":["다항식", "방정식", "도형", "다항식", "부등식"],
                "난이도":["하", "중", "상", "중", "상"],
                "핵심 개념":["다항식의 덧셈", "이차방정식 근과 계수", "원의 방정식 접선", "조립제법", "연립이차부등식"]
            })
            st.dataframe(table_data, use_container_width=True, hide_index=True)

    else:
        st.warning("⚠️ 파일을 먼저 업로드해주세요!")
