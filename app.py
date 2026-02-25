import streamlit as st
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

st.title("📈 Binance Futures Testnet Bot")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0, value=0.001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=0.0, value=60000.0)

if st.button("Place Order"):
    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)

        order = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        st.success("✅ Order placed successfully")
        st.json(order)

    except Exception as e:
        st.error(f"❌ Order failed: {e}")