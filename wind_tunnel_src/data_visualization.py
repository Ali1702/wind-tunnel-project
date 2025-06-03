import os
import matplotlib.pyplot as plt

data = {"time": [], "lift": [], "drag": [], "velocity": [], "pressure": []}

PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

def log_data(elapsed_time, lift, drag, velocity, pressure):
    data["time"].append(elapsed_time)
    data["lift"].append(lift)
    data["drag"].append(drag)
    data["velocity"].append(velocity)
    data["pressure"].append(pressure)

def visualize_data():
    plt.figure(figsize=(18, 6))

    # lift and drag vs. time
    plt.subplot(1, 3, 1)
    plt.plot(data["time"], data["lift"], label="Lift (g)", marker="o")
    plt.plot(data["time"], data["drag"], label="Drag (g)", marker="o")
    plt.xlabel("Elapsed Time (s)")
    plt.ylabel("Force (g)")
    plt.title("Lift and Drag vs. Time")
    plt.legend()
    plt.grid(True)

    # velocity vs. time
    plt.subplot(1, 3, 2)
    plt.plot(data["time"], data["velocity"], label="Velocity (m/s)", color="green", marker="o")
    plt.xlabel("Elapsed Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Velocity vs. Time")
    plt.legend()
    plt.grid(True)
    
    # pressure vs. time
    plt.subplot(1, 3, 3)
    plt.plot(data["time"], data["pressure"], label="Pressure (kPa)", color="orange", marker="o")
    plt.xlabel("Elapsed Time (s)")
    plt.ylabel("Pressure (kPa)")
    plt.title("Pressure vs. Time")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    save_path = os.path.join(PLOTS_DIR, "results.png")
    plt.savefig(save_path)
    print(f"Saved plot to: {save_path}")
