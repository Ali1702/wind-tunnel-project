import spidev
import math
import time

V_0 = 5.0               # supply voltage to pressure sensor
rho = 1.204             # density of air (kg/m^3)
offset_size = 10        # number of samples for calculating offset
veloc_mean_size = 20    # number of samples for averaging velocity
zero_span = 2           # tolerance for zero velocity

spi = spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz = 1350000  

def read_adc(channel):
    if channel < 0 or channel > 7:
        raise ValueError("ADC channel must be between 0 and 7")
    adc = spi.xfer2([1, (8 + channel) << 4, 0])  
    data = ((adc[1] & 3) << 8) + adc[2]  # combine response bits into a value
    return data

offset = 0
for _ in range(offset_size):
    offset += read_adc(0) - (1023 / 2)
    time.sleep(0.01)  
offset /= offset_size  

try:
    while True:
        adc_avg = 0

        # reduce noise from adc
        for _ in range(veloc_mean_size):
            adc_avg += read_adc(0) - offset
            time.sleep(0.01)
        adc_avg /= veloc_mean_size

        voltage = (adc_avg + offset) / 1023.0 * V_0  

        pressure = (voltage - 2.5) / 0.2  # sensor-specific formula

        if 512 - zero_span < adc_avg < 512 + zero_span:
            velocity = 0  
        else:
            if adc_avg < 512:  # negative velocity 
                velocity = -math.sqrt((-10000.0 * ((adc_avg / 1023.0) - 0.5)) / rho)
            else:  # positive velocity 
                velocity = math.sqrt((10000.0 * ((adc_avg / 1023.0) - 0.5)) / rho)

        print(f"ADC: {adc_avg:.2f}, Voltage: {voltage:.2f} V, Pressure: {pressure:.2f} kPa, Velocity: {velocity:.2f} m/s")
        time.sleep(0.1)  

except KeyboardInterrupt:
    spi.close()  
