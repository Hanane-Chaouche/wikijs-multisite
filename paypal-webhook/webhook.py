from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/paypal/webhook', methods=['POST'])
def webhook():
    data = request.json
    with open("/tmp/paypal_log.txt", "a") as f:
        f.write(str(data) + "\n")
    print("Webhook PayPal (enseignant) reçu :", data)
    if data.get("event_type") == "PAYMENT.SALE.COMPLETED":
        print("Paiement réussi ")
    return jsonify({'status': 'OK'}), 200
