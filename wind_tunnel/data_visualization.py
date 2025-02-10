import matplotlib.pyplot as plt # type: ignore

data = {"angle": [], "lift": [], "drag": [], "velocity": []}

def log_data(angle, lift, drag, velocity):
    data["angle"].append(angle)
    data["lift"].append(lift)
    data["drag"].append(drag)
    data["velocity"].append(velocity)
    print(f"Logged: Angle={angle}°, Lift={lift:.2f} g, Drag={drag:.2f} g, Velocity={velocity:.2f} m/s")

def visualize_data():
    plt.figure(figsize=(12, 6))
    
    # lift and drag vs. angle
    plt.subplot(1, 2, 1)
    plt.plot(data["angle"], data["lift"], label="Lift (g)", marker="o")
    plt.plot(data["angle"], data["drag"], label="Drag (g)", marker="o")
    plt.xlabel("Angle of Attack (°)")
    plt.ylabel("Force (g)")
    plt.title("Lift and Drag vs. Angle of Attack")
    plt.legend()
    plt.grid(True)

    # velocity vs. angle
    plt.subplot(1, 2, 2)
    plt.plot(data["angle"], data["velocity"], label="Velocity (m/s)", color="green", marker="o")
    plt.xlabel("Angle of Attack (°)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Velocity vs. Angle of Attack")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
