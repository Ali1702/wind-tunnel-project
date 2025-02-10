from load_cells import get_lift_and_drag
from servo_control import set_angle, control_servo, angle
from pressure_sensor import get_velocity
from data_visualization import log_data, visualize_data
import time

if __name__ == "__main__":
    try:
        print("Starting experiment...")
        for current_angle in range(0, 91, 10):  # measure from 0° to 90° in 10° increments
            set_angle(current_angle)
            time.sleep(2)  # Wait for airflow to stabilize

            lift, drag = get_lift_and_drag()
            velocity = get_velocity()
            log_data(current_angle, lift, drag, velocity)

        print("Experiment complete. Visualizing data...")
        visualize_data()

    except KeyboardInterrupt:
        print("Experiment interrupted!")
