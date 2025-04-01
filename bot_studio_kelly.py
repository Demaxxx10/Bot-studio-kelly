from flask import Flask, request
import requests

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "SEU_TOKEN_AQUI"
VERIFY_TOKEN = "studio_kelly_token"

def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v12.0/me/messages"
    headers = {"Content-Type": "application/json"}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
        "messaging_type": "RESPONSE"
    }
    params = {"access_token": PAGE_ACCESS_TOKEN}
    requests.post(url, headers=headers, params=params, json=payload)

@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Erro de verificação", 403

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    send_message(sender_id, "Olá, linda! Seja bem-vinda ao Studio Kelly Araújo.")
                    send_message(sender_id, "Nossa equipe já viu sua mensagem e logo vai te responder com todo carinho.")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
