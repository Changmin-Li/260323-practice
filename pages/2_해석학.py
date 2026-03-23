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

st.title("해석학")

st.header("교수")
st.write("윤영훈 (yeonghunyoun@inu.ac.kr)")

st.header("과목 소개")
st.write("""
해석학은 실수와 복소수의 해석적 성질을 다루는 수학의 기초 과목입니다. 이 과목에서는 미적분, 급수, 함수의 연속성과 미분가능성, 그리고 수학적 엄밀성을 강조하는 개념들을 학습합니다. 해석학은 수학의 다른 분야를 이해하는 데 필수적인 기반을 제공합니다.
""")