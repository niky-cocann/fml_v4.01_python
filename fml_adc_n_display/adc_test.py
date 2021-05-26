import rpicm4
import adc

adc = adc.MCP346xR(rpicm4.SPI.DEV0_CS0)

# configure mux setup
adc.mux.set_mux_vin_p(0b1101)
adc.mux.set_mux_vin_n(0b1110)
adc.write_mux()

# enable scan channel
adc.scan.set_temp(0b1)
adc.write_scan()

# switch to internal clock
adc.config0.set_clk_sel(0b10)
adc.write_config()

# start conversion
adc.conversion_start_restart_fast_command()
# read interrupt flags
adc.read_irq()
# while new conversion data not available
while adc.irq.get_n_dr_status() == 0b1:
    # read interrupt flags
    adc.read_irq()

# read conversion result
adc.read_adcdata()

# display result
print("conversion result: 0x{:04X}".format(adc.adcdata.get_register()))
