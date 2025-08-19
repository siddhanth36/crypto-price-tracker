import requests
import argparse
from datetime import datetime

def get_crypto_price(coin_id='bitcoin', currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data[coin_id][currency]

def main():
    parser = argparse.ArgumentParser(description="Fetch real-time cryptocurrency prices.")
    parser.add_argument('--coin', type=str, default='bitcoin', help="Cryptocurrency ID (e.g., 'ethereum')")
    parser.add_argument('--currency', type=str, default='usd', help="Currency (e.g., 'eur', 'jpy')")
    args = parser.parse_args()

    price = get_crypto_price(args.coin, args.currency)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {args.coin.upper()}: {price} {args.currency.upper()}")

if __name__ == "__main__":
    main()
