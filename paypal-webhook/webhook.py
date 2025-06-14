from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/paypal/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook PayPal actif (GET)", 200

    data = request.json
    with open("/tmp/paypal_log.txt", "a") as f:
        f.write(str(data) + "\n")
    print("Webhook PayPal (enseignant) reçu :", data)

    if data.get("event_type") == "PAYMENT.SALE.COMPLETED":
        print("✅ Paiement réussi !")

    return jsonify({'status': 'OK'}), 200
