
import streamlit as st
import os
import time
import random
from PIL import Image
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if "user" not in st.session_state:
    st.session_state.user = None
if "cv_uploaded" not in st.session_state:
    st.session_state.cv_uploaded = False
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "interview_completed" not in st.session_state:
    st.session_state.interview_completed = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0

# Mock questions for the interview
mock_questions = [
    "Tell me about yourself and your background.",
    "What are your greatest strengths and how have you applied them in your work?",
    "Can you describe a challenging situation you faced at work and how you handled it?",
    "Why are you interested in this position?",
    "Where do you see yourself in 5 years?",
    "Do you have any questions for me about the role or company?"
]

# Mock skill scores for results page
skill_scores = {
    "Communication": 85,
    "Technical Knowledge": 92,
    "Problem Solving": 78,
    "Cultural Fit": 88,
    "Leadership": 72
}

# Mock feedback for results page
question_feedback = [
    {
        "question": "Tell me about yourself and your background.",
        "feedback": "Strong introduction with clear articulation of relevant experience. Could benefit from more concise delivery and focus on recent achievements."
    },
    {
        "question": "What are your greatest strengths and how have you applied them in your work?",
        "feedback": "Excellent examples provided that demonstrate both technical and soft skills. The connection between strengths and outcomes was well established."
    },
    {
        "question": "Can you describe a challenging situation you faced at work and how you handled it?",
        "feedback": "Good use of the STAR method to structure your response. Consider emphasizing the measurable results more clearly to showcase impact."
    },
    {
        "question": "Why are you interested in this position?",
        "feedback": "Demonstrated good research about the role and company. Could further highlight alignment between personal career goals and company mission."
    },
    {
        "question": "Where do you see yourself in 5 years?",
        "feedback": "Showed ambition while remaining realistic. Response could be strengthened by connecting long-term goals more explicitly to the current role."
    }
]

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #1E88E5;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #1E88E5;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .message-ai {
        background-color: #e3f2fd;
        padding: 0.8rem;
        border-radius: 0.5rem;
        margin-bottom: 0.8rem;
        display: inline-block;
        max-width: 80%;
    }
    .message-user {
        background-color: #bbdefb;
        padding: 0.8rem;
        border-radius: 0.5rem;
        margin-bottom: 0.8rem;
        display: inline-block;
        max-width: 80%;
        margin-left: auto;
        text-align: right;
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
    }
    .stProgress .st-bo {
        background-color: #1E88E5;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/conference-call--v1.png", width=100)
        st.title("AI Interview Assistant")
        
        if st.session_state.user:
            st.success(f"Logged in as {st.session_state.user}")
            if st.button("Logout"):
                st.session_state.user = None
                st.session_state.cv_uploaded = False
                st.session_state.interview_started = False
                st.session_state.interview_completed = False
                st.session_state.messages = []
                st.session_state.current_question_index = 0
                st.experimental_rerun()
        
        st.markdown("---")
        
        if st.session_state.user:
            menu = ["Dashboard", "Upload CV", "Interview", "Results"]
            choice = st.radio("Navigation", menu)
        else:
            menu = ["Login", "Sign Up"]
            choice = st.radio("Navigation", menu)
    
    # Main content based on navigation choice
    if choice == "Login":
        display_login_page()
    elif choice == "Sign Up":
        display_signup_page()
    elif choice == "Dashboard":
        display_dashboard()
    elif choice == "Upload CV":
        display_upload_cv()
    elif choice == "Interview":
        display_interview()
    elif choice == "Results":
        display_results()

def display_login_page():
    st.markdown('<p class="main-header">Sign In</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Welcome Back")
        st.markdown("Sign in to your account to continue with your interviews.")
        
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        
        col1_1, col1_2, col1_3 = st.columns([1, 1, 1])
        with col1_2:
            if st.button("Sign In"):
                if email and password:  # Simple validation
                    st.session_state.user = email.split('@')[0]  # Use username from email
                    st.success("Login successful!")
                    time.sleep(1)
                    st.experimental_rerun()
                else:
                    st.error("Please enter both email and password")
        
        st.markdown("Don't have an account? Navigate to Sign Up from the sidebar.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.image("https://img.icons8.com/color/480/000000/interviewer.png", width=300)

def display_signup_page():
    st.markdown('<p class="main-header">Create Account</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Join Our Platform")
        st.markdown("Create an account to get started with AI-powered interviews.")
        
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        col1_1, col1_2, col1_3 = st.columns([1, 1, 1])
        with col1_2:
            if st.button("Sign Up"):
                if name and email and password and confirm_password:
                    if password == confirm_password:
                        st.session_state.user = name
                        st.success("Account created successfully!")
                        time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.error("Passwords do not match")
                else:
                    st.error("Please fill in all fields")
        
        st.markdown("Already have an account? Navigate to Login from the sidebar.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.image("https://img.icons8.com/color/480/000000/add-user-male.png", width=300)

def display_dashboard():
    st.markdown(f'<p class="main-header">Dashboard</p>', unsafe_allow_html=True)
    st.markdown(f"### Welcome, {st.session_state.user}!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/color/96/000000/upload-to-cloud--v1.png", width=50)
        st.markdown("### Upload CV")
        st.markdown("Upload your resume for AI analysis before the interview.")
        if st.button("Upload CV", key="dashboard_upload"):
            st.session_state.cv_uploaded = False
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/color/96/000000/video-call--v1.png", width=50)
        st.markdown("### Start Interview")
        st.markdown("Begin your AI-powered interview session.")
        if st.button("Start Interview", key="dashboard_interview"):
            if st.session_state.cv_uploaded:
                st.session_state.interview_started = True
                st.experimental_rerun()
            else:
                st.error("Please upload your CV first")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/color/96/000000/check-all--v1.png", width=50)
        st.markdown("### Interview Results")
        st.markdown("View feedback and results from your previous interviews.")
        if st.button("View Results", key="dashboard_results"):
            if st.session_state.interview_completed:
                st.experimental_rerun()
            else:
                st.error("Complete an interview to see results")
        st.markdown('</div>', unsafe_allow_html=True)

def display_upload_cv():
    st.markdown('<p class="main-header">Upload Your CV</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    if not st.session_state.cv_uploaded:
        st.markdown("### Resume Upload")
        st.markdown("Upload your CV or resume so our AI can personalize your interview experience")
        
        uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "doc"])
        
        if uploaded_file is not None:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Process CV"):
                    with st.spinner("Uploading..."):
                        progress_bar = st.progress(0)
                        for percent_complete in range(0, 101, 10):
                            time.sleep(0.1)
                            progress_bar.progress(percent_complete)
                    
                    with st.spinner("Analyzing your resume..."):
                        time.sleep(2)
                    
                    st.success("CV uploaded and processed successfully!")
                    st.session_state.cv_uploaded = True
                    st.experimental_rerun()
    else:
        st.success("CV has been uploaded and processed!")
        st.image("https://img.icons8.com/color/96/000000/checked--v1.png", width=50)
        st.markdown("### Resume Analysis Complete")
        st.markdown("Your CV has been analyzed and is ready for the interview.")
        
        if st.button("Start Interview Now"):
            st.session_state.interview_started = True
            st.experimental_rerun()
        
        if st.button("Upload a Different CV"):
            st.session_state.cv_uploaded = False
            st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_interview():
    st.markdown('<p class="main-header">AI Interview Session</p>', unsafe_allow_html=True)
    
    # Check if CV has been uploaded
    if not st.session_state.cv_uploaded:
        st.warning("Please upload your CV before starting the interview")
        if st.button("Go to CV Upload"):
            st.experimental_rerun()
        return
    
    # Initialize interview
    if not st.session_state.interview_started or len(st.session_state.messages) == 0:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Ready for Your Interview?")
        st.markdown("You'll be interviewed by our AI assistant who will ask questions related to your experience and skills.")
        st.markdown("Make sure your camera and microphone are working properly before starting.")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Start Interview Session"):
                st.session_state.interview_started = True
                st.session_state.messages = []
                
                # Add initial greeting
                ai_message = "Hello! I'm your AI interviewer today. I'll be asking you a series of questions to learn more about your skills and experience. Are you ready to begin?"
                st.session_state.messages.append({"role": "ai", "content": ai_message})
                st.experimental_rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    # Display interview interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Display chat messages
        for message in st.session_state.messages:
            if message["role"] == "ai":
                st.markdown(f'<div class="message-ai">{message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="message-user">{message["content"]}</div>', unsafe_allow_html=True)
        
        # User input
        if st.session_state.current_question_index <= len(mock_questions) and not st.session_state.interview_completed:
            user_input = st.text_input("Your response:", key="user_input")
            
            col1_1, col1_2, col1_3 = st.columns([3, 1, 1])
            with col1_3:
                if st.button("Send") and user_input:
                    # Add user message
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    
                    # Add AI response if there are more questions
                    if st.session_state.current_question_index < len(mock_questions):
                        ai_message = mock_questions[st.session_state.current_question_index]
                        st.session_state.messages.append({"role": "ai", "content": ai_message})
                        st.session_state.current_question_index += 1
                    else:
                        # End of interview
                        ai_message = "Thank you for participating in this interview. We've now completed all the questions. I'll analyze your responses and provide feedback. You can view your results now."
                        st.session_state.messages.append({"role": "ai", "content": ai_message})
                        st.session_state.interview_completed = True
                    
                    st.experimental_rerun()
        
        # End interview button
        if st.session_state.interview_completed:
            if st.button("View Results"):
                st.experimental_rerun()
    
    with col2:
        # Camera/video preview
        st.markdown("### Camera Preview")
        st.image("https://img.icons8.com/color/96/000000/video-call--v1.png", width=100)
        st.markdown("(Camera access would be requested here)")
        
        # Audio controls
        st.markdown("### Audio Controls")
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            st.button("🎤 Mic")
        with col2_2:
            st.button("🔇 Mute")

def display_results():
    st.markdown('<p class="main-header">Interview Results</p>', unsafe_allow_html=True)
    
    if not st.session_state.interview_completed:
        st.warning("You need to complete an interview first")
        if st.button("Go to Interview"):
            st.experimental_rerun()
        return
    
    # Calculate overall score
    overall_score = sum(skill_scores.values()) // len(skill_scores)
    
    # Display overall performance
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Overall Performance")
        
        # Display score in a circle
        html_score = f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <div style="width: 150px; height: 150px; border-radius: 50%; background-color: #e3f2fd; 
                        display: flex; align-items: center; justify-content: center; 
                        border: 10px solid #1E88E5;">
                <span style="font-size: 2.5rem; font-weight: bold; color: #1E88E5;">{overall_score}%</span>
            </div>
        </div>
        """
        st.markdown(html_score, unsafe_allow_html=True)
        
        # Display rating text
        if overall_score >= 90:
            rating = "Excellent"
        elif overall_score >= 80:
            rating = "Very Good"
        elif overall_score >= 70:
            rating = "Good"
        elif overall_score >= 60:
            rating = "Satisfactory"
        else:
            rating = "Needs Improvement"
        
        st.markdown(f"<h3 style='text-align: center;'>{rating}</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Based on your responses and communication during the interview</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Skill Assessment")
        
        for skill, score in skill_scores.items():
            st.markdown(f"**{skill}**: {score}%")
            st.progress(score/100)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Question analysis
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Question Analysis")
    
    for i, feedback in enumerate(question_feedback):
        with st.expander(feedback["question"]):
            st.markdown(f"**Feedback**: {feedback['feedback']}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Summary and recommendations
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Summary & Recommendations")
    
    st.markdown("""
    You demonstrated strong communication skills and technical knowledge throughout the interview. 
    Your responses were generally well-structured and showcased relevant experience.
    
    **Strengths:**
    - Excellent articulation of technical concepts
    - Strong examples of past achievements
    - Good understanding of role requirements
    - Positive attitude and engagement
    
    **Areas for Improvement:**
    - Be more concise in responses to behavioral questions
    - Further highlight measurable impacts and outcomes
    - Provide more specific examples when discussing leadership experience
    
    Overall, your performance in this interview was strong. Continue focusing on highlighting 
    specific achievements with measurable results and consider practicing more concise delivery 
    for future interviews.
    """)
    
    # Action buttons
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        if st.button("Download Report"):
            st.info("In a real app, this would download a PDF of the interview results.")
    with col_b:
        if st.button("Share Results"):
            st.info("In a real app, this would open options to share the results.")
    with col_c:
        if st.button("New Interview"):
            st.session_state.interview_started = False
            st.session_state.interview_completed = False
            st.session_state.messages = []
            st.session_state.current_question_index = 0
            st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
