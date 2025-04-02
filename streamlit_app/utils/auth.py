
import streamlit as st
import json
import os
import re
from pathlib import Path
import time

# Path to user data file
DATA_DIR = Path(__file__).parent.parent / "data"
USER_DATA_FILE = DATA_DIR / "user_data.json"

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)

def _load_users():
    """Load user data from JSON file"""
    if not USER_DATA_FILE.exists():
        return {}
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def _save_users(users):
    """Save user data to JSON file"""
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def login(email, password):
    """Login a user and return success status"""
    users = _load_users()
    
    # Check if credentials are valid
    if email in users and users[email]["password"] == password:
        st.session_state.user = {
            "email": email,
            "name": users[email]["name"]
        }
        st.session_state.page = "dashboard"
        return True
    return False

def register(name, email, password, password_confirm):
    """Register a new user and return (success, message)"""
    if not name or not email or not password:
        return False, "All fields are required"
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Please enter a valid email address"
    
    if password != password_confirm:
        return False, "Passwords do not match"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    # Check if user already exists
    users = _load_users()
    if email in users:
        return False, "Email already registered"
    
    # Register new user
    users[email] = {
        "name": name,
        "password": password,
        "created_at": time.time()
    }
    _save_users(users)
    
    # Set session state
    st.session_state.user = {
        "email": email,
        "name": name
    }
    st.session_state.page = "dashboard"
    return True, "Registration successful"

def logout():
    """Logout the current user"""
    st.session_state.user = None
    st.session_state.page = "login"
