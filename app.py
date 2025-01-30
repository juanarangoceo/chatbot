from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS para evitar bloqueos de origen cruzado
import openai
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir conexiones desde cualquier origen

# Configurar la API Key desde una variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "El mensaje está vacío"}), 400

    try:
        # Llamar a GPT-4 para generar una respuesta
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente de ventas experto en Shopify."},
                {"role": "user", "content": user_message}
            ]
        )
        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Usa el puerto que Render asigna
    app.run(host="0.0.0.0", port=port, debug=True)

