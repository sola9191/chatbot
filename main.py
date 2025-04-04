from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, render_template, request, jsonify

load_dotenv() # APIkey 불러옴
client = OpenAI() # 객체생성

app = Flask(__name__)

# Home screen
@app.route('/')
def home():
    return render_template("home.html")

# Chatting screen
@app.route('/chatbot')
def chatbot():
    return render_template("chat.html")

# Chatting API Endpoint 
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role" : "user",
                "content" : user_message
            }
        ]
    )
    response = completion.choices[0].message.content
    return jsonify({"response" : response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port =5000)
