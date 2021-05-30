import multiprocessing
import time

from fml_adc import MCP346xR
from fml_display import Display7Seg
from fml_globals import config_params_dict, tank_params_dict, button_inp_pin, nozzle_inp_pin, leakage_inp_pin
from fml_misc import FMLMachine, FMLButton
from fml_processes import data_acquisition_process, display_control_process
from fml_rpicm4 import SPI as RPI_CM4_SPI

import fml_globals

if __name__=="__main__":
    ''' globals '''
    fml_globals.adc_result = multiprocessing.Value('L', 0)
    fml_globals.button_status = multiprocessing.Value('B', 0)
    fml_globals.nozzle_status = multiprocessing.Value('B', 0)
    fml_globals.leakage_status = multiprocessing.Value('B', 0)
    fml_globals.display_type =  multiprocessing.Value('B', 0)

    ''' configure MCP346xR ADC '''
    adc = MCP346xR(RPI_CM4_SPI.DEV0_CS0)

    # configure mux setup
    adc.mux.set_mux_vin_p(0b0000) # ch0 (default)
    adc.mux.set_mux_vin_n(0b0001) # ch1 (default)
    adc.write_mux()

    # enable scan channel
    adc.scan.set_scan_diff_ch(0b1000) # differential channel A (ch0-ch1)
    adc.write_scan()

    # switch to internal clock
    adc.config0.set_clk_sel(0b10)
    adc.write_config()    

    ''' configure button '''
    button = FMLButton(gpio_bcm_pin=button_inp_pin, inverted=False, debounce=True, debounce_counts=2)

    ''' configure nozzle '''
    nozzle = FMLButton(gpio_bcm_pin=nozzle_inp_pin, inverted=False, debounce=True, debounce_counts=2)

    ''' configure leakage '''
    leakage = FMLButton(gpio_bcm_pin=leakage_inp_pin, inverted=False, debounce=True, debounce_counts=2)

    ''' configure flow encoder '''
    pass # todo:

    ''' configure pump output '''
    pass # todo:

    ''' configure display '''
    display = Display7Seg(RPI_CM4_SPI.DEV1_CS0)

    ''' set up parallel processes '''
    processes = list()

    # create processes for data acquisition and display, then add them to the processes list
    processes.append(multiprocessing.Process(target=data_acquisition_process, args=[adc, fml_globals.adc_result, button, fml_globals.button_status, nozzle, fml_globals.nozzle_status, leakage, fml_globals.leakage_status], name="data acquisition process"))
    processes.append(multiprocessing.Process(target=display_control_process, args=[display, fml_globals.display_type, fml_globals.adc_result], name="display control process"))

    # start processes
    for process in processes:
        process.start()

    ''' init fml state machine '''
    # init state machine
    fml_machine = FMLMachine()

    ''' main loop '''
    while True:
        # default state
        if fml_machine.is_default:
            # fml_machine.default_to_prev_refill()
            # fml_machine.default_to_curr_refill()
            # fml_machine.default_to_nozzle_fill()
            pass

        # prev_refill state
        elif fml_machine.is_prev_refill:
            # fml_machine.prev_refill_to_default()
            pass

        # curr_refill state
        elif fml_machine.is_curr_refill:
            # fml_machine.curr_refill_to_default()
            pass

        # nozzle_fill state
        elif fml_machine.is_nozzle_fill:
            # fml_machine.nozzle_fill_to_default()
            pass

        # error - unknown state
        else:
            pass
