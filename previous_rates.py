import subprocess
import db.connect


def history_compare(current_rates):
    """Send notification to screen if current_avg reaches new high or new low."""
    highest_avg_rate = _get_highest_avg_rate()
    lowest_avg_rate = _get_lowest_avg_rate()
    current_avg = current_rates[2]

    if current_avg < lowest_avg_rate:
        message = f"Alert!!!\nBitcoin at LOWEST rate!\nCurrently: £{current_avg:_.2f}!"
        subprocess.Popen(['notify-send', message])

    if current_avg > highest_avg_rate:
        message = f"Alert!!!\nBitcoin at HIGHEST rate!\nCurrently: £{current_avg:_.2f}!"
        subprocess.Popen(['notify-send', message])


def _get_highest_avg_rate():
    sql = 'SELECT MAX(mean_avg) FROM bitcoin_price_history;'
    highest_avg_rate = db.connect.select(sql)[0][0]
    return float(highest_avg_rate)


def _get_lowest_avg_rate():
    sql = 'SELECT MIN(mean_avg) FROM bitcoin_price_history;'
    lowest_avg_rate = db.connect.select(sql)[0][0]
    return float(lowest_avg_rate)