
import streamlit as st
import time
from utils.cv_processing import save_uploaded_cv, analyze_cv
from utils.session import navigate_to

def render_upload_cv():
    st.markdown("<h1 class='page-title'>Upload CV</h1>", unsafe_allow_html=True)
    st.markdown("<p>Upload your resume or CV for analysis before your interview</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose your CV file", type=["pdf", "docx", "doc"])
    
    upload_description = st.text_area("Tell us about the position you're applying for", 
                                    height=100,
                                    placeholder="e.g., Senior Software Engineer with 5 years of experience in Python...")
    
    if st.button("Upload and Analyze"):
        if uploaded_file is not None:
            with st.spinner('Analyzing your CV...'):
                # Save the uploaded file
                file_path = save_uploaded_cv(uploaded_file, st.session_state.user["email"])
                
                # Analyze the CV
                analysis = analyze_cv(file_path, upload_description)
                
                # Store in session state
                st.session_state.cv_analysis = analysis
                st.session_state.cv_uploaded = True
                
                st.success("CV uploaded and analyzed successfully!")
        else:
            st.error("Please upload a CV file")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Show a preview of the analysis if CV is uploaded
    if st.session_state.cv_uploaded and "cv_analysis" in st.session_state:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### CV Analysis Results")
        st.markdown("Here's what our AI found in your CV:")
        
        analysis = st.session_state.cv_analysis
        
        st.markdown("**Skills detected:**")
        for skill in analysis["skills"]:
            st.markdown(f"- {skill['name']} ({skill['years']} years)")
        
        st.markdown("**Education:**")
        for edu in analysis["education"]:
            st.markdown(f"- {edu['degree']} ({edu['year']})")
        
        st.markdown("**Recommendation:**")
        st.info(analysis["recommendation"])
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Dashboard"):
            navigate_to("dashboard")
            st.rerun()
    with col2:
        if st.button("Proceed to Interview"):
            navigate_to("interview")
            st.rerun()
