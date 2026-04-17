from flask import Flask, request
import requests

app = Flask(__name__)

# ===== CONFIG =====
BOT_TOKEN = "PASTE_YOUR_NEW_TOKEN"
CHAT_ID = "PASTE_YOUR_CHAT_ID"

BOT_ACTIVE = True

# ===== SEND TELEGRAM =====
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

# ===== TRADINGVIEW WEBHOOK =====
@app.route('/webhook', methods=['POST'])
def webhook():
    global BOT_ACTIVE

    if not BOT_ACTIVE:
        send_telegram("⛔ Bot paused. Signal ignored.")
        return {"status": "paused"}

    data = request.json

    action = data.get("action", "N/A")
    symbol = data.get("symbol", "XAUUSD")

    msg = f"""
📊 AUTO SIGNAL
Action: {action.upper()}
Symbol: {symbol}
"""

    send_telegram(msg)

    return {"status": "ok"}

# ===== TELEGRAM COMMANDS =====
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def telegram_commands():
    global BOT_ACTIVE

    data = request.json
    text = data["message"]["text"]

    if text == "/start":
        send_telegram("🤖 Bot is ONLINE")

    elif text == "/status":
        status = "ACTIVE ✅" if BOT_ACTIVE else "PAUSED ⛔"
        send_telegram(f"Status: {status}")

    elif text == "/pause":
        BOT_ACTIVE = False
        send_telegram("⛔ Bot paused")

    elif text == "/resume":
        BOT_ACTIVE = True
        send_telegram("✅ Bot resumed")

    elif text == "/buy":
        send_telegram("📈 Manual BUY command received")

    elif text == "/sell":
        send_telegram("📉 Manual SELL command received")

    elif text == "/close":
        send_telegram("❌ Close trades (not connected yet)")

    else:
        send_telegram("❓ Unknown command")

    return {"ok": True}

# ===== RUN =====
app.run(host="0.0.0.0", port=5000)
