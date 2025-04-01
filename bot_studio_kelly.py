
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "Studio2025"

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_token(token_sent)
    return "Webhook funcionando"

def verify_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Token inválido"

if __name__ == '__main__':
    app.run()
