from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, request, jsonify
import os

# Load environment variables
load_dotenv()

# DEBUG: check if key is loaded
print("API KEY:", os.getenv("OPEN_AI_SECRET_KEY"))

app = Flask(__name__)
CORS(app)

# Pass API key explicitly (IMPORTANT FIX)
client = OpenAI(api_key=os.getenv("OPEN_AI_SECRET_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
    )

    ai_reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": ai_reply})

    return jsonify({"reply": ai_reply})

if __name__ == '__main__':
    app.run(debug=True)