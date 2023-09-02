import streamlit as st
from math import *

st.set_page_config(page_title='공동교육과정',
                   page_icon='🛠')

menu = st.sidebar.selectbox('MENU',['BMI 지수 계산기','원의 넓이 계산기','자유 낙하 높이 계산기'])

if menu == 'BMI 지수 계산기':
    st.subheader('BMI 지수 계산기')
    #몸무게 / 키의 제곱

    키 = st.number_input('키를 입력하세요(cm)',step=1)
    체중 = st.number_input('몸무게를 입력하세요(kg)', step=1)
    btn = st.button('계산하기')
    키 = 키/100
    if btn:
        bmi = round((체중 / (키 * 키)), 1)
        st.write('당신의 BMI 지수는 ',bmi,'입니다.')
    #과제 1 저체중, 정상, 과체중, 경도비만,중등도비만
        if bmi <= 18.5:
            st.write("저체중입니다.")
        elif bmi > 18.5 and bmi <= 23:
            st.write('정상입니다.')
        elif bmi > 23 and bmi <= 25:
            st.write('과체중입니다.')
        else:
            st.write('비만입니다.')

elif menu == '원의 넓이 계산기':
    st.subheader('원의 넓이 계산기')
    #과제 2 원 넓이 구하기
    #반지름^2 * 원주율
    r = st.number_input('반지름을 입력하세요(cm)',step=1)
    btn = st.button('계산하기')
    if btn:
        st.write("원의 넓이는 약", round(((r*r)*pi),3), "입니다.")


elif menu == '자유 낙하 높이 계산기':
    st.subheader('자유 낙하 하는 물체의 높이 계산기')
    #이동 거리 = 처음속도 * 시간 + 1/2(a*t^2) ---등가속도 공식
    t = st.number_input('물체가 떨어지는데 걸린 시간(s)을 입력하세요(단, 공기저항은 없다)',step=1)
    g = 9.8 #중력가속도
    btn = st.button('계산하기')
    if btn:
        st.write("물체가 떨어진 높이는 약 ",round(((g*(t*t))/2),2),"m 입니다.")