import streamlit as st

st.set_page_config(page_title="2026학년도 1학기 인천대학교 사범대학 수학교육과 교과목 소개", page_icon="📚", layout="wide")

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
st.write("수학교과교육론")
st.write("해석학")

st.header("전공심화")
st.write("미분방정식")
st.write("조합및그래프이론")
st.write("집합론")

st.write("각 교과목 페이지는 왼쪽 사이드바에서 선택할 수 있습니다.")
