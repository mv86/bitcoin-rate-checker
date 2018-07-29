#!/TODO/insert/path/for/script
"""Script to scrape bitcoin price data and store in db."""
from fetch_rates import current_gbp_rates
from previous_rates import history_compare
import db.connect


def store_gbp_rates():
    """Fetch current bitcoin GBP rates, save to db & compare against rate history."""
    bitcoin_rates_gbp = current_gbp_rates()
    if bitcoin_rates_gbp:
        store_rates(bitcoin_rates_gbp)
        history_compare(bitcoin_rates_gbp)


def store_rates(rates):
    """Connect to db and store rates."""
    sql = '''INSERT INTO bitcoin_price_history 
             (bitcoin_idx_rate, coindesk_rate, mean_avg)
             VALUES (%s, %s, %s);'''
    db.connect.insert(sql, rates)


if __name__ == '__main__':
    """Entry point to script."""
    store_gbp_rates()
