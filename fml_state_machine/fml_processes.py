import time
import fml_enums
import fml_misc
import fml_globals

def data_acquisition_process(adc, button, nozzle, leakage):
    while True:
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Starting data acquisition process...")
        ''' adc conversion '''
        fml_globals.adc_result = adc.get_conversion_result()
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] ADC conversion: {fml_globals.adc_result}")

        ''' button status updated '''
        fml_globals.button_status = button.update_status()
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Button status update: {fml_globals.button_status}")

        ''' nozzle status update '''
        fml_globals.nozzle_status = nozzle.update_status()
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Nozzle status update: {fml_globals.nozzle_status}")

        ''' leakage status update '''
        fml_globals.leakage_stats = leakage.update_status()
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Leakage status update: {fml_globals.leakage_stats}")

        if fml_globals.debug: print("f[{time.perf_counter_ns()}] Data acquisition completed. Sleeping for 100ms...")

        # sleep for 100 miliseconds
        time.sleep(0.1)

def display_control_process(display):
    while True:
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Starting display update process...")
        if fml_globals.display_type==fml_enums.FMLDisplayType.TANK_LEVEL:
            if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Display type: {fml_globals.display_type}")

            display_intensity = fml_globals.config_params_path[""]
            display_value = fml_misc.adc_to_liters(fml_globals.adc_result)
            
        display.update(display_value, display_intensity)

        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Display intensity: {display_intensity}")
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Display value (adc): {display_value}")

        if fml_globals.debug: print("f[{time.perf_counter_ns()}] Display update completed. Sleeping for 100ms...")

        # sleep for 100 miliseconds
        time.sleep(0.1)
            

        print(f"{time.perf_counter()}: display control")
        time.sleep(1)
