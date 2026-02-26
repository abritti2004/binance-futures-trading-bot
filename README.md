 HEAD
# Binance Futures Trading Bot (Testnet)

## 📌 Overview
This project is a simplified Python trading bot for Binance Futures Testnet (USDT-M).

It supports:

- Market orders (BUY/SELL)
- Limit orders (BUY/SELL)
- CLI-based user input
- Proper logging and error handling
- Clean modular structure

---

## ⚙️ Setup Steps

1. Clone the repository
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Create a .env file and add:

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

---

## ▶️ How to Run

CLI:

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

---

## 📁 Project Structure

- client.py → Binance API wrapper  
- orders.py → order logic  
- validators.py → input validation  
- logging_config.py → logging setup  
- cli.py → CLI entry  

---

## 🧪 Test Evidence

Logs for MARKET and LIMIT orders are included in the logs folder.

# binance-futures-trading-bot
Modular Python trading bot for Binance Futures Testnet (USDT-M) with MARKET/LIMIT orders, CLI interface, logging, and robust error handling. 0a20b9be785eb12c1c31d14af5a0b0f037b463b2
