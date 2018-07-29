#!/TODO/insert/path/for/script
import subprocess
import db.connect


def check_current_rate():
    """Send notification to screen if current_avg reaches new high or new low."""
    current_avg = get_current_avg_rate()
    highest_avg = _get_highest_avg_rate()
    lowest_avg = _get_lowest_avg_rate()

    if current_avg < lowest_avg:
        message = f"Alert!!!\nBitcoin at LOWEST rate!\nCurrently: £{current_avg:_.2f}!"
        subprocess.Popen(['notify-send', message])

    elif current_avg > highest_avg:
        message = f"Alert!!!\nBitcoin at HIGHEST rate!\nCurrently: £{current_avg:_.2f}!"
        subprocess.Popen(['notify-send', message])

    else:
        message = f"Nothing to report.\nCurrent avg = £{current_avg:_.2f}\n"
        message2 = f"Lowest avg =  £{lowest_avg:_.2f}\nHighest avg = £{highest_avg:_.2f}"
        subprocess.Popen(['notify-send', message + message2])


def get_current_avg_rate():
    sql = '''SELECT mean_avg FROM bitcoin_price_history WHERE created_on = (
                SELECT MAX(created_on) FROM bitcoin_price_history
             );'''
    current_avg_rate = db.connect.select(sql)[0][0]
    return float(current_avg_rate)


def _get_highest_avg_rate():
    sql = 'SELECT MAX(mean_avg) FROM bitcoin_price_history;'
    highest_avg_rate = db.connect.select(sql)[0][0]
    return float(highest_avg_rate)


def _get_lowest_avg_rate():
    sql = 'SELECT MIN(mean_avg) FROM bitcoin_price_history;'
    lowest_avg_rate = db.connect.select(sql)[0][0]
    return float(lowest_avg_rate)


if __name__ == '__main__':
    check_current_rate()