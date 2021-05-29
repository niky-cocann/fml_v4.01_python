import csv
from fml_enums import FMLDisplayType

# functions
def load_config_params(path):
    config_params_dict = {}

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, skipinitialspace=True, quotechar="'")
        _ = next(csv_reader) # skip first row
        for row in csv_reader:
            config_params_dict[row[0]] = row[1]
        
    return config_params_dict

def load_tank_params(path):
    tank_params_dict = {}

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, skipinitialspace=True, quotechar="'")
        _ = next(csv_reader) # skip first row
        for row in csv_reader:
            tank_params_dict[row[0]] = row[1]
        
    return tank_params_dict


''' load config and tank parameters '''
#config_params_path = "/home/niky/Documents/Projects/MindEngineering/fml-python-dev/fml_flask/app/data/config.csv" # dev machine
config_params_path = "/home/pi/Documents/fml_v4.01_python/fml_flask/app/data/config.csv" # rpi cm4
config_params_dict = load_config_params(config_params_path)

# tank_params_path = "/home/niky/Documents/Projects/MindEngineering/fml-python-dev/fml_flask/app/data/tank_params.csv" # dev machine
tank_params_path = "/home/pi/Documents/fml_v4.01_python/fml_flask/app/data/tank_params.csv" # rpi cm4
tank_params_dict = load_tank_params(tank_params_path)

''' globals '''
debug = True
adc_result = 0
display_type = FMLDisplayType.TANK_LEVEL
button_status = False
nozzle_status = False
leakage_stats = False

# rpi gpio input pins
button_inp_pin = 2
nozzle_inp_pin = 4
flow_inp_pin = 5
leakage_inp_pin = 3

# rpi gpio output pins
pump_out_pin = 6
