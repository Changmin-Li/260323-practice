import streamlit as st

st.markdown("""
<style>
@font-face {
    font-family: 'Nanum Gothic';
    src: url('/fonts/NanumGothic-Regular.ttf') format('truetype');
}
body {
    font-family: 'Nanum Gothic', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("2026학년도 1학기 인천대학교 사범대학 수학교육과 교과목 소개")

st.header("전공핵심")
st.page_link("pages/1_수학교과교육론.py", label="수학교과교육론")
st.page_link("pages/2_해석학.py", label="해석학")

st.header("전공심화")
st.page_link("pages/3_미분방정식.py", label="미분방정식")
st.page_link("pages/4_조합및그래프이론.py", label="조합및그래프이론")
st.page_link("pages/5_집합론.py", label="집합론")
