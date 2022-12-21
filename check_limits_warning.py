from battery_check_warning import check_warning, temperature_warning_limit, soc_warning_limit, charge_rate_warning_limit

TEMPERATURE_THRESHOLD_TEST_VALUES = {"0":[2.25,2.26,42.74,42.75], "1":[-1,0,2.24,42.76,45,46]}  # 0-2.25 & 42.75-45 --> warning range
SOC_THRESHOLD_TEST_VALUES = {"0":[24,25,75,76], "1":[19,20,23,77,80,81]} # 20-24 & 76-80 --> warning range
CHARGE_RATE_TEST_VALUES = {"0":[0.75, 0.76], "1":[0.77,0.8,0.81]} # 0.76-0.8 --> warning range
TEMP_SOC_CHARGE_RATE_TEST_VALUES = {"0":[[42.76, 24, 0.76],[42, 23, 0.76], [42, 24, 0.77], [42, 23, 0.77],[42.77, 20, 0.76],[45, 20, 0.8]], "1":[[30, 40, 0.4]]}

def test_cases_warning():
  for output, temperature_list,  in TEMPERATURE_THRESHOLD_TEST_VALUES.items():
    output = bool(int(output))
    for temperature in temperature_list:
      assert temperature_warning_limit(temperature)==output, f'temperature threshold check failed for value {temperature}'
  
  for output, soc_list in SOC_THRESHOLD_TEST_VALUES.items():
    output = bool(int(output))
    for soc in soc_list:
      assert soc_warning_limit(soc)==output, f'soc threshold check failed for value {soc}'
  
  for output, charge_rate_list in CHARGE_RATE_TEST_VALUES.items():
    output = bool(int(output))
    for charge_rate in charge_rate_list:    
      assert charge_rate_warning_limit(charge_rate)==output, f'charge_rate threshold check failed for value {charge_rate}'    

  for output, test_value_lists in TEMP_SOC_CHARGE_RATE_TEST_VALUES.items():
    for test_value in test_value_lists:
      assert check_warning(test_value[0], test_value[1], test_value[2]) == bool(int(output)), f'limit check output {bool(int(output))} failed for temperature {test_value[0]}, soc {test_value[1]}, charge_rate {test_value[2]}'
