from flask import Flask, request
app = Flask(__name__)

@app.route('/paypal/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook PayPal (enseignant) reçu :", data)
    if data.get("event_type") == "PAYMENT.SALE.COMPLETED":
        print("Paiement réussi ")
    return '', 200
