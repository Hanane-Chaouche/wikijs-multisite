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

@app.route('/paypal/logs', methods=['GET'])
def show_logs():
    if not os.path.exists(LOG_FILE):
        return "<h3>Aucune transaction enregistrée.</h3>", 200

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    html = """
    <h2>Transactions PayPal reçues :</h2>
    <ul>
    """
    for i, line in enumerate(lines, 1):
        try:
            data = json.loads(line)

            # Recherche des champs principaux (si dispo)
            amount = (data.get('resource', {}).get('amount', {}).get('value') or
                      data.get('resource', {}).get('gross_amount', {}).get('value') or
                      data.get('resource', {}).get('seller_receivable_breakdown', {}).get('gross_amount', {}).get('value') or
                      "N/A")
            currency = (data.get('resource', {}).get('amount', {}).get('currency_code') or
                        data.get('resource', {}).get('gross_amount', {}).get('currency_code') or
                        data.get('resource', {}).get('seller_receivable_breakdown', {}).get('gross_amount', {}).get('currency_code') or
                        "")
            email = (data.get('resource', {}).get('payer', {}).get('email_address') or
                     data.get('resource', {}).get('payee', {}).get('email_address') or
                     "N/A")
            status = (data.get('resource', {}).get('status') or data.get('event_type') or "N/A")
            date = (data.get('resource', {}).get('create_time') or data.get('create_time') or "N/A")

            # Résumé affiché dans <summary>
            summary = f"""<b>Transaction #{i}</b> |
                <b>Montant :</b> {amount} {currency} |
                <b>Email :</b> {email} |
                <b>Statut :</b> {status} |
                <b>Date :</b> {date}"""

            pretty_json = json.dumps(data, indent=2, ensure_ascii=False)
            html += f"<li><details><summary>{summary}</summary><pre>{pretty_json}</pre></details></li>"

        except Exception as e:
            html += f"<li><pre>{line.strip()}</pre></li>"

    html += "</ul>"
    return Response(html, mimetype='text/html')


    html += "</ul>"
    return Response(html, mimetype='text/html')
