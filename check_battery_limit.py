from battery_temperature import temperature_beyond_limit
from battery_soc import soc_beyond_limit
from battery_charge_rate import charge_rate_beyond_limit

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
