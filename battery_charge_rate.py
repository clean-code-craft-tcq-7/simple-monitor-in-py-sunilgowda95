import battery_thresholds as bt
from checkThresholdLimit import checkMinExcluded, checkMaxExcluded

def charge_rate_beyond_limit(charge_rate):
  return checkMaxExcluded(charge_rate, bt.CHAGE_RATE_MAX)
