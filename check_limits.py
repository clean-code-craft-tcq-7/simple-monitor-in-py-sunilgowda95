from battery_check import battery_is_ok
from check_limits_breach import test_cases_breach
from check_limits_warning import test_cases_warning

BATTERY_TEST_VALUES = {"0":[[46, 20, 0.8],[44, 81, 0.8], [44, 25, 0.81], [-1, 20, 0.8],[0, 19, 0.8],[42.76, 24, 0.76],[42, 23, 0.76], [42, 24, 0.77], [42, 23, 0.77],[42.77, 20, 0.76],[45, 20, 0.8]], "1":[[30, 40, 0.4],[2.25,24,0.76]]}

if __name__ == '__main__':
  test_cases_breach()
  test_cases_warning()
  for output, test_value_lists in BATTERY_TEST_VALUES.items():
    for test_value in test_value_lists:
      assert battery_is_ok(test_value[0], test_value[1], test_value[2]) == bool(int(output)), f'limit check output {bool(int(output))} failed for temperature {test_value[0]}, soc {test_value[1]}, charge_rate {test_value[2]}'  
  print("Battery Parameters Test Done!")
