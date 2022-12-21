from battery_params_thresholds import PARAMS_THRESHOLD_COUNT, BATTERY_PARAMS_THRESHOLDS
from threshold_checker import thresholdMaxExcluded, thresholdMinExcluded
from send_alert import print_message
# ------------------------------------------------------------------- #  
def get_warning_threshold(value, tolerance):
    return value * (tolerance/100)
# ------------------------------------------------------------------- #  
def temperature_warning_limit(temperature):
    warning_thresold = get_warning_threshold(BATTERY_PARAMS_THRESHOLDS["TEMPERATURE"]["BREACH_HIGH"], BATTERY_PARAMS_THRESHOLDS["TEMPERATURE"]["WARNING_TOLERANCE"])
    warning_low = BATTERY_PARAMS_THRESHOLDS["TEMPERATURE"]["BREACH_LOW"] + warning_thresold
    warning_high = BATTERY_PARAMS_THRESHOLDS["TEMPERATURE"]["BREACH_HIGH"] - warning_thresold
    return thresholdMinExcluded(temperature, warning_low) or thresholdMaxExcluded(temperature, warning_high)

def soc_warning_limit(soc):
    warning_thresold = get_warning_threshold(BATTERY_PARAMS_THRESHOLDS["SOC"]["BREACH_HIGH"], BATTERY_PARAMS_THRESHOLDS["SOC"]["WARNING_TOLERANCE"])
    warning_low = BATTERY_PARAMS_THRESHOLDS["SOC"]["BREACH_LOW"] + warning_thresold
    warning_high = BATTERY_PARAMS_THRESHOLDS["SOC"]["BREACH_HIGH"] - warning_thresold
    return thresholdMinExcluded(soc, warning_low) or thresholdMaxExcluded(soc, warning_high)

def charge_rate_warning_limit(charge_rate):
    warning_thresold = get_warning_threshold(BATTERY_PARAMS_THRESHOLDS["CHARGE_RATE"]["BREACH_HIGH"], BATTERY_PARAMS_THRESHOLDS["CHARGE_RATE"]["WARNING_TOLERANCE"])
    warning_high = BATTERY_PARAMS_THRESHOLDS["CHARGE_RATE"]["BREACH_HIGH"] - warning_thresold
    return thresholdMaxExcluded(charge_rate, warning_high)
# ------------------------------------------------------------------- #  
def battery_check_charge_rate_warning(*args):
    if charge_rate_warning_limit(args[2]):
      print_message(1, "charge_rate", args[2])
      return False
    return True

def battery_check_soc_warning(*args):
    if soc_warning_limit(args[1]):
      print_message(1, "soc", args[1])
      return False
    return battery_check_charge_rate_warning(*args)

def check_warning(*args):
    if temperature_warning_limit(args[0]):
      print_message(1, "temperature", args[0])
      return False
    return battery_check_soc_warning(*args)    