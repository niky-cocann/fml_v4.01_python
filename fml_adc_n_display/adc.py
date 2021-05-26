# imports
import spi
import rpicm4
import warnings
from enum import Enum

warnings.filterwarnings("ignore", category=DeprecationWarning)


#
class Adcdata:
    """ADCDATA Register"""

    def __init__(self, adcdata_reg=0x0000):
        # register
        self.value = adcdata_reg

    # adcdata register

    def get_register(self):
        return self.value

    def set_register(self, adcdata_reg):
        # register
        self.value = adcdata_reg


#
class Config0:
    """CONFIG0 Register"""

    def __init__(self, config0_reg=0xC0):
        # register
        self.value = config0_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.config0 = (self.value & 0x80) >> 7
        self.vref_sel = (self.value & 0x40) >> 6
        self.clk_sel = (self.value & 0x30) >> 4
        self.cs_sel = (self.value & 0x0C) >> 2
        self.adc_mode = self.value & 0x03

    # config0 register

    def get_register(self):
        return self.value

    def set_register(self, config0_reg):
        # register
        self.value = config0_reg
        # unpack bit fields
        self.__unpack_register()

    # config0 bit field

    def get_config0(self):
        return self.config0

    def set_config0(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0x7F) | (new_value << 7)
        # unpack bit fields
        self.__unpack_register()

    # vref_sel bit field

    def get_vref_sel(self):
        return self.vref_sel

    def set_vref_sel(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xBF) | (new_value << 6)
        # unpack bit fields
        self.__unpack_register()

    # clk_sel bit field

    def get_clk_sel(self):
        return self.clk_sel

    def set_clk_sel(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xCF) | (new_value << 4)
        # unpack bit fields
        self.__unpack_register()

    # cs_sel bit field

    def get_cs_sel(self):
        return self.cs_sel

    def set_cs_sel(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xF3) | (new_value << 2)
        # unpack bit fields
        self.__unpack_register()

    # adc_mode bit field

    def get_adc_mode(self):
        return self.adc_mode

    def set_adc_mode(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFC) | new_value
        # unpack bit fields
        self.__unpack_register()


#
class Config1:
    """CONFIG1 Register"""

    def __init__(self, config1_reg=0x0C):
        # register
        self.value = config1_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.pre = (self.value & 0xC0) >> 6
        self.osr = (self.value & 0x3C) >> 2

    # config1 register

    def get_register(self):
        return self.value

    def set_register(self, config1_reg):
        # register
        self.value = config1_reg
        # unpack bit fields
        self.__unpack_register()

    # pre bit field

    def get_pre(self):
        return self.pre

    def set_pre(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0x3F) | (new_value << 6)
        # unpack bit fields
        self.__unpack_register()

    # osr bit field

    def get_osr(self):
        return self.osr

    def set_osr(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xC3) | (new_value << 2)
        # unpack bit fields
        self.__unpack_register()


#
class Config2:
    """CONFIG2 Register"""

    def __init__(self, config2_reg=0x8B):
        # register
        self.value = config2_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.boost = (self.value & 0xC0) >> 6
        self.gain = (self.value & 0x38) >> 3
        self.az_mux = (self.value & 0x04) >> 2
        self.az_ref = (self.value & 0x02) >> 1

    # config2 register

    def get_register(self):
        return self.value

    def set_register(self, config2_reg):
        # register
        self.value = config2_reg
        # unpack bit fields
        self.__unpack_register()

    # boost bit field

    def get_boost(self):
        return self.boost

    def set_boost(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0x3F) | (new_value << 6)
        # unpack bit fields
        self.__unpack_register()

    # gain bit field

    def get_gain(self):
        return self.gain

    def set_gain(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xC7) | (new_value << 3)
        # unpack bit fields
        self.__unpack_register()

    # az_mux bit field

    def get_az_mux(self):
        return self.az_mux

    def set_az_mux(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFB) | (new_value << 2)
        # unpack bit fields
        self.__unpack_register()

    # az_ref bit field

    def get_az_ref(self):
        return self.az_ref

    def set_az_ref(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFD) | (new_value << 1)
        # unpack bit fields
        self.__unpack_register()


