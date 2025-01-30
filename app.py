from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configurar la API Key desde una variable de entorno
client = openai.OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "El mensaje está vacío"}), 400

    # Llamar a GPT-4 para generar una respuesta
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente de ventas experto en Shopify."},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
