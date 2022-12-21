from battery_check_breach import check_breach
from battery_check_warning import check_warning

def battery_is_ok(*args):
  if not check_breach(*args):
    return False # battery state is under warning
  return check_warning(*args)