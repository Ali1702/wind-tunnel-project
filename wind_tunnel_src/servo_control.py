import RPi.GPIO as GPIO
from time import sleep
import sys
import select
import termios
import tty

# GPIO setup
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# create PWM at 50 Hz
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

def get_key_nonblocking():
    # returns a character from stdin if available; otherwise None.
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        return sys.stdin.read(1)
    return None

def control_servo():
    global angle
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        print("Use 'a' to decrease angle, 'd' to increase angle. Press 'q' to quit.")
        while True:
            key = get_key_nonblocking()
            if key == 'a':
                angle = max(angle - 5, 0)
                set_angle(angle)
                print(f"Angle: {angle}°")
                sleep(0.2)
            elif key == 'd':
                angle = min(angle + 5, 90)
                set_angle(angle)
                print(f"Angle: {angle}°")
                sleep(0.2)
            elif key == 'q':
                break
            # if no key pressed, continue without blocking
            sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        # restore terminal settings and clean up GPIO
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        GPIO.cleanup()
        print("Exiting servo control...")

if __name__ == "__main__":
    control_servo()
