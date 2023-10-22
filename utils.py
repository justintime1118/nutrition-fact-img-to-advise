import streamlit as st
import os

def init_session_state():
    if 'user_info' not in st.session_state:
        st.session_state.user_info = dict()

    if 'image' not in st.session_state:
        st.session_state.image = None

    if 'page' not in st.session_state:
        st.session_state.page = 'get_user_info'

def config():
    # bard api 토큰(cookie 값)
    os.environ['_BARD_API_KEY']= 'cQgX91wJYdtvGtIAgCLjHg8TBacL7yj1SPbznpvdXwP2Z08ou__gmbOdDdMBMwGWbnPt2Q.'