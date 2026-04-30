from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load env
load_dotenv()


app = Flask(__name__)
CORS(app)

# Configure OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
    )

messages=[
    {"role": "system", "content": "You are a helpful assistant."}]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="google/gemma-4-31b-it:free",
            messages=messages
        )

        ai_reply = response.choices[0].message.content

        messages.append({"role": "assistant", "content": ai_reply})

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)