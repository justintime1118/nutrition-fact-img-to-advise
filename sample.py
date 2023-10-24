import streamlit as st
import base64

file_ = open("/Users/jiyoo/ASAC_data_analysis_3rd/nutrition-fact-img-to-advise/resources/pikachu-excited.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

"""### 우오오오오!!!!!"""