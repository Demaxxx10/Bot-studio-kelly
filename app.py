
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = "Studio2025"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == verify_token:
            return challenge
        return "Token de verificação inválido.", 403
    return "Webhook funcionando!", 200

if __name__ == "__main__":
    app.run(port=5000)
