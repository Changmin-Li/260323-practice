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

st.title("조합및그래프이론")

st.header("교수")
st.write("하구용 (kyha@inu.ac.kr)")

st.header("과목 소개")
st.write("""
조합 및 그래프 이론은 이산 수학의 기초를 다루는 과목입니다. 이 과목에서는 조합론의 원리, 그래프의 구조와 성질, 연결성, 색칠 문제, 그리고 컴퓨터 과학과 응용 수학에서의 활용을 학습합니다.
""")