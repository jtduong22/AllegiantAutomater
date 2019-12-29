from AllegiantAutomator import allegiant_automator
from allegiant_config import option

options_file = 'options.cfg'
options = option()
options.import_config_file(options_file)

print(allegiant_automator(options))