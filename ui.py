import streamlit as st
from contentGenerationForm.queryGPT import query

# -- Set page config
apptitle = 'LinkedIn Post Generator'
st.set_page_config(page_title=apptitle, page_icon=":pencil:")

# Title the app
st.title('LinkedIn Post Generator')

with st.sidebar:
    # Model Form
    with st.form("Model Form"):
        st.text_input("Who do you want to be the model influencer: ")
        
        model_form_submitted = st.form_submit_button("Submit")
        if model_form_submitted:
            st.write("You submitted the form")

    # Content Generation Form
    with st.form("Content Generation Form"):
        st.write("Content Generation Form")
        temperature = st.slider(
            'temperature',
            min_value=0.0, 
            max_value=2.0, 
            value=1.0
        )
        max_tokens = st.slider(
            "How lon (tokens: 1 word ≈ 1.3 tokens) do you want your post be?",
            min_value=0,
            max_value=400,
            value=10
        )
        context = st.text_area(
            "Who are you? What do you do?",
            placeholder="I am a college student studying computer science, passionate about the software engineering and want to share my experience with everyone. "
        )
        content = st.text_area(
            "What do you want to talk about:"
        )

        # Every form must have a submit button.
        content_form_submitted = st.form_submit_button("Write")
        if content_form_submitted:
            st.write("You submitted the form")
        generated_content = query(temperature, max_tokens, context, content)

# Generated Post
st.markdown("---")
st.write("Generated Post:")

# specify which form submitted would trigger the query function
if content_form_submitted:
    st.write(generated_content)
    st.balloons()
else:
    st.write("No content generated yet")
st.markdown("---")