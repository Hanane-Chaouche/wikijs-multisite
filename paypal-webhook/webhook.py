from flask import Flask, request

app = Flask(__name__)

@app.route('/paypal/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(" Webhook PayPal reçu :", data)

    if data.get("event_type") == "PAYMENT.SALE.COMPLETED":
        print("Paiement confirmé !")
        # je peux ajouter ici des actions (ajouter utilisateur, envoyer un email, etc.)

    return '', 200

