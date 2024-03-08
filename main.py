import streamlit as st

## main streamlit layout page

# -- Set page config
apptitle = 'LinkedIn Post Generator'


st.set_page_config(page_title=apptitle, page_icon="")

# Title the app
st.title('LinkedIn Post Generator')

with st.sidebar:
    st.text_input("Choose you model influencer: ")
    st.selectbox("Select your ")
    st.slider("How long do you want your post be?")