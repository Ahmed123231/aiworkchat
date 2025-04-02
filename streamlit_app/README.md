
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

4. **Results Analysis**
   - Comprehensive feedback on interview performance
   - Skill assessment with scores
   - Question-by-question feedback
   - Strengths and areas for improvement
   - Option to download reports

## Project Structure

```
/streamlit_app/
    app.py              # Main application file
    requirements.txt    # Python dependencies
    README.md           # Documentation
    /assets/            # Images and other static files
    /pages/             # For multi-page Streamlit application
        login.py
        signup.py
        dashboard.py
        upload_cv.py
        interview.py
        results.py
    /utils/             # Utility functions and helpers
        auth.py
        session.py
        cv_processing.py
        interview.py
    /styles/            # Custom CSS styling
        style.css       # Custom CSS overrides
    /data/              # For storing data (if not using a database)
        user_data.json
```

## Setup Instructions

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit application:
   ```
   cd streamlit_app
   streamlit run app.py
   ```

3. Access the application in your web browser at http://localhost:8501

## Note

This is a demonstration application with simulated AI interview functionality. In a production environment, you would integrate with:

- A real AI model for processing resumes and conducting interviews
- A database for user management and storing interview results
- Secure authentication systems
- Cloud storage for resume files
