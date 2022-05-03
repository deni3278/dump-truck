from hx711 import HX711

pin_dt = 5
pin_sck = 6
hx: HX711

def initialize():
    global hx

    hx = HX711(dout_pin=pin_dt, pd_sck_pin=pin_sck)

    input("Clear the strain gauge of any weights and press enter to start calibrating.")

    err = hx.zero() # measure tare

    if err:
        print("An error has occurred while initializing the strain gauge.")
        quit()

def calibrate():
    input("Place a known weight on the gauge and press enter.")

    reading = hx.get_data_mean()
    known_weight: str
    grams: float

    valid = False

    while not valid:
        try:
            known_weight = input("Enter how many grams were placed on the gauge: ")
            grams = float(known_weight)

            valid = True
        except ValueError:
            print("Expected integer or float.")

            valid = False

    ratio = reading / grams
    hx.set_scale_ratio(ratio)

    print("Successfully calibrated the strain gauge.")

def measure():
    return hx.get_weight_mean()