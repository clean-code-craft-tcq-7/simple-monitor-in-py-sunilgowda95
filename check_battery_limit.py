import battery_thresholds as bt
from checkThresholdLimit import checkMinExcluded, checkMaxExcluded

def temperature_beyond_limit(temperature):
  return checkMinExcluded(temperature, bt.TEMPERATURE_MIN) or checkMaxExcluded(temperature, bt.TEMPERATURE_MAX)

def soc_beyond_limit(soc):
  return checkMinExcluded(soc, bt.STATE_OF_CHARGE_MIN) or checkMaxExcluded(soc, bt.STATE_OF_CHARGE_MAX)

def charge_rate_beyond_limit(charge_rate):
  return checkMaxExcluded(charge_rate, bt.CHAGE_RATE_MAX)
    
# old Logic:
#   if temp is True return False
#   elif soc is True return False
#   elif rate is True return False
#   else True
# This is deduced as : 
#   if any one is True, Return False, else True
#   if any two are True, Return False, else True
#   if all three are True, Return False, else True
def battery_is_ok(temperature, soc, charge_rate):
  if temperature_beyond_limit(temperature) or soc_beyond_limit(soc) or charge_rate_beyond_limit(charge_rate):
    return False
  return True
