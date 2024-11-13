# ITS120L-Group-7
# Voluntario Chatbot

This is a Flask-based chatbot application named **Voluntario**, designed to answer questions about volunteering opportunities in the Philippines. The chatbot is powered by Gemini AI's generative model.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before installing the application, make sure you have the following installed:

1. **Python 3.7+** - You can download it from [python.org](https://www.python.org/downloads/).
2. **pip** - Python's package installer, included by default with Python installations.
3. **Git** (optional) - To clone the repository.

---


## Environment Variables
This application uses an environment variable to store the Gemini API key securely. Create a .env file in the root directory with the following content:
```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```
- Replace YOUR_GEMINI_API_KEY with your actual API key for Gemini AI.

To get a Gemini API key, you need to register and obtain an API key from Gemini AI’s platform.

---

## Running the Application
1. Run the Flask Application:
```
   python app.py
```
2. Access the Application: Open a web browser and go to http://127.0.0.1:5000 to view the homepage of the chatbot.
The application includes the following routes:

- Homepage - /: Displays the main interface for the chatbot.
- About Us - /AboutUs: Information about the chatbot’s purpose.
- Contact Us - /ContactUs: Contact details for support.
- Event List - /EventList: List of volunteering events.
- Log In - /LogIn: Log in page for users.
- Sign Up - /SignUp: Registration page for new users.
- Ask Route - /ask: Used to send user queries to the chatbot and get responses.

To ask questions, type your query in the input field, and the chatbot will respond with relevant information based on the model configuration.

---

## Troubleshooting
-Error: "No module named 'flask'":
  -Make sure you’re in the virtual environment and have installed all dependencies. Run pip install -r requirements.txt.
-Error: "Failed to fetch GEMINI_API_KEY":
  -Ensure the .env file is correctly set up in the root directory, and your environment has access to it. Restart the application if needed.
-API Errors:
  -If you encounter errors related to the Gemini API, verify your API key and ensure your network connection is stable.
