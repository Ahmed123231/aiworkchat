
import streamlit as st
import time
from utils.interview import get_interview_questions, generate_interview_results
from utils.session import navigate_to

def start_interview():
    st.session_state.interview_in_progress = True
    st.session_state.current_question = 0
    st.session_state.answers = []
    
    # Generate questions based on CV analysis if available
    cv_analysis = st.session_state.get("cv_analysis", None)
    st.session_state.questions = get_interview_questions(cv_analysis)

def submit_answer(answer):
    if st.session_state.current_question < len(st.session_state.questions):
        st.session_state.answers.append(answer)
        
        # Move to next question or complete interview
        if st.session_state.current_question == len(st.session_state.questions) - 1:
            complete_interview()
        else:
            st.session_state.current_question += 1

def complete_interview():
    st.session_state.interview_completed = True
    st.session_state.interview_in_progress = False
    
    # Generate interview results
    results = generate_interview_results(
        st.session_state.questions, 
        st.session_state.answers
    )
    
    st.session_state.interview_results = results
    navigate_to("results")

def render_interview():
    st.markdown("<h1 class='page-title'>AI Interview</h1>", unsafe_allow_html=True)
    
    if not st.session_state.interview_in_progress:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Ready to start your interview?")
        st.markdown("""
        This AI interview will ask you a series of questions about your experience and skills.
        Answer as you would in a real interview. Your responses will be analyzed to provide feedback.
        
        Tips:
        - Speak clearly and confidently
        - Provide specific examples from your experience
        - Be honest and authentic
        - Structure your answers using the STAR method (Situation, Task, Action, Result)
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back to Dashboard"):
                navigate_to("dashboard")
                st.rerun()
        with col2:
            if st.button("Start Interview Now"):
                start_interview()
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        # Show the interview interface
        st.markdown("<div class='interview-avatar'>🤖</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        current_q = st.session_state.current_question
        st.markdown(f"### Question {current_q + 1} of {len(st.session_state.questions)}")
        st.markdown(f"{st.session_state.questions[current_q]}")
        
        # Answer input
        answer = st.text_area("Your answer:", height=150, key=f"answer_{current_q}")
        
        # Recording simulation (just for UI effect)
        col1, col2 = st.columns([3, 1])
        with col1:
            if answer:
                if st.button("Submit Answer"):
                    with st.spinner('Processing your answer...'):
                        time.sleep(1)  # Simulate processing
                        submit_answer(answer)
                        st.rerun()
        with col2:
            st.markdown("<div class='pulse'>🎤 Listening...</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Show progress
        progress = (current_q + 1) / len(st.session_state.questions)
        st.progress(progress)
        
        # Option to end interview early
        if st.button("End Interview Early"):
            if len(st.session_state.answers) > 0:  # Ensure at least one question was answered
                complete_interview()
                st.rerun()
            else:
                st.error("Please answer at least one question before ending the interview")
