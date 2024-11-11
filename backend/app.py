from flask import Flask, request, render_template, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
print("API Key:", os.getenv("GEMINI_API_KEY"))

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Configure Gemini AI (Replace "YOUR_GEMINI_API_KEY" with your actual API key)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Replace this with your Gemini API key

# Set up the chatbot model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are Agape that will focus on assisting the users on their questions about volunteering in the Philippines...",
)

@app.route("/")
def home():
    return render_template("Homepage.html")  # Create an index.html template for the chatbot UI

@app.route("/AboutUs")
def AboutUs():
    return render_template("AboutUs.html")

@app.route("/ContactUs")
def ContactUs():
    return render_template("ContactUs.html")

@app.route("/EventList")
def EventList():
    return render_template("EventList.html")

@app.route("/LogIn")
def LogIn():
    return render_template("LogIn.html")

@app.route("/SignUp")
def SignUp():
    return render_template("SignUp.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form.get("question")
    print("Received question:", user_input)  # Log the question

    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)
        print("Response from model:", response.text)  # Log the model's response
        return jsonify(response=response.text)
    except Exception as e:
        print("Error:", e)
        return jsonify(response="Sorry, something went wrong."), 500


if __name__ == "__main__":
    app.run(debug=True)
