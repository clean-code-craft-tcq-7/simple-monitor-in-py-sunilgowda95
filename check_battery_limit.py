from battery_temperature import temperature_beyond_limit
from battery_soc import soc_beyond_limit
from battery_charge_rate import charge_rate_beyond_limit

def check_soc_charge_rate(soc, charge_rate):
  if soc_beyond_limit(soc):
    return False
  return not charge_rate_beyond_limit(charge_rate)
    
def battery_is_ok(temperature, soc, charge_rate):
  if temperature_beyond_limit(temperature):
    return False
  return check_soc_charge_rate(soc, charge_rate) 