#
class Config3:
    """CONFIG3 Register"""

    def __init__(self, config3_reg=0x00):
        # register
        self.value = config3_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.conv_mode = (self.value & 0xC0) >> 6
        self.data_format = (self.value & 0x30) >> 4
        self.crc_format = (self.value & 0x08) >> 3
        self.en_crccom = (self.value & 0x04) >> 2
        self.en_offcal = (self.value & 0x02) >> 1
        self.en_gaincal = self.value & 0x01

    # config3 register

    def get_register(self):
        return self.value

    def set_register(self, config3_reg):
        # register
        self.value = config3_reg
        # unpack bit fields
        self.__unpack_register()

    # conv_mode bit field

    def get_conv_mode(self):
        return self.conv_mode

    def set_conv_mode(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0x3F) | (new_value << 6)
        # unpack bit fields
        self.__unpack_register()

    # data_format bit field

    def get_data_format(self):
        return self.data_format

    def set_data_format(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xCF) | (new_value << 4)
        # unpack bit fields
        self.__unpack_register()

    # crc_format bit field

    def get_crc_format(self):
        return self.crc_format

    def set_crc_format(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xF7) | (new_value << 3)
        # unpack bit fields
        self.__unpack_register()

    # en_crccom bit field

    def get_en_crccom(self):
        return self.en_crccom

    def set_en_crccom(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFB) | (new_value << 2)
        # unpack bit fields
        self.__unpack_register()

    # en_offcal bit field

    def get_en_offcal(self):
        return self.en_offcal

    def set_en_offcal(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFD) | (new_value << 1)
        # unpack bit fields
        self.__unpack_register()

    # en_gaincal bit field

    def get_en_gaincal(self):
        return self.en_gaincal

    def set_en_gaincal(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFE) | new_value
        # unpack bit fields
        self.__unpack_register()


#
class Irq:
    """IRQ Register"""

    def __init__(self, irq_reg=0x73):
        # register
        self.value = irq_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.n_dr_status = (self.value & 0x40) >> 5
        self.n_crccfg_status = (self.value & 0x20) >> 4
        self.n_por_status = (self.value & 0x01) >> 3
        self.irq_mode = (self.value & 0x0C) >> 2
        self.en_fastcmd = (self.value & 0x02) >> 1
        self.en_stp = self.value & 0x01

    # irq register

    def get_register(self):
        return self.value

    def set_register(self, irq_reg):
        # register
        self.value = irq_reg
        # unpack bit fields
        self.__unpack_register()

    # n_dr_status bit field

    def get_n_dr_status(self):
        return self.n_dr_status

    # n_crccfg_status bit field

    def get_n_crccfg_status(self):
        return self.n_crccfg_status

    # n_por_status bit field

    def get_n_por_status(self):
        return self.n_por_status

    # irq_mode bit field

    def get_irq_mode(self):
        return self.irq_mode

    def set_irq_mode(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xF3) | (new_value << 2)
        # unpack bit fields
        self.__unpack_register()

    # en_fastcmd bit field

    def get_en_fastcmd(self):
        return self.en_fastcmd

    def set_en_fastcmd(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFD) | (new_value << 1)
        # unpack bit fields
        self.__unpack_register()

    # en_stp bit field

    def get_en_stp(self):
        return self.en_stp

    def set_en_stp(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFE) | new_value
        # unpack bit fields
        self.__unpack_register()


