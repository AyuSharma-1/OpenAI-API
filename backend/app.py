from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI()

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