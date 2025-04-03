
# AI Interview Assistant

A Streamlit application that helps job seekers prepare for interviews by:
1. Uploading and analyzing their CV
2. Conducting mock AI interviews
3. Providing feedback and improvement suggestions

## Getting Started

### Prerequisites
- Python 3.7+
- pip or conda for package management

### Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/ai-interview-assistant.git
cd ai-interview-assistant
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
cd streamlit_app
streamlit run app.py
```

## Project Structure

```
/streamlit_app/
    app.py              # Main application file
    requirements.txt    # Python dependencies
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
        cv_processing.py
        interview.py
        session.py
    /styles/            # Custom CSS styling
        style.css
    /data/              # For storing user data
        user_data.json
```

## Features
- User authentication (signup/login)
- CV/resume upload and analysis
- Interactive AI interviews with feedback
- Comprehensive results and recommendations
- Clean and responsive UI

## Technologies Used
- Streamlit for the web application
- Python for backend processing
- Custom CSS for styling
