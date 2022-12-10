TEMPERATURE_MIN = 0
TEMPERATURE_MAX = 45
STATE_OF_CHARGE_MIN = 20
STATE_OF_CHARGE_MAX = 80
CHAGE_RATE_MAX = 0.8

from threshold_checker import thresholdMinExcluded, thresholdMaxExcluded

def temperature_beyond_limit(temperature):
  return thresholdMinExcluded(temperature, TEMPERATURE_MIN) or thresholdMaxExcluded(temperature, TEMPERATURE_MAX)

def soc_beyond_limit(soc):
  return thresholdMinExcluded(soc, STATE_OF_CHARGE_MIN) or thresholdMaxExcluded(soc, STATE_OF_CHARGE_MAX)

def charge_rate_beyond_limit(charge_rate):
  return thresholdMaxExcluded(charge_rate, CHAGE_RATE_MAX)
