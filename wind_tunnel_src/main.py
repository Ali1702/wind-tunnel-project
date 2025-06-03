from load_cells import get_lift_and_drag
from servo_control import set_angle
from pressure_sensor import get_velocity
from data_visualization import log_data, visualize_data
import time

if __name__ == "__main__":
    try:
        print("Starting experiment for 1/2 minute...")
        
        # optional
        fixed_angle = 90
        #set_angle(fixed_angle)
        #print(f"Servo set to {fixed_angle}°")

        start_time = time.time()
        duration = 30  # seconds

        while time.time() - start_time < duration:
            elapsed = time.time() - start_time

            lift, drag = get_lift_and_drag()
            pressure, velocity = get_velocity()

            log_data(elapsed, lift, drag, velocity, pressure)

            # simple console feedback
            print(
                f"t = {elapsed:5.1f}s | "
                f"Lift: {lift:7.2f} g | Drag: {drag:7.2f} g | "
                f"Velocity: {velocity:7.3f} m/s | Pressure: {pressure:7.3f} kPa"
            )

            time.sleep(1)  # wait 1 second 

        print("1/2-minute acquisition complete. Visualizing data...")
        visualize_data()

    except KeyboardInterrupt:
        print("\nExperiment interrupted!")

    finally:
        print("Program exiting.")
