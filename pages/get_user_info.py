import streamlit as st

def render():
    st.title('정보를 입력해주세요')

    user_name = st.text_input('이름', value="")
    gender = st.selectbox('성별', ['남', '여'])
    height = st.number_input('키(cm 단위로 숫자만 입력해주세요)', min_value=0, value=165)
    weight = st.number_input('키(kg 단위로 숫자만 입력해주세요)', min_value=0, value=65)

    st.session_state.user_info['user_name'] = user_name
    st.session_state.user_info['gender'] = gender
    st.session_state.user_info['height'] = height
    st.session_state.user_info['weight'] = weight

    if st.button('다음', key='to_image_upload_option'):
        st.session_state.page = 'image_upload_option'
