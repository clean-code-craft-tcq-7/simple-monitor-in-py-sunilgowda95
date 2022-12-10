import battery_thresholds as bt
from checkThresholdLimit import checkMinExcluded, checkMaxExcluded

def temperature_beyond_limit(temperature):
  return checkMinExcluded(temperature, bt.TEMPERATURE_MIN) or checkMaxExcluded(temperature, bt.TEMPERATURE_MAX)
