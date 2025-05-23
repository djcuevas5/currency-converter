import requests

# Already have this one:
def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    try:
        response = requests.get(url)
        data = response.json()
        if "result" in data:
            return round(data["result"], 2)
        else:
            return None
    except Exception as e:
        print(f"Error fetching conversion data: {e}")
        return None

def get_historical_rates(from_currency, to_currency, start_date, end_date):
    url = f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&base={from_currency}&symbols={to_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if "rates" in data:
            return data["rates"]
        else:
            return None
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None
