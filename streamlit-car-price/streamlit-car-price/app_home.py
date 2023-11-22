import streamlit as st

def run_home_app():
    st.subheader('Welcom~!')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('고객 정보는 넣으면, 차 구매 금액도 예측해 줍니다.')

    st.text('AWS에 배포까지 된 앱입니다.')
    
    img_url = 'https://images.unsplash.com/photo-1489824904134-891ab64532f1?q=80&w=1031&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

    st.image(img_url)