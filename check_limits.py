from check_battery_limit import battery_is_ok
from battery_temperature import temperature_beyond_limit
from battery_soc import soc_beyond_limit
from battery_charge_rate import charge_rate_beyond_limit

TEMPERATURE_THRESHOLD_TEST_VALUES = {"-1":True, "0":False, "1":False, "45":False, "46":True}
SOC_THRESHOLD_TEST_VALUES = {"19":True, "20":False, "21":False, "80":False, "81":True}
CHARGE_STATE_TEST_VALUES = {"0.79":False, "0.8":False, "0.81":True}

if __name__ == '__main__':
  # assert temperature < 0, ==0, > 0, == 45, > 45 --> 2 paths
  for temperature, output in TEMPERATURE_THRESHOLD_TEST_VALUES.items():
    assert temperature_beyond_limit(float(temperature))==output, f'temperature threshold check failed for value {temperature}'
  # assert soc < 20, ==20, > 20, == 80, > 80 --> 2 paths
  for soc, output in SOC_THRESHOLD_TEST_VALUES.items():
    assert soc_beyond_limit(float(soc))==output, f'soc threshold check failed for value {soc}'
  # assert charge_rate < 0.8, ==0.8, > 0.8 --> 2 paths
  for charge_rate, output in CHARGE_STATE_TEST_VALUES.items():
    assert charge_rate_beyond_limit(float(charge_rate))==output, f'charge_rate threshold check failed for value {charge_rate}'    
  # assert battery_is_ok for 2 paths
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  print("All is Well!")
