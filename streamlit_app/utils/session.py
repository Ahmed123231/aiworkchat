
import streamlit as st

def init_session_state():
    """Initialize all session state variables"""
    # User authentication
    if "user" not in st.session_state:
        st.session_state.user = None
    if "page" not in st.session_state:
        st.session_state.page = "login"
        
    # CV upload
    if "cv_uploaded" not in st.session_state:
        st.session_state.cv_uploaded = False
    
    # Interview
    if "interview_completed" not in st.session_state:
        st.session_state.interview_completed = False
    if "interview_in_progress" not in st.session_state:
        st.session_state.interview_in_progress = False
    if "interview_results" not in st.session_state:
        st.session_state.interview_results = None
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "answers" not in st.session_state:
        st.session_state.answers = []

def navigate_to(page):
    """Helper function to navigate between pages"""
    st.session_state.page = page
