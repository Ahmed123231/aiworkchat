
import streamlit as st
from utils.auth import register
from utils.session import navigate_to

def render_signup_page():
    st.markdown("<h1 class='page-title'>AI Interview Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    
    st.markdown("<h2>Create an Account</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    name = st.text_input("Full Name", key="signup_name")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    password_confirm = st.text_input("Confirm Password", type="password", key="signup_password_confirm")
    
    if st.button("Sign Up", key="signup_button"):
        success, message = register(name, email, password, password_confirm)
        if success:
            st.success(message)
            st.rerun()
        else:
            st.error(message)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p>Already have an account?</p>", unsafe_allow_html=True)
    
    if st.button("Back to Login", key="goto_login"):
        navigate_to("login")
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
