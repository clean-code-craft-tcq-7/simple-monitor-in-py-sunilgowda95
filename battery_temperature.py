import battery_thresholds as bt
def temperature_beyond_limit(temperature):
    if temperature < bt.TEMPERATURE_MIN or temperature > bt.TEMPERATURE_MAX:
        return True
    return False

