from battery_check_breach import check_breach, temperature_beyond_limit, soc_beyond_limit, charge_rate_beyond_limit

TEMPERATURE_THRESHOLD_TEST_VALUES = {"0":[0,1,45], "1":[-1,46]}  # assert temperature < 0, ==0, > 0, == 45, > 45 
SOC_THRESHOLD_TEST_VALUES = {"0":[20,21,80], "1":[19,81]} # assert soc < 20, ==20, > 20, == 80, > 80 
CHARGE_RATE_TEST_VALUES = {"0":[0.79, 0.8], "1":[0.81]} # assert charge_rate < 0.8, ==0.8, > 0.8
TEMP_SOC_CHARGE_RATE_TEST_VALUES = {"0":[[46, 20, 0.8],[44, 81, 0.8], [44, 25, 0.81], [-1, 20, 0.8],[0, 19, 0.8]], "1":[[25, 25, 0.8]]}

def test_cases_breach_temperature():
  for output, temperature_list,  in TEMPERATURE_THRESHOLD_TEST_VALUES.items():
    output = bool(int(output))
    for temperature in temperature_list:
      assert temperature_beyond_limit(temperature)==output, f'temperature threshold check failed for value {temperature}'

def test_cases_breach_soc():
  for output, soc_list in SOC_THRESHOLD_TEST_VALUES.items():
    output = bool(int(output))
    for soc in soc_list:
      assert soc_beyond_limit(soc)==output, f'soc threshold check failed for value {soc}'

def test_cases_breach_charge_rate():
  for output, charge_rate_list in CHARGE_RATE_TEST_VALUES.items():
    output = bool(int(output))
    for charge_rate in charge_rate_list:    
      assert charge_rate_beyond_limit(charge_rate)==output, f'charge_rate threshold check failed for value {charge_rate}'    

def test_cases_breach_all(): 
  for output, test_value_lists in TEMP_SOC_CHARGE_RATE_TEST_VALUES.items():
    for test_value in test_value_lists:
      assert check_breach(test_value[0], test_value[1], test_value[2]) == bool(int(output)), f'limit check output {bool(int(output))} failed for temperature {test_value[0]}, soc {test_value[1]}, charge_rate {test_value[2]}'

def test_cases_breach():
  test_cases_breach_temperature()
  test_cases_breach_soc()
  test_cases_breach_charge_rate()  
  test_cases_breach_all()
