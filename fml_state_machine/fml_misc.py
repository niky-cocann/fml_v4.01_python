import fml_globals
import RPi.GPIO as GPIO
from statemachine import StateMachine, State
from fml_enums import FMLDisplayType
from fml_globals import config_params_dict, tank_params_dict

# classes
class FMLButton():
    def __init__(self, gpio_bcm_pin, inverted=False, debounce=False, debounce_counts=1):
        self.pin = gpio_bcm_pin
        self.inverted = inverted
        self.debounce = debounce
        if self.debounce is True:
            self.debounce_counts = debounce_counts
        else:
            self.debounce_counts = 1
        self.counter = 1

        # set gpio pin as input
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
                
        # set current and previous states
        self.prev_state = False
        self.curr_state = GPIO.input(self.pin)
        self.state = False
    
    def update_status(self):
        # read curent state
        self.curr_state = GPIO.input(self.pin)

        if self.prev_state==self.curr_state:
            if self.counter<self.debounce_counts:
                # increment counter
                self.counter += 1
            else:
                self.state = self.curr_state
        else:
            # update previous state
            self.prev_state = self.curr_state
            # reset counter
            self.counter = 1

        # return pin state
        if self.inverted:
            return not self.state
        else:
            return self.state

class FMLMachine(StateMachine):
    # states
    default = State("default", initial=True)
    prev_refill = State("previous refill")
    curr_refill = State("current refill")
    nozzle_fill = State("nozzle fill")

    # transitions - default to x
    default_to_prev_refill = default.to(prev_refill)
    default_to_curr_refill = default.to(curr_refill)
    default_to_nozzle_fill = default.to(nozzle_fill)

    # transitions - prev_refill to x
    prev_refill_to_default = prev_refill.to(default)

    # transitions - curr_refill to x
    curr_refill_to_default = curr_refill.to(default)

    # transitions - nozzle_fill to x
    nozzle_fill_to_default = nozzle_fill.to(default)

    # callbacks
    def on_default_to_prev_refill(self):
        print("default -> prev_refill")
        display_type = FMLDisplayType.PREVIOUS_REFILL
        print(f"display type: {display_type}")
    
    def on_default_to_curr_refill(self):
        print("default -> curr_refill")
        display_type = FMLDisplayType.CURRENT_REFILL
        print(f"display type: {display_type}")
    
    def on_default_to_nozzle_fill(self):
        print("default -> nozzle_fill")
        display_type = FMLDisplayType.NOZZLE_FILL
        print(f"display type: {display_type}")
    
    def on_prev_refill_to_default(self):
        print("prev_refill -> default")
        display_type = FMLDisplayType.TANK_LEVEL
        print(f"display type: {display_type}")
    
    def on_curr_refill_to_default(self):
        print("curr_refill -> default")
        display_type = FMLDisplayType.TANK_LEVEL
        print(f"display type: {display_type}")
    
    def on_nozzle_fill_to_default(self):
        print("nozzle_fill -> default")
        display_type = FMLDisplayType.TANK_LEVEL
        print(f"display type: {display_type}")

def adc_to_ohms(adc_value):
    return int(adc_value * fml_globals.adcu_to_ohm_factor)
