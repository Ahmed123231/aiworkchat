
# AI Interview Assistant - Streamlit Application

This is a Streamlit-based application for conducting AI-powered job interviews, analyzing resumes, and providing feedback to candidates.

## Features

1. **User Authentication**
   - Sign up and login functionality
   - Session management

2. **Resume/CV Upload**
   - Upload and analysis of candidate resumes
   - Support for PDF, DOCX, and DOC formats

3. **AI Interview**
   - Simulated interview experience with an AI interviewer
   - Realistic question and answer interface
   - Video/audio controls simulation

4. **Results Analysis**
   - Comprehensive feedback on interview performance
   - Skill assessment with scores
   - Question-by-question feedback
   - Strengths and areas for improvement
   - Option to download and share results

## Setup Instructions

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

3. Access the application in your web browser at http://localhost:8501

## Application Structure

- `app.py` - Main Streamlit application with all functionality
- `requirements.txt` - Required Python packages

## Note

This is a demonstration application with simulated AI interview functionality. In a production environment, you would integrate with:

- A real AI model for processing resumes and conducting interviews
- A database for user management and storing interview results
- Secure authentication systems
- Cloud storage for resume files
