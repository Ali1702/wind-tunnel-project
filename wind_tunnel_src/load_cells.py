from hx711py.hx711 import HX711
import time

class LoadCell:
    def __init__(self, dout_pin, sck_pin, reference_unit):
        self.hx = HX711(dout_pin, sck_pin)
        self.hx.set_reading_format("MSB", "MSB")
        self.hx.set_reference_unit(reference_unit)
        self.hx.reset()
        self.hx.tare()  

    def get_weight(self):
        weight = self.hx.get_weight(5)
        self.hx.power_down()
        self.hx.power_up()
        return weight

lift_cell = LoadCell(dout_pin=17, sck_pin=22, reference_unit=-387.08)  
drag_cell = LoadCell(dout_pin=27, sck_pin=23, reference_unit=-403.64)  

def get_lift_and_drag():
    lift = lift_cell.get_weight()
    drag = drag_cell.get_weight()
    return lift, drag

if __name__ == "__main__":
    while True:
        lift, drag = get_lift_and_drag()
        print(f"Lift = {lift:.2f} g\tDrag = {drag:.2f} g")
        time.sleep(0.5)  