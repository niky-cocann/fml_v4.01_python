# imports
import spi
import rpicm4
import warnings
from enum import Enum

warnings.filterwarnings("ignore", category=DeprecationWarning)


#
class Display:
	"""7-segment Dispaly"""

	ALPHABET = "0123456789ljJK"
	NO_OF_DIGITS = 5
	INTENSITY_STEPS = 16

	# address
	ADDR_DIGIT0 = 0
	ADDR_DIGIT1 = 1
	ADDR_DIGIT2 = 2
	ADDR_DIGIT3 = 3
	ADDR_DIGIT4 = 4

	# intensity
	INTENSITY_0_PER_16 = 0
	INTENSITY_1_PER_16 = 1
	INTENSITY_2_PER_16 = 2
	INTENSITY_3_PER_16 = 3
	INTENSITY_4_PER_16 = 4
	INTENSITY_5_PER_16 = 5
	INTENSITY_6_PER_16 = 6
	INTENSITY_7_PER_16 = 7
	INTENSITY_8_PER_16 = 8
	INTENSITY_9_PER_16 = 9
	INTENSITY_10_PER_16 = 10
	INTENSITY_11_PER_16 = 11
	INTENSITY_12_PER_16 = 12
	INTENSITY_13_PER_16 = 13
	INTENSITY_14_PER_16 = 14
	INTENSITY_15_PER_16 = 15

	# decimal point
	DP_OFF = 0
	DP_ON = 1

	#
	def __init__(self, spi_instance, spi_mode=spi.SPI.MODE_0, spi_bits_per_word=8, spi_speed=500000):
		# spi
		self.spi = spi.SPI(spi_instance)
		self.spi.mode = spi_mode
		self.spi.bits_per_word = spi_bits_per_word
		self.spi_speed = spi_speed

		# log level
		self.verbose = True

	#
	def set_value(self, display_value):
		assert display_value <= self.NO_OF_DIGITS, "The value you are trying to set is too long!"

	#
	def set_digit(self, address, intensity, dp, ascii):
		assert address < self.NO_OF_DIGITS, "You are trying to set an unexisting digit (min address: 0, max address: {})".format(self.no_of_digits-1)
		assert intensity < self.INTENSITY_STEPS, "Max intensity: {}".format(self.INTENSITY_STEPS-1)

		command = (address << 4) + intensity
		data = (dp << 7) + ord(ascii)

		msg = [data, command]

		response = self.spi.transfer(msg)


#
if __name__ == "__main__":
	display = Display(rpicm4.SPI.DEV1_CS0)

	display.set_digit(display.ADDR_DIGIT3, display.INTENSITY_1_PER_16, display.DP_OFF, '6')
	display.set_digit(display.ADDR_DIGIT1, display.INTENSITY_15_PER_16, display.DP_OFF, '2')
	display.set_digit(display.ADDR_DIGIT0, display.INTENSITY_8_PER_16, display.DP_OFF, 'J')
