# Read serial output from Arduino and display a polar "radar" plot in real-time.
# Requirements:
#   pip install pyserial matplotlib numpy

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
import time

# ====== CONFIG ======
SERIAL_PORT = 'COM3'   # <- change to your serial port, e.g. '/dev/ttyUSB0'
BAUD_RATE = 9600
MAX_DISTANCE_CM = 200   # radial limit shown on the plot
READ_TIMEOUT = 1.0
# =====================

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=READ_TIMEOUT)
    time.sleep(2)  # wait for Arduino reset
except Exception as e:
    print("Cannot open serial port:", e)
    print("Edit SERIAL_PORT in the script and try again.")
    sys.exit(1)

angles = []
distances = []

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location('N')   # 0 degrees at top
ax.set_theta_direction(-1)        # clockwise
ax.set_rlim(0, MAX_DISTANCE_CM)
scat = ax.scatter([], [])

plt.title("Radar Scanner (real-time)")

def parse_line(line):
    # Expect lines like: Angle: 45 Distance: 23.5 cm
    line = line.strip()
    if not line:
        return None
    try:
        parts = line.split()
        if len(parts) >= 4 and parts[0].startswith("Angle"):
            angle = float(parts[1])
            # find 'Distance:' token index
            if "Distance:" in parts:
                idx = parts.index("Distance:")
                dist_str = parts[idx+1]
            else:
                dist_str = parts[3]
            distance = float(dist_str)
            if distance < 0:
                return None
            return (np.deg2rad(angle), distance)
    except Exception:
        return None
    return None

# Keep a buffer for the current sweep
sweep_points = []

def update(frame):
    global sweep_points
    # read available lines (may be multiple per animation frame)
    try:
        while ser.in_waiting:
            raw = ser.readline().decode(errors='ignore').strip()
            parsed = parse_line(raw)
            if parsed:
                sweep_points.append(parsed)
    except Exception:
        pass

    if not sweep_points:
        return scat,

    # For smoother display, take the last N points
    pts = np.array(sweep_points[-500:])  # limit points
    thetas = pts[:,0]
    rs = pts[:,1]
    scat.set_offsets(np.c_[thetas, rs])
    scat.set_sizes(np.clip(2000/ (rs+1), 2, 60))  # marker size based on distance

    # Optionally clear buffer when we see angles near 0 (a new sweep)
    # If last angle is < 5 degrees, consider it a new sweep and keep points
    if len(thetas) and (np.rad2deg(thetas[-1]) < 5):
        # keep last sweep only
        sweep_points = sweep_points[-500:]
    return scat,

ani = animation.FuncAnimation(fig, update, interval=100, blit=True)
plt.show()
