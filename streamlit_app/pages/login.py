
import streamlit as st
from utils.auth import login
from utils.session import navigate_to

def render_login_page():
    st.markdown("<h1 class='page-title'>AI Interview Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    
    st.markdown("<h2>Sign In</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Sign In", key="login_button"):
        if login(email, password):
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid email or password")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p>Don't have an account?</p>", unsafe_allow_html=True)
    
    if st.button("Create an Account", key="goto_signup"):
        navigate_to("signup")
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
