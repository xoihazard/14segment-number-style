import time
import fourletterphat
from fourletterphat.alphanum4 import DIGIT_VALUES

# Override bitmask definitions:
DIGIT_VALUES["0"] = 0b0000000011011100
DIGIT_VALUES["1"] = 0b0000010000000110
DIGIT_VALUES["2"] = 0b0000100010001011
DIGIT_VALUES["3"] = 0b0000010011001101
DIGIT_VALUES["4"] = 0b0000000110000110
DIGIT_VALUES["5"] = 0b0000000110001101
DIGIT_VALUES["6"] = 0b0000010011011100
DIGIT_VALUES["7"] = 0b0001010000000001
DIGIT_VALUES["8"] = 0b0000000111011111
DIGIT_VALUES["9"] = 0b0000100011100011

def show_clock():
    str_time = time.strftime("%H%M")

    fourletterphat.clear()
    fourletterphat.print_str(str_time)
    fourletterphat.set_decimal(1, int(time.time() % 2))
    fourletterphat.show()

while True:
    fourletterphat.set_brightness(15)
    show_clock()
    time.sleep(0.1)