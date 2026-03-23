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
if st.button("수학교과교육론"):
    st.switch_page("pages/1_수학교과교육론.py")
if st.button("해석학"):
    st.switch_page("pages/2_해석학.py")

st.header("전공심화")
if st.button("미분방정식"):
    st.switch_page("pages/3_미분방정식.py")
if st.button("조합및그래프이론"):
    st.switch_page("pages/4_조합및그래프이론.py")
if st.button("집합론"):
    st.switch_page("pages/5_집합론.py")
