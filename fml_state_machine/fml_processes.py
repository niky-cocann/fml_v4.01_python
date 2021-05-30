import time
import fml_enums
import fml_misc
import fml_globals

def data_acquisition_process(adc, adc_result, button, button_status, nozzle, nozzle_status, leakage, leakage_status):
    while True:
        if fml_globals.debug_data_acquisition_process: print(f"\n===========================================================================================================")
        if fml_globals.debug_data_acquisition_process: print(f"===== DATA ACQUISITION PROCESS ============================================================================")
        if fml_globals.debug_data_acquisition_process: print(f"===========================================================================================================")

        process_start = time.perf_counter_ns()
        if fml_globals.debug_data_acquisition_process: print(f"\n[{process_start}] Starting data acquisition process...")

        ''' adc conversion '''
        adc_result.value = adc.get_conversion_result()
        if fml_globals.debug_data_acquisition_process: print(f"\n[{time.perf_counter_ns()}] ADC conversion: {adc_result.value}")

        ''' button status updated '''
        button_status.value = int(button.update_status())
        if fml_globals.debug_data_acquisition_process: print(f"[{time.perf_counter_ns()}] Button status update: {button_status.value}")

        ''' nozzle status update '''
        nozzle_status.value = int(nozzle.update_status())
        if fml_globals.debug_data_acquisition_process: print(f"[{time.perf_counter_ns()}] Nozzle status update: {nozzle_status.value}")

        ''' leakage status update '''
        leakage_status.value = int(leakage.update_status())
        if fml_globals.debug_data_acquisition_process: print(f"[{time.perf_counter_ns()}] Leakage status update: {leakage_status.value}")

        process_stop = time.perf_counter_ns()
        if fml_globals.debug_data_acquisition_process: print(f"\n[{process_stop}] Data acquisition completed. Process duration: {(process_stop - process_start) // 1000}us. Sleeping for {fml_globals.data_acquisition_process_sleep}s...")

        # sleep
        time.sleep(fml_globals.data_acquisition_process_sleep)

def display_control_process(display, display_type, adc_result):
    while True:
        if fml_globals.debug_display_update_process: print(f"\n===========================================================================================================")
        if fml_globals.debug_display_update_process: print(f"===== DISPLAY UPDATE PROCESS ==============================================================================")
        if fml_globals.debug_display_update_process: print(f"===========================================================================================================")

        process_start = time.perf_counter_ns()
        if fml_globals.debug_display_update_process: print(f"\n[{process_start}] Starting display update process...\n")

        if display_type.value==fml_enums.FMLDisplayType.TANK_LEVEL.value:
            if fml_globals.debug_display_update_process: print(f"\n[{time.perf_counter_ns()}] Display type: {fml_enums.FMLDisplayType(display_type.value)}")
            display_intensity = int(fml_globals.config_params_dict["display brightness (normal operating mode)"])
            ohms = fml_misc.adc_to_ohms(adc_result.value)

            if str(ohms) in fml_globals.tank_params_dict.keys():
                display_value = fml_globals.tank_params_dict[str(ohms)]
            else:
                if ohms<min(fml_globals.tank_params_dict.keys()):
                    display_value = fml_globals.tank_params_dict[min(fml_globals.tank_params_dict.keys())]
                elif ohms>max(fml_globals.tank_params_dict.keys()):
                    display_value = fml_globals.tank_params_dict[max(fml_globals.tank_params_dict.keys())]
                else:
                    display_value = "0"

            if '.' in display_value:
                display_value = f"{display_value}".rjust(5)[:5]
                if display_value[-1]=='.':
                    display_value = display_value[:-1]
            else:
                display_value = f"{display_value}".rjust(4)[:4]
            
            display_value = f"{display_value}L"

        print(f"ohms: {ohms}")
        print(f"liters: {display_value}")

        display.update(display_value, display_intensity)

        if fml_globals.debug_display_update_process: print(f"[{time.perf_counter_ns()}] Display intensity: {display_intensity}")
        if fml_globals.debug_display_update_process: print(f"[{time.perf_counter_ns()}] Display value (adc): {adc_result.value}")
        if fml_globals.debug_display_update_process: print(f"[{time.perf_counter_ns()}] Display value (liters): {display_value}")

        process_stop = time.perf_counter_ns()
        if fml_globals.debug_display_update_process: print(f"\n[{process_stop}] Display update completed. Process duration: {(process_stop - process_start) // 1000}us. Sleeping for {fml_globals.display_update_process_sleep}s...")

        # sleep
        time.sleep(fml_globals.display_update_process_sleep)