#
class Mux:
    """MUX Register"""

    def __init__(self, mux_reg=0x01):
        # register
        self.value = mux_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.mux_vin_p = (self.value & 0xF0) >> 4
        self.mux_vin_n = (self.value & 0x0F)

    # mux register

    def get_register(self):
        return self.value

    def set_register(self, mux_reg):
        # register
        self.value = mux_reg
        # unpack bit fields
        self.__unpack_register()

    # mux_vin_p bit field

    def get_mux_vin_p(self):
        return self.mux_vin_p

    def set_mux_vin_p(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0x0F) | (new_value << 4)
        # unpack bit fields
        self.__unpack_register()

    # mux_vin_n bit field

    def get_mux_vin_n(self):
        return self.mux_vin_n

    def set_mux_vin_n(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xF0) | new_value
        # unpack bit fields
        self.__unpack_register()


#
class Scan:
    """SCAN Register"""

    def __init__(self, scan_reg=0x000000):
        # register
        self.value = scan_reg
        # bit fields
        self.__unpack_register()

    def __unpack_register(self):
        # bit fields
        self.dly = (self.value & 0xE00000) >> 21
        self.offset = (self.value & 0x008000) >> 15
        self.vcm = (self.value & 0x004000) >> 14
        self.avdd = (self.value & 0x002000) >> 13
        self.temp = (self.value & 0x001000) >> 12
        self.scan_diff_ch = (self.value & 0x000F00) >> 8
        self.scan_se_ch = self.value & 0x0000FF

    # scan register

    def get_register(self):
        return self.value

    def set_register(self, scan_reg):
        # register
        self.value = scan_reg
        # unpack bit fields
        self.__unpack_register()

    # dly bit field

    def get_dly(self):
        return self.dly

    def set_dly(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0x1FFFFF) | (new_value << 21)
        # unpack bit fields
        self.__unpack_register()

    # offset bit field

    def get_offset(self):
        return self.offset

    def set_offset(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFF7FFF) | (new_value << 15)
        # unpack bit fields
        self.__unpack_register()

    # vcm bit field

    def get_vcm(self):
        return self.vcm

    def set_vcm(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFFBFFF) | (new_value << 14)
        # unpack bit fields
        self.__unpack_register()

    # avdd bit field

    def get_avdd(self):
        return self.avdd

    def set_avdd(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFFDFFF) | (new_value << 13)
        # unpack bit fields
        self.__unpack_register()

    # temp bit field

    def get_temp(self):
        return self.temp

    def set_temp(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFFEFFF) | (new_value << 12)
        # unpack bit fields
        self.__unpack_register()

    # scan_diff_ch bit field

    def get_scan_diff_ch(self):
        return self.scan_diff_ch

    def set_scan_diff_ch(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFFF0FF) | (new_value << 8)
        # unpack bit fields
        self.__unpack_register()

    # scan_se_ch bit field

    def get_scan_se_ch(self):
        return self.scan_se_ch

    def set_scan_se_ch(self, new_value):
        # parameter sanity check
        pass
        # update register value
        self.value = (self.value & 0xFFFF00) | new_value
        # unpack bit fields
        self.__unpack_register()


#
class Timer:
    """TIMER Register"""

    def __init__(self, timer_reg=0x000000):
        # register
        self.value = timer_reg

    # timer register

    def get_register(self):
        return self.value

    def set_register(self, timer_reg):
        # register
        self.value = timer_reg


#
class Offsetcal:
    """OFFSETCAL Register"""

    def __init__(self, offsetcal_reg=0x000000):
        # register
        self.value = offsetcal_reg

    # offsetcal register

    def get_register(self):
        return self.value

    def set_register(self, offsetcal_reg):
        # register
        self.value = offsetcal_reg & 0xFFFF00


#
class Gaincal:
    """GAINCAL Register"""

    def __init__(self, gaincal_reg=0x000000):
        # register
        self.value = gaincal_reg

    # gaincal register

    def get_register(self):
        return self.value

    def set_register(self, gaincal_reg):
        # register
        self.value = gaincal_reg & 0xFFFF00


