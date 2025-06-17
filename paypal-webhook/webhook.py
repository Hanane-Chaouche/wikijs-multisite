from flask import Flask, request, jsonify, Response
import json
import os

app = Flask(__name__)
LOG_FILE = "paypal_log.txt"

@app.route('/paypal/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook PayPal actif (GET)", 200

    data = request.json
    if data:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")
        print("Webhook PayPal (enseignant) reçu :", data)

        if data.get("event_type") == "PAYMENT.SALE.COMPLETED":
            print(" Paiement réussi !")

    return jsonify({'status': 'OK'}), 200

@app.route('/fr/paypal/logs', methods=['GET'])
def show_logs():
    if not os.path.exists(LOG_FILE):
        return "<h3>Aucune transaction enregistrée.</h3>", 200

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    html = "<h2>Transactions PayPal reçues :</h2><ul>"
    for line in lines:
        html += f"<li><pre>{line.strip()}</pre></li>"
    html += "</ul>"
    return Response(html, mimetype='text/html')
