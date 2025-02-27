from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a fire alarm technician assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message.content

        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
