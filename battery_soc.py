import battery_thresholds as bt
def soc_beyond_limit(soc):
    if soc < bt.STATE_OF_CHARGE_MIN or soc > bt.STATE_OF_CHARGE_MAX:
        return True
    return False