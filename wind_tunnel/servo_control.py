import RPi.GPIO as GPIO
from time import sleep
import keyboard 

GPIO.setmode(GPIO.BCM)
servo_pin = 18 
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

angle = 0

def set_angle(angle):
    duty = 2 + (angle / 18) 
    GPIO.output(servo_pin, True)
    servo.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(servo_pin, False)
    servo.ChangeDutyCycle(0)

def control_servo():
    global angle
    try:
        print("Use 'a' to decrease angle and 'd' to increase angle. Press 'q' to quit.")
        while True:
            if keyboard.is_pressed('a'):  # decrease angle
                angle = max(angle - 5, 0)  # minimum angle is 0
                set_angle(angle)
                print(f"Angle: {angle}°")
                sleep(0.2)  
            elif keyboard.is_pressed('d'):  # increase angle
                angle = min(angle + 5, 90)  # maximum angle is 90
                set_angle(angle)
                print(f"Angle: {angle}°")
                sleep(0.2)
            elif keyboard.is_pressed('q'): 
                break
    except KeyboardInterrupt:
        print("Exiting servo control...")
        GPIO.cleanup()

if __name__ == "__main__":
    control_servo()
