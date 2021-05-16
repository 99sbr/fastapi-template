import pandas as pd
import streamlit as st
from streamlit import caching
caching.clear_cache()
from application.main.routers.question_classifier import classification_service

st.set_page_config(page_title='Demo App', page_icon='😎', layout='centered')


def display_app_header(main_txt, sub_txt, is_sidebar=False):
    """
    function to display major headers at user interface
    Parameters
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed
    is_sidebar: bool -> check if its side panel or major panel
    #054029
    """

    html_temp = f"""
    <div style = "background.color:#0066ff ; padding:15px">
    <h2 style = "color:white; text_align:center;"> {main_txt} </h2>
    <p style = "color:white; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html=True)
    else:
        st.markdown(html_temp, unsafe_allow_html=True)


def space_header():
    """
    function to create space using html
    Parameters
    ----------
    """
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Main panel title
display_app_header(main_txt='Demo App',
                   sub_txt='Test and demonstrate some api functionality ')

space_header()


with st.form(key='app'):
    question = st.text_input(label='Question')
    submit_button = st.form_submit_button(label='Classify')
    if submit_button:
        type_out = classification_service.classify(question)
        space_header()
        st.write(f' **Type:  {type_out}**')