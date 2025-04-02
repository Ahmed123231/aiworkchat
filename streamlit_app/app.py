
import streamlit as st
import time
import os
from pathlib import Path
import sys

# Add the project root directory to the Python path
root_dir = Path(__file__).parent.absolute()
sys.path.append(str(root_dir))

# Import modules from our project structure
from utils.auth import login, register, logout
from utils.session import init_session_state

# Configure the page
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open(os.path.join(root_dir, "styles", "style.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
init_session_state()

# Main application
def main():
    load_css()
    
    # Simple navigation based on session state
    if st.session_state.user is None and st.session_state.page not in ["login", "signup"]:
        st.session_state.page = "login"
    
    # Show sidebar navigation for logged-in users
    if st.session_state.user is not None:
        with st.sidebar:
            st.markdown("## Navigation")
            if st.button("Dashboard", key="nav_dashboard"):
                st.session_state.page = "dashboard"
            if st.button("Upload CV", key="nav_upload"):
                st.session_state.page = "upload_cv"
            if st.button("Interview", key="nav_interview"):
                st.session_state.page = "interview"
            if st.button("Results", key="nav_results"):
                st.session_state.page = "results"
            
            st.markdown("---")
            if st.button("Sign Out", key="nav_logout"):
                logout()
                st.rerun()
    
    # Render the appropriate page based on session state
    if st.session_state.page == "login":
        from pages.login import render_login_page
        render_login_page()
    elif st.session_state.page == "signup":
        from pages.signup import render_signup_page
        render_signup_page()
    elif st.session_state.page == "dashboard":
        from pages.dashboard import render_dashboard
        render_dashboard()
    elif st.session_state.page == "upload_cv":
        from pages.upload_cv import render_upload_cv
        render_upload_cv()
    elif st.session_state.page == "interview":
        from pages.interview import render_interview
        render_interview()
    elif st.session_state.page == "results":
        from pages.results import render_results
        render_results()

if __name__ == "__main__":
    main()
