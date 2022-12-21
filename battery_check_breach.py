from battery_params_thresholds import PARAMS_THRESHOLD_COUNT, BATTERY_PARAMS_THRESHOLDS
from threshold_checker import thresholdMaxExcluded, thresholdMinExcluded
from send_alert import print_message
# ------------------------------------------------------------------- #  
def temperature_beyond_limit(temperature): 
  return thresholdMinExcluded(temperature, BATTERY_PARAMS_THRESHOLDS["TEMPERATURE"]["BREACH_LOW"]) or thresholdMaxExcluded(temperature, BATTERY_PARAMS_THRESHOLDS["TEMPERATURE"]["BREACH_HIGH"])

def soc_beyond_limit(soc):
  return thresholdMinExcluded(soc, BATTERY_PARAMS_THRESHOLDS["SOC"]["BREACH_LOW"]) or thresholdMaxExcluded(soc, BATTERY_PARAMS_THRESHOLDS["SOC"]["BREACH_HIGH"])

def charge_rate_beyond_limit(charge_rate):
  return thresholdMaxExcluded(charge_rate, BATTERY_PARAMS_THRESHOLDS["CHARGE_RATE"]["BREACH_HIGH"])  
# ------------------------------------------------------------------- #  
def battery_check_charge_rate_breach(*args):
  if charge_rate_beyond_limit(args[2]):
    print_message(0, "charge_rate", args[2])
    return False
  return True

def battery_check_soc_breach(*args):
  if soc_beyond_limit(args[1]):
    print_message(0, "soc", args[1])
    return False
  return battery_check_charge_rate_breach(*args)

def check_breach(*args):
  if temperature_beyond_limit(args[0]):
    print_message(0, "temperature", args[0])
    return False
  return battery_check_soc_breach(*args)
# ------------------------------------------------------------------- #  