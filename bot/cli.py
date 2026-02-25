import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)

        order = place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=args.quantity,
            price=args.price
        )

        print("✅ Order Success")
        print(order)

    except Exception as e:
        print("❌ Order Failed:", e)

if __name__ == "__main__":
    main()