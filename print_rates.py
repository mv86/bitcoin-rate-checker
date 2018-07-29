from datetime import datetime
from fetch_rates import current_gbp_rates


def fetch_current_rates():
    current_rates = current_gbp_rates()
    print_rates(current_rates)


def print_rates(rate_info):
    timestamp = datetime.now() 
    print(
    f'''\n
    *************************************************\n
        Rate at: {timestamp}\n
        Bitcoin.com:   £{rate_info[0]:_.2f}\n
        Coindesk.com:  £{rate_info[1]:_.2f}\n
        Average rate:  £{rate_info[2]:_.2f}\n
    *************************************************\n
    ''')


if __name__ == '__main__':
    fetch_current_rates()