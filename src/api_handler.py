import requests

# Your real API access key
access_key = "60124ddd65dfceee49cfe3a15505d6c1"

def convert_currency(from_currency, to_currency, amount):
    """Convert currency using ExchangeRate.host with access key."""
    url = f"https://api.exchangerate.host/convert?access_key={access_key}&from={from_currency}&to={to_currency}&amount={amount}"
    try:
        response = requests.get(url)
        data = response.json()
        if "result" in data and data["result"] is not None:
            return round(data["result"], 2)
        else:
            return None
    except Exception as e:
        print(f"Error fetching conversion data: {e}")
        return None

def get_historical_rates(from_currency, to_currency, start_date, end_date):
    """Get historical exchange rates using ExchangeRate.host with access key."""
    url = f"https://api.exchangerate.host/timeseries?access_key={access_key}&start_date={start_date}&end_date={end_date}&base={from_currency}&symbols={to_currency}"
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
