import battery_thresholds as bt
def charge_rate_beyond_limit(charge_rate):
    if charge_rate > bt.CHAGE_RATE_MAX:
        return True
    return False
    