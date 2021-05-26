from distutils.util import strtobool as strtobool
import getopt
import spidev
import sys
import time

def main(argv):
	address = None
	intensity = None
	decimal_point = False
	ascii = None

	try:
		opts, args = getopt.getopt(argv, "h", ["help", "address=", "intensity=", "decimal-point", "ascii="])
	except getopt.GetoptError:
		print("spicom.py --address <address> --intensity <intensity> --ascii <ascii>")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print("spicom.py --address <address> --intensity <intensity> --ascii <ascii>")
			sys.exit()
		elif opt == "--address":
			if arg.isnumeric and 0 <= int(arg) and int(arg) < 16:
				address = int(arg)
			else:
				print("address must be part of [0, 15] interval")
				sys.exit()
		elif opt == "--intensity":
			if arg.isnumeric and 0 <= int(arg) and int(arg) < 16:
                                intensity = int(arg)
			else:
                                print("intensity must be part of [0, 15] interval")
                                sys.exit()
		elif opt == "--decimal-point":
			if arg not in (None, ''):
				if bool(strtobool(arg)) is True or bool(strtobool(arg)) is False:
        	                        decimal_point = strtobool(arg)
				else:
                        	        print("decimal-point must be a boolean [True|False]")
                                	sys.exit()
		elif opt == "--ascii":
			if arg.isnumeric and 0 <= int(arg) and int(arg) < 128:
                                ascii = int(arg)
			else:
                                print("ascii must be part of [0, 127] interval")
                                sys.exit()
	print("address = {}\nintensity = {}\ndecimal-point = {}\nascii = {}\n".format(address, intensity, decimal_point, ascii))

if __name__ == "__main__":
	main(sys.argv[1:])



'''
# use SPI1
bus = 1
# use CS0
device = 0

spi = spidev.SpiDev()
spi.open(bus, device)

spi.max_speed_hz = 500000
spi.mode = 0

msg = [0x30, 0x32]
print(format(msg[0], '08b'), format(msg[1], '08b'))
spi.xfer2(msg)
'''
