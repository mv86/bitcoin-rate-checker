import subprocess
import statistics
import requests


BITCOIN_URL = 'https://index.bitcoin.com/api/v0/price/GBP'

COINDESK_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def current_gbp_rates():
    """Fetch current bitcoin rates in GBP, calculate mean_avg and return as tuple.

       Tuple = (bitcoin.com rate, coindesk.com rate, mean average)
    """
    bitcoin_req = requests.get(BITCOIN_URL)
    coindesk_req = requests.get(COINDESK_URL)

    try:
        rate1 = _get_bitcoin_rate(bitcoin_req)
        rate2 = _get_coindesk_rate(coindesk_req)
        mean_avg = statistics.mean([rate1, rate2])
        bitcoin_rates = (rate1, rate2, mean_avg)
        return bitcoin_rates
    except Exception as exception:
        message = f"Exception while fetching bitcoin rates: {exception}!"
        subprocess.Popen(['notify-send', message])
        return None


def _get_bitcoin_rate(req):
    bitcoin_url_rate = req.json()['price']
    str_rate = str(bitcoin_url_rate)
    formatted_bitcoin_rate = f'{str_rate[:-2]}.{str_rate[-2:]}'
    bitcoin_rate = float(formatted_bitcoin_rate)
    return bitcoin_rate


def _get_coindesk_rate(req):
    coindesk_url_rate = req.json()['bpi']['GBP']['rate']
    formatted_coindesk_rate = coindesk_url_rate.replace(',', '')
    coindesk_rate = float(formatted_coindesk_rate)
    return coindesk_rate
