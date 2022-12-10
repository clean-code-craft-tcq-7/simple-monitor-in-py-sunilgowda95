from battery_check import battery_is_ok, battery_is_ok_for_soc_charge_rate
from battery_check_thresholds import temperature_beyond_limit, soc_beyond_limit, charge_rate_beyond_limit

TEMPERATURE_THRESHOLD_TEST_VALUES = {"0":[0,1,45], "1":[-1,46]}  # assert temperature < 0, ==0, > 0, == 45, > 45 
SOC_THRESHOLD_TEST_VALUES = {"0":[20,21,80], "1":[19,81]} # assert soc < 20, ==20, > 20, == 80, > 80 
CHARGE_RATE_TEST_VALUES = {"0":[0.79, 0.8], "1":[0.81]} # assert charge_rate < 0.8, ==0.8, > 0.8
SOC_CHARGE_RATE_TEST_VALUES = {"0":[[19, 0.8]], "1":[[25, 0.8]]} # here charge rate is constant as only one condition is checked in function
TEMP_SOC_CHARGE_RATE_TEST_VALUES = {"0":[[46, 19, 0.8]], "1":[[25, 25, 0.8]]} # here soc & charge rate is constant as only one condition is checked in function

if __name__ == '__main__':
  for output, temperature_list,  in TEMPERATURE_THRESHOLD_TEST_VALUES.items():
    output = bool(int(output))
    for temperature in temperature_list:
      assert temperature_beyond_limit(temperature)==output, f'temperature threshold check failed for value {temperature}'
  
  for output, soc_list in SOC_THRESHOLD_TEST_VALUES.items():
    output = bool(int(output))
    for soc in soc_list:
      assert soc_beyond_limit(soc)==output, f'soc threshold check failed for value {soc}'
  
  for output, charge_rate_list in CHARGE_RATE_TEST_VALUES.items():
    output = bool(int(output))
    for charge_rate in charge_rate_list:    
      assert charge_rate_beyond_limit(charge_rate)==output, f'charge_rate threshold check failed for value {charge_rate}'    

  for output, test_value_lists in SOC_CHARGE_RATE_TEST_VALUES.items():
    for test_value in test_value_lists:
      assert battery_is_ok_for_soc_charge_rate(test_value[0], test_value[1]) == bool(int(output)), "limit check for soc/charge_rate"

  for output, test_value_lists in TEMP_SOC_CHARGE_RATE_TEST_VALUES.items():
    for test_value in test_value_lists:
      assert battery_is_ok(test_value[0], test_value[1], test_value[2]) == bool(int(output)), f'limit check output {bool(int(output))} failed for temperature {test_value[0]}, soc {test_value[1]}, charge_rate {test_value[2]}'
  print("All is Well!")
