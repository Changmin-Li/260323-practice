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

st.title("미분방정식")

st.header("교수")
st.write("이동선 (esen@inu.ac.kr)")

st.header("과목 소개")
st.write("""
미분방정식은 함수의 변화율을 다루는 방정식의 해를 찾는 방법을 학습하는 과목입니다. 이 과목에서는 상미분 방정식과 편미분 방정식의 해석 방법, 해의 존재성과 유일성, 그리고 물리학, 공학 등 다양한 분야에서의 응용을 다룹니다.
""")