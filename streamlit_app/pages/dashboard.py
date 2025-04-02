
import streamlit as st
from utils.session import navigate_to

def render_dashboard():
    st.markdown(f"<h1 class='page-title'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"<p>Welcome, {st.session_state.user['name']}!</p>", unsafe_allow_html=True)
    
    # Create a 3-column layout for the dashboard cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Upload CV")
        st.markdown("Upload your resume for AI analysis before the interview")
        if st.button("Upload CV", key="goto_upload"):
            navigate_to("upload_cv")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Start Interview")
        st.markdown("Begin your AI-powered interview session")
        if st.button("Start Interview", key="goto_interview"):
            navigate_to("interview")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Interview Results")
        st.markdown("View feedback and results from your previous interviews")
        if st.button("View Results", key="goto_results"):
            if st.session_state.interview_completed:
                navigate_to("results")
                st.rerun()
            else:
                st.warning("You need to complete an interview first")
        st.markdown("</div>", unsafe_allow_html=True)
