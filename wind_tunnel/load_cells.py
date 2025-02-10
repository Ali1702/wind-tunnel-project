from hx711 import HX711
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

lift_cell = LoadCell(dout_pin=11, sck_pin=15, reference_unit=1.47)  # replace with your reference unit
drag_cell = LoadCell(dout_pin=13, sck_pin=16, reference_unit=-3.7)  # replace with your reference unit

def get_lift_and_drag():
    lift = lift_cell.get_weight()
    drag = drag_cell.get_weight()
    return lift, drag
