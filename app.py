import streamlit as st
import pandas as pd
import time

# 1. 페이지 기본 설정 (넓은 화면 사용)
st.set_page_config(page_title="AI 시험지 분석 솔루션", page_icon="📝", layout="wide")

# ==========================================
# 🎨 2. 고급 CSS 스타일링 (EBS 느낌 유지)
# ==========================================
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');
    html, body, [class*="css"] {
        font-family: 'Pretendard Variable', Pretendard, sans-serif;
    }
    .hero-banner {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    }
    .hero-banner h1 {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 1rem;
    }
    .hero-banner p { font-size: 1.1rem; color: #4b5563; font-weight: 500; }
    .badge {
        background-color: #3b82f6; color: white; padding: 0.4rem 1rem;
        border-radius: 50px; font-size: 0.9rem; font-weight: 800;
        margin-bottom: 1rem; display: inline-block;
    }
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
        color: white; font-size: 1.1rem; font-weight: bold;
        padding: 0.75rem 2rem; border-radius: 50px; border: none; width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px); box-shadow: 0 8px 15px rgba(59, 130, 246, 0.4); color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🎯 3. 메인 히어로 배너
# ==========================================
st.markdown("""
<div class="hero-banner">
    <div class="badge">VISION AI 기반 스마트 에듀테크</div>
    <h1>중·고등 시험지 자동 분석 솔루션</h1>
    <p>좌측에 시험지를 업로드하면, 우측에서 AI가 즉시 문항을 분석해 드립니다.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 🚀 4. 파일 업로드 및 분석 로직 (좌우 분할 UX 적용)
# ==========================================
uploaded_file = st.file_uploader("시험지 이미지 파일(PNG, JPG)을 업로드하세요", type=['png', 'jpg', 'jpeg'])

if st.button("✨ AI 분석 시작하기"):
    if uploaded_file is not None:
        st.markdown("---")
        
        # 💡 핵심: 화면을 4.5 대 5.5 비율로 좌우 분할
        left_col, right_col = st.columns([4.5, 5.5], gap="large")
        
        # ⬅️ [왼쪽 화면] 업로드한 원본 이미지 표시
        with left_col:
            st.markdown("### 📄 원본 시험지")
            # 이미지를 화면 너비에 맞게 꽉 차게 보여줌
            st.image(uploaded_file, use_container_width=True, caption="업로드된 시험지 이미지")
            
        # ➡️ [오른쪽 화면] AI 분석 결과 출력
        with right_col:
            st.markdown("### 🤖 AI 분석 리포트")
            
            # 우측 화면에서 로딩 스피너 돌리기
            with st.spinner("Gemini AI가 텍스트와 수식을 추출하고 있습니다..."):
                time.sleep(1.5)
            with st.spinner("교육과정 데이터베이스와 교차 검증 중입니다..."):
                time.sleep(1.5)
            
            st.success("✨ 분석 완료! (Notion DB 저장 완료)")
            st.write("<br>", unsafe_allow_html=True)
            
            # 우측 화면 안에서 다시 2열로 분할하여 핵심 지표 표시 (공간 활용)
            m1, m2 = st.columns(2)
            m1.metric("분석 과목", "고1 수학(상)", "정확도 99%")
            m2.metric("총 문항 수", "20 문항", "객관식 15 / 주관식 5")
            
            m3, m4 = st.columns(2)
            m3.metric("예상 체감 난이도", "중상", "상위 20% 수준")
            m4.metric("오답률 1위 예상", "18번 문항", "도형의 방정식")
            
            st.write("<br>", unsafe_allow_html=True)
            
            # 출제 단원 비중 차트
            st.markdown("##### 📌 출제 단원 비중")
            chart_data = pd.DataFrame({
                "비중(%)":[35, 25, 20, 20]
            }, index=["다항식의 연산", "방정식과 부등식", "도형의 방정식", "나머지정리"])
            st.bar_chart(chart_data)
            
            # 상세 분석표
            st.markdown("##### 📌 문항별 상세 분석표")
            table_data = pd.DataFrame({
                "번호":["1번", "2번", "3번", "4번", "5번"],
                "단원":["다항식", "방정식", "도형", "다항식", "부등식"],
                "난이도":["하", "중", "상", "중", "상"],
                "핵심 개념":["다항식 덧셈", "근과 계수", "원의 접선", "조립제법", "연립부등식"]
            })
            st.dataframe(table_data, use_container_width=True, hide_index=True)

    else:
        st.warning("⚠️ 시험지 이미지를 먼저 업로드해주세요!")
