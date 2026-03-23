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

st.title("집합론")

st.header("교수")
st.write("장규환 (whan@inu.ac.kr)")

st.header("과목 소개")
st.write("""
집합론은 수학의 기초를 이루는 과목으로, 집합의 개념, 원소 관계, 함수, 관계, 그리고 수학적 논리의 원리를 학습합니다. 이 과목은 다른 수학 분야의 토대를 마련하며, 추상적 사고력을 기르는 데 중요합니다.
""")