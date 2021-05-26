import time
from fml_globals import debug, adc_result, display_type, button_status, nozzle_status, leakage_status

def data_acquisition_process(adc, button, nozzle, leakage):
    while True:
        if debug: print(f"[{time.perf_counter_ns()}] Starting data acquisition process...")
        ''' adc conversion '''
        if debug: print(f"[{time.perf_counter_ns()}] ADC conversion")
        adc_result = adc.get_conversion_result()

        ''' button status updated '''
        if debug: print(f"[{time.perf_counter_ns()}] Button status update")
        button_status = button.update_status()

        ''' nozzle status update '''
        if debug: print(f"[{time.perf_counter_ns()}] Nozzle status update")
        nozzle_status = nozzle.update_status()

        ''' leakage status update '''
        if debug: print(f"[{time.perf_counter_ns()}] Leakage status update")
        leakage_status = leakage.update_status()

        if debug: print("f[{time.perf_counter_ns()}] Data acquisition completed. Sleeping for 100ms...")

        # sleep for 100 miliseconds
        time.sleep(0.1)

def display_control_process(display):
    while True:
        print(f"{time.perf_counter()}: display control")
        time.sleep(1)
