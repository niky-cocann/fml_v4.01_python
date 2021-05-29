import time
import fml_enums
import fml_misc
import fml_globals

def data_acquisition_process(adc, adc_result, button, button_status, nozzle, nozzle_status, leakage, leakage_status):
    while True:
        if fml_globals.debug: print(f"\n===========================================================================================================")
        if fml_globals.debug: print(f"===== DATA ACQUISITION PROCESS ============================================================================")
        if fml_globals.debug: print(f"===========================================================================================================")

        if fml_globals.debug: print(f"\n[{time.perf_counter_ns()}] Starting data acquisition process...")

        ''' adc conversion '''
        adc_result.value = adc.get_conversion_result()
        if fml_globals.debug: print(f"\n[{time.perf_counter_ns()}] ADC conversion: {adc_result.value}")

        ''' button status updated '''
        button_status.value = int(button.update_status())
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Button status update: {button_status.value}")

        ''' nozzle status update '''
        nozzle_status.value = int(nozzle.update_status())
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Nozzle status update: {nozzle_status.value}")

        ''' leakage status update '''
        leakage_status.value = int(leakage.update_status())
        
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Leakage status update: {leakage_status.value}")

        if fml_globals.debug: print(f"\n[{time.perf_counter_ns()}] Data acquisition completed. Sleeping for 1s...")

        # sleep for 1 miliseconds
        time.sleep(1)

def display_control_process(display, display_type, adc_result):
    while True:
        if fml_globals.debug: print(f"\n===========================================================================================================")
        if fml_globals.debug: print(f"===== DISPLAY UPDATE PROCESS ==============================================================================")
        if fml_globals.debug: print(f"===========================================================================================================")

        if fml_globals.debug: print(f"\n[{time.perf_counter_ns()}] Starting display update process...\n")

        if display_type.value==fml_enums.FMLDisplayType.TANK_LEVEL.value:
            if fml_globals.debug: print(f"\n[{time.perf_counter_ns()}] Display type: {fml_enums.FMLDisplayType(display_type.value)}")
            display_intensity = int(fml_globals.config_params_dict["display brightness (normal operating mode)"])
            display_value = fml_misc.adc_to_liters(adc_result.value, fml_globals.tank_params_dict)
            
        display.update(display_value, display_intensity)

        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Display intensity: {display_intensity}")
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Display value (adc): {adc_result.value}")
        if fml_globals.debug: print(f"[{time.perf_counter_ns()}] Display value (liters): {display_value}")

        if fml_globals.debug: print(f"\n[{time.perf_counter_ns()}] Display update completed. Sleeping for 1s...")

        # sleep for 1 seconds
        time.sleep(1)
