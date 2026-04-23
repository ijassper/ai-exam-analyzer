import streamlit as st
import pandas as pd
import time

# 1. 페이지 기본 설정
st.set_page_config(page_title="AI 시험지 분석 솔루션", page_icon="📝", layout="wide")

# ==========================================
# 🎨 2. 고급 CSS 스타일링 (EBS 느낌의 UI/UX)
# ==========================================
st.markdown("""
<style>
    /* 트렌디한 Pretendard 폰트 적용 */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');
    
    html, body,[class*="css"] {
        font-family: 'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }

    /* 메인 히어로 배너 (그라데이션 및 입체감) */
    .hero-banner {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    }
    .hero-banner h1 {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 1rem;
    }
    .hero-banner p {
        font-size: 1.2rem;
        color: #4b5563;
        font-weight: 500;
    }
    .badge {
        background-color: #3b82f6;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        display: inline-block;
        box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3);
    }

    /* 특징 소개 카드 디자인 */
    .feature-container {
        display: flex;
        justify-content: space-between;
        gap: 1.5rem;
        margin-bottom: 4rem;
    }
    .feature-card {
        background: white;
        flex: 1;
        padding: 2.5rem 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        text-align: center;
        border-top: 5px solid #3b82f6;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 0.8rem;
    }
    .feature-desc {
        color: #6b7280;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Streamlit 기본 버튼 커스텀 */
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        border: none;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(59, 130, 246, 0.4);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🎯 3. 메인 히어로 배너 (HTML)
# ==========================================
st.markdown("""
<div class="hero-banner">
    <div class="badge">VISION AI 기반 스마트 에듀테크</div>
    <h1>중·고등 시험지 자동 분석 솔루션</h1>
    <p>단 한 장의 사진으로 문항 분석부터 노션 DB 저장까지, 교육 업무의 디지털 전환을 경험하세요.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# ✨ 4. 기능 소개 카드 섹션 (HTML)
# ==========================================
st.markdown("""
<div class="feature-container">
    <div class="feature-card">
        <div class="feature-icon">⏱️</div>
        <div class="feature-title">업무 시간 90% 단축</div>
        <div class="feature-desc">수작업으로 하던 문항 분류 및 분석을 AI가 10초 만에 자동으로 완료합니다.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">강력한 AI 멀티모달</div>
        <div class="feature-desc">스마트폰으로 찍은 시험지 사진에서도 수학 수식, 표, 그래프를 완벽하게 인식합니다.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">노션 DB 자동화</div>
        <div class="feature-desc">분석된 데이터는 즉시 Notion DB에 저장되어 학원 관리자/강사들이 쉽게 공유합니다.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 🚀 5. 기능 시연부 (Streamlit 기본 기능)
# ==========================================
st.markdown("### 🚀 AI 분석 시연해보기")
st.info("💡 하단에 시험지 파일을 업로드하고 분석 버튼을 눌러보세요.")

uploaded_file = st.file_uploader("시험지 이미지나 PDF 파일을 업로드하세요", type=['png', 'jpg', 'pdf'])

if st.button("✨ AI 분석 시작하기"):
    if uploaded_file is not None:
        # 가짜 로딩 애니메이션
        with st.spinner("구글 Gemini AI가 이미지의 텍스트와 수식을 추출하고 있습니다..."):
            time.sleep(1.5)
        with st.spinner("교육과정 데이터베이스와 교차 검증하여 난이도와 단원을 분석 중입니다..."):
            time.sleep(1.5)
        
        st.success("✨ 분석이 성공적으로 완료되었습니다! (결과는 Notion DB에 자동 저장되었습니다)")
        
        st.markdown("---")
        st.markdown("### 📊 AI 분석 리포트")
        
        # 메트릭스 데이터 출력
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("분석 과목", "고1 수학(상)", "정확도 99%")
        col2.metric("총 문항 수", "20 문항", "객관식 15 / 주관식 5")
        col3.metric("예상 체감 난이도", "중상", "상위 20% 수준")
        col4.metric("오답률 1위 예상", "18번 문항", "도형의 방정식")
        
        st.write("<br>", unsafe_allow_html=True)
        
        chart_col, table_col = st.columns([1, 1.5])
        
        with chart_col:
            st.markdown("##### 📌 출제 단원 비중")
            chart_data = pd.DataFrame({
                "비중(%)":[35, 25, 20, 20]
            }, index=["다항식의 연산", "방정식과 부등식", "도형의 방정식", "나머지정리"])
            st.bar_chart(chart_data)
            
        with table_col:
            st.markdown("##### 📌 문항별 상세 분석표")
            table_data = pd.DataFrame({
                "문항 번호":["1번", "2번", "3번", "4번", "5번"],
                "출제 단원":["다항식", "방정식", "도형", "다항식", "부등식"],
                "난이도":["하", "중", "상", "중", "상"],
                "핵심 개념":["다항식의 덧셈", "이차방정식 근과 계수", "원의 방정식 접선", "조립제법", "연립이차부등식"]
            })
            st.dataframe(table_data, use_container_width=True, hide_index=True)

    else:
        st.warning("⚠️ 파일을 먼저 업로드해주세요!")
