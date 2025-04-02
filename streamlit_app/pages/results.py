
import streamlit as st
from utils.session import navigate_to

def render_results():
    st.markdown("<h1 class='page-title'>Interview Results</h1>", unsafe_allow_html=True)
    
    if not st.session_state.interview_completed:
        st.warning("You haven't completed an interview yet. Please complete an interview to see results.")
        if st.button("Go to Interview"):
            navigate_to("interview")
            st.rerun()
        return
    
    results = st.session_state.interview_results
    
    # Overall score card
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Overall Assessment")
    
    score = results["overall_score"]
    score_class = "score-good" if score >= 80 else "score-medium" if score >= 60 else "score-bad"
    
    st.markdown(f"<div class='result-score {score_class}'>{score}/100</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Strengths")
        for strength in results["strengths"]:
            st.markdown(f"- {strength}")
    
    with col2:
        st.markdown("#### Areas for Improvement")
        for improvement in results["improvements"]:
            st.markdown(f"- {improvement}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Detailed question feedback
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Question-by-Question Feedback")
    
    for i, q_result in enumerate(results["question_scores"]):
        with st.expander(f"Question {i+1}: {q_result['question'][:50]}..."):
            st.markdown(f"**Your Answer:** {st.session_state.answers[i]}")
            st.markdown(f"**Score:** {q_result['score']}/100")
            st.markdown(f"**Feedback:** {q_result['feedback']}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Download report button (simulated)
    if st.download_button("Download Full Report (PDF)", 
                          data="Sample report content",
                          file_name="interview_report.pdf",
                          mime="application/pdf"):
        st.success("Report downloaded successfully!")
    
    # Navigation
    if st.button("Back to Dashboard"):
        navigate_to("dashboard")
        st.rerun()
