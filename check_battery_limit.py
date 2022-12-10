from battery_check_thresholds import temperature_beyond_limit, soc_beyond_limit, charge_rate_beyond_limit

def battery_is_ok_for_soc_charge_rate(soc, charge_rate):
  if soc_beyond_limit(soc):
    return False
  return not charge_rate_beyond_limit(charge_rate)
    
def battery_is_ok(temperature, soc, charge_rate):
  if temperature_beyond_limit(temperature):
    return False
  return battery_is_ok_for_soc_charge_rate(soc, charge_rate) 
