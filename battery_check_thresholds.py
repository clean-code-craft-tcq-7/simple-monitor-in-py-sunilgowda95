TEMPERATURE_MIN = 0
TEMPERATURE_MAX = 45
STATE_OF_CHARGE_MIN = 20
STATE_OF_CHARGE_MAX = 80
CHAGE_RATE_MAX = 0.8

from checkThresholdLimit import checkMinExcluded, checkMaxExcluded

def temperature_beyond_limit(temperature):
  return checkMinExcluded(temperature, TEMPERATURE_MIN) or checkMaxExcluded(temperature, TEMPERATURE_MAX)

def soc_beyond_limit(soc):
  return checkMinExcluded(soc, STATE_OF_CHARGE_MIN) or checkMaxExcluded(soc, STATE_OF_CHARGE_MAX)

def charge_rate_beyond_limit(charge_rate):
  return checkMaxExcluded(charge_rate, CHAGE_RATE_MAX)