#
class Lock:
    """LOCK Register"""

    def __init__(self, lock_reg=0xA5):
        # register
        self.value = lock_reg

    # lock register

    def get_register(self):
        return self.value

    def set_register(self, lock_reg):
        # register
        self.value = lock_reg


#
class Crccfg:
    """CRCCFG Register"""

    def __init__(self, timer_reg=0x0000):
        # register
        self.value = timer_reg

    # crccfg register

    def get_register(self):
        return self.value

    def set_register(self, crccfg_reg):
        # register
        self.value = crccfg_reg


#
class MCP346xR:
    """MCP346xR class"""

    # class variables
    DEVICE_ADDR = 0b01

    LOCK_PASS = 0x27
    UNLOCK_PASS = 0xA5

    # command type
    FAST_CMD = 0x0
    STATIC_READ_CMD = 0x1
    INCREMENTAL_WRITE_CMD = 0x2
    INCREMENTAL_READ_CMD = 0x3

    # fast commands
    START_CONVERSION_FAST_COMMAND = 0xA
    ENABLE_STANDBY_MODE_FAST_COMMAND = 0xB
    ENABLE_SHUTDOWN_MODE_FAST_COMMAND = 0xC
    ENABLE_FULL_SHUTDOWN_MODE_FAST_COMMAND = 0xD
    TRIGGER_FULL_RESET_FAST_COMMAND = 0xE

    # adcdata size
    ADCDATA_4BIT = 0x04
    ADCDATA_16BIT = 0x10
    ADCDATA_32BIT = 0x20

    # memory map
    ADCDATA_ADDR = 0x0
    CONFIG0_ADDR = 0x1
    CONFIG1_ADDR = 0x2
    CONFIG2_ADDR = 0x3
    CONFIG3_ADDR = 0x4
    IRQ_ADDR = 0x5
    MUX_ADDR = 0x6
    SCAN_ADDR = 0x7
    TIMER_ADDR = 0x8
    OFFSETCAL_ADDR = 0x9
    GAINCAL_ADDR = 0xA
    LOCK_ADDR = 0xD
    CRCCFG_ADDR = 0xF

    # mux 
    MUX_INT_VCM = 0b1111
    MUX_INT_TEMP_SDM = 0b1110
    MUX_INT_TEMP_SDP = 0b1101
    MUX_REFIN_N = 0b1100
    MUX_REFIN_P = 0b1011
    MUX_AVDD = 0b1001
    MUX_AGND = 0b1000
    MUX_CH7 = 0b0111
    MUX_CH6 = 0b0110
    MUX_CH5 = 0b0101
    MUX_CH4 = 0b0100
    MUX_CH3 = 0b0011
    MUX_CH2 = 0b0010
    MUX_CH1 = 0b0001
    MUX_CH0 = 0b0000

    # scan
    SCAN_DLY_512_DMCLK = 0b111
    SCAN_DLY_256_DMCLK = 0b110
    SCAN_DLY_128_DMCLK = 0b101
    SCAN_DLY_64_DMCLK = 0b100
    SCAN_DLY_32_DMCLK = 0b011
    SCAN_DLY_16_DMCLK = 0b010
    SCAN_DLY_8_DMCLK = 0b001
    SCAN_DLY_0_DMCLK = 0b000
    SCAN_OFFSET_ON = 0b1
    SCAN_OFFSET_OFF = 0b0
    SCAN_VCM_ON = 0b1
    SCAN_VCM_OFF = 0b0
    SCAN_AVDD_ON = 0b1
    SCAN_AVDD_OFF = 0b0
    SCAN_TEMP_ON = 0b1
    SCAN_TEMP_OFF = 0b0

    # init

    def __init__(self, spi_instance, spi_mode=spi.SPI.MODE_0, spi_bits_per_word=8, spi_speed=500000):
        # spi
        self.spi = spi.SPI(spi_instance)
        self.spi.mode = spi_mode
        self.spi.bits_per_word = spi_bits_per_word
        self.spi.speed = spi_speed

	# log level
        self.verbose = True

	# adc status
        self.status_byte = None

	# init adc memory map
        self.init_memory_map()

    # init memory map
    def init_memory_map(self):
        self.adcdata = Adcdata()
        self.config0 = Config0()
        self.config1 = Config1()
        self.config2 = Config2()
        self.config3 = Config3()
        self.irq = Irq()
        self.mux = Mux()
        self.scan = Scan()
        self.timer = Timer()
        self.offsetcal = Offsetcal()
        self.gaincal = Gaincal()
        self.lock = Lock()
        self.crccfg = Crccfg()

    # fast command api

    def conversion_start_restart_fast_command(self):
        if self.verbose:
            print("> adc conversion start/restart fast command")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.START_CONVERSION_FAST_COMMAND << 2) + self.FAST_CMD

        # spi communication
        transfer_buffer = [command_byte]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def standby_mode_fast_command(self):
        if self.verbose:
            print("> adc standby mode fast command")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.ENABLE_STANDBY_MODE_FAST_COMMAND << 2) + self.FAST_CMD

        # spi communication
        transfer_buffer = [command_byte]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def shutdown_mode_fast_command(self):
        if self.verbose:
            print("> adc shutdown mode fast command")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.ENABLE_SHUTDOWN_MODE_FAST_COMMAND << 2) + self.FAST_CMD

        # spi communication
        transfer_buffer = [command_byte]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def full_shutdown_mode_fast_command(self):
        if self.verbose:
            print("> adc full shutdown mode fast command")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.ENABLE_FULL_SHUTDOWN_MODE_FAST_COMMAND << 2) + self.FAST_CMD

        # spi communication
        transfer_buffer = [command_byte]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # adcdata register api

    def read_adcdata(self):
        if self.verbose:
            print("> read adcdata")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.ADCDATA_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        data_format = self.config3.get_data_format()
        if data_format == 0:
            additional_bytes = 2  # 2 for the adcdata register (16-bit)
        else:
            additional_bytes = 4  # 4 for the adcdata register (32-bit)
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if data_format == 0:
                adcdata_b15_b8 = response[1]
                adcdata_b7_b0 = response[2]
                adcdata_reg = 0x00000000 + \
                    (adcdata_b15_b8 << 8) + adcdata_b7_b0
            else:
                adcdata_b31_b24 = response[1]
                adcdata_b23_b16 = response[2]
                adcdata_b15_b8 = response[3]
                adcdata_b7_b0 = response[4]
                adcdata_reg = (adcdata_b31_b24 << 24) + (adcdata_b23_b16 <<
                                                         16) + (adcdata_b15_b8 << 8) + adcdata_b7_b0

            self.adcdata.set_register(adcdata_reg)

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                if data_format == 0:
                    print("  adcdata register: 0x{:04X}".format(
                        self.adcdata.get_register()))
                else:
                    print("  adcdata register: 0x{:08X}".format(
                        self.adcdata.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # config registers api

    def read_config(self):
        if self.verbose:
            print("> read config")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.CONFIG0_ADDR << 2) + self.INCREMENTAL_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        # 1 for the status byte, 3 for the CONFIG1, CONFIG2 and CONFIG3 registers
        additional_bytes = 4
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            self.config0.set_register(response[1])
            self.config1.set_register(response[2])
            self.config2.set_register(response[3])
            self.config3.set_register(response[4])

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  configuration registers: [0x{:02X}, 0x{:02X}, 0x{:02X}, 0x{:02X}]".format(self.config0.get_register(
                ), self.config1.get_register(), self.config2.get_register(), self.config3.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_config(self):
        if self.verbose:
            print("> write config")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.CONFIG0_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        transfer_buffer = [command_byte, self.config0.get_register(), self.config1.get_register(
        ), self.config2.get_register(), self.config3.get_register()]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  configuration registers: [0x{:02X}, 0x{:02X}, 0x{:02X}, 0x{:02X}]".format(self.config0.get_register(
                ), self.config1.get_register(), self.config2.get_register(), self.config3.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # irq register api

    def read_irq(self):
        if self.verbose:
            print("> read irq")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.IRQ_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 1  # 1 for the status byte
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            self.irq.set_register(response[1])

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  irq register: 0x{:02X}".format(
                    self.irq.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_irq(self):
        if self.verbose:
            print("> write irq")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.IRQ_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        transfer_buffer = [command_byte, self.irq.get_register()]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  irq register: 0x{:02X}".format(
                    self.irq.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # mux register api

    def read_mux(self):
        if self.verbose:
            print("> read mux")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.MUX_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 1  # 1 for the status byte
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            self.mux.set_register(response[1])

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  mux register: 0x{:02X}".format(
                    self.mux.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_mux(self):
        if self.verbose:
            print("> write mux")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.MUX_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        transfer_buffer = [command_byte, self.mux.get_register()]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  mux register: 0x{:02X}".format(
                    self.mux.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # scan register api

    def read_scan(self):
        if self.verbose:
            print("> read scan")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.SCAN_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 3  # 3 for the scan register (24-bit)
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            scan_b23_b16 = response[1]
            scan_b15_b8 = response[2]
            scan_b7_b0 = response[3]
            scan_reg = (scan_b23_b16 << 16) + (scan_b15_b8 << 8) + scan_b7_b0
            self.scan.set_register(scan_reg)

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  scan register: 0x{:06X}".format(
                    self.scan.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_scan(self):
        if self.verbose:
            print("> write scan")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.SCAN_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        scan_reg = self.scan.get_register()
        scan_b23_b16 = (scan_reg & 0xFF0000) >> 16
        scan_b15_b8 = (scan_reg & 0x00FF00) >> 8
        scan_b7_b0 = scan_reg & 0x0000FF
        transfer_buffer = [command_byte, scan_b23_b16, scan_b15_b8, scan_b7_b0]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  scan register: 0x{:06X}".format(
                    self.scan.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # timer register api

    def read_timer(self):
        if self.verbose:
            print("> read timer")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.TIMER_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 3  # 3 for the timer register (24-bit)
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            timer_b23_b16 = response[1]
            timer_b15_b8 = response[2]
            timer_b7_b0 = response[3]
            timer_reg = (timer_b23_b16 << 16) + \
                (timer_b15_b8 << 8) + timer_b7_b0
            self.timer.set_register(timer_reg)

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  timer register: 0x{:06X}".format(
                    self.timer.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_timer(self):
        if self.verbose:
            print("> write timer")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.TIMER_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        timer_reg = self.timer.get_register()
        timer_b23_b16 = (timer_reg & 0xFF0000) >> 16
        timer_b15_b8 = (timer_reg & 0x00FF00) >> 8
        timer_b7_b0 = timer_reg & 0x0000FF
        transfer_buffer = [command_byte,
                           timer_b23_b16, timer_b15_b8, timer_b7_b0]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  timer register: 0x{:06X}".format(
                    self.timer.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # offsetcal register api

    def read_offsetcal(self):
        if self.verbose:
            print("> read offsetcal")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.OFFSETCAL_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 3  # 3 for the timer register (24-bit)
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            offsetcal_b23_b16 = response[1]
            offsetcal_b15_b8 = response[2]
            offsetcal_b7_b0 = response[3]
            offsetcal_reg = (offsetcal_b23_b16 << 16) + \
                (offsetcal_b15_b8 << 8) + offsetcal_b7_b0
            self.offsetcal.set_register(offsetcal_reg)

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  offsetcal register: 0x{:06X}".format(
                    self.offsetcal.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_offsetcal(self):
        if self.verbose:
            print("> write offsetcal")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.OFFSETCAL_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        offsetcal_reg = self.offsetcal.get_register()
        offsetcal_b23_b16 = (offsetcal_reg & 0xFF0000) >> 16
        offsetcal_b15_b8 = (offsetcal_reg & 0x00FF00) >> 8
        offsetcal_b7_b0 = offsetcal_reg & 0x0000FF
        transfer_buffer = [command_byte, offsetcal_b23_b16,
                           offsetcal_b15_b8, offsetcal_b7_b0]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  offsetcal register: 0x{:06X}".format(
                    self.offsetcal.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # gaincal register api

    def read_gaincal(self):
        if self.verbose:
            print("> read gaincal")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.GAINCAL_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 3  # 3 for the timer register (24-bit)
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            gaincal_b23_b16 = response[1]
            gaincal_b15_b8 = response[2]
            gaincal_b7_b0 = response[3]
            gaincal_reg = (gaincal_b23_b16 << 16) + \
                (gaincal_b15_b8 << 8) + gaincal_b7_b0
            self.gaincal.set_register(gaincal_reg)

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  gaincal register: 0x{:06X}".format(
                    self.gaincal.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def write_gaincal(self):
        if self.verbose:
            print("> write gaincal")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.GAINCAL_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        gaincal_reg = self.gaincal.get_register()
        gaincal_b23_b16 = (gaincal_reg & 0xFF0000) >> 16
        gaincal_b15_b8 = (gaincal_reg & 0x00FF00) >> 8
        gaincal_b7_b0 = gaincal_reg & 0x0000FF
        transfer_buffer = [command_byte, gaincal_b23_b16,
                           gaincal_b15_b8, gaincal_b7_b0]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  gaincal register: 0x{:06X}".format(
                    self.gaincal.get_register()))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def read_lock(self):
        if self.verbose:
            print("> read lock")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.LOCK_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 1  # 1 for the status byte
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]
            lock_register = response[1]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  lock register: 0x{:02X}".format(lock_register))
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def lock_register_map_write_access(self):
        if self.verbose:
            print("> lock register map write access")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.LOCK_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        transfer_buffer = [command_byte, self.LOCK_PASS]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  register map write access lock enabled")
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    #

    def unlock_register_map_write_access(self):
        if self.verbose:
            print("> unlock register map write access")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.LOCK_ADDR << 2) + self.INCREMENTAL_WRITE_CMD

        # spi communication
        transfer_buffer = [command_byte, self.UNLOCK_PASS]
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  register map write access lock disabled")
        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))

    # crccfg register api

    def read_crccfg(self):
        if self.verbose:
            print("> read crccfg")

        # build command byte
        command_byte = (self.DEVICE_ADDR << 6) + \
            (self.CRCCFG_ADDR << 2) + self.STATIC_READ_CMD

        # spi communication
        transfer_buffer = [command_byte]
        additional_bytes = 2  # 2 for the crccfg register (16-bit)
        for _ in range(additional_bytes):
            transfer_buffer.append(0x00)
        response = self.spi.transfer(transfer_buffer)

        # unpack response
        if len(response) == len(transfer_buffer):
            self.status_byte = response[0]

            crccfg_b15_b8 = response[1]
            crccfg_b7_b0 = response[2]
            crccfg_reg = (crccfg_b15_b8 << 8) + crccfg_b7_b0
            self.crccfg.set_register(crccfg_reg)

            if self.verbose:
                print("  status byte: 0x{:02X}".format(self.status_byte))
                print("  crccfg register: 0x{:04X}".format(
                    self.crccfg.get_register()))

        else:
            raise Exception("Expected response length: {}. Actual response length: {}".format(
                len(transfer_buffer), len(response)))


# main
if __name__ == "__main__":
    adc = MCP346xR(rpicm4.SPI.DEV0_CS0)

    adc.mux.set_mux_vin_p(0b1111)
    adc.write_mux()
    adc.read_mux()

    adc.conversion_start_restart_fast_command()
    adc.read_adcdata()
