import streamlit as st
from utils import init_session_state, config
from pages import get_user_info
from pages import image_upload_option
from pages import image_upload
from pages import camera
from pages import model_process

init_session_state()
config()

# 페이지 이동 처리
if st.session_state.page == 'get_user_info':
    get_user_info.render()
elif st.session_state.page == 'image_upload_option':
    image_upload_option.render()
elif st.session_state.page == 'image_upload':
    image_upload.render()
elif st.session_state.page == 'camera':
    camera.render()
elif st.session_state.page == 'model_process':
    model_process.render()