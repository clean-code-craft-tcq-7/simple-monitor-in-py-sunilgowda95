import battery_thresholds as bt
from checkThresholdLimit import checkMinExcluded, checkMaxExcluded
from battery_charge_rate import charge_rate_beyond_limit

def soc_beyond_limit(soc):
  return checkMinExcluded(soc, bt.STATE_OF_CHARGE_MIN) or checkMaxExcluded(soc, bt.STATE_OF_CHARGE_MAX)

def check_soc_charge_rate(soc, charge_rate):
  if soc_beyond_limit(soc):
    return False
  return not charge_rate_beyond_limit(charge_rate)