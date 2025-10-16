# 🛰️ Mini Radar Tracking System

A **visual radar simulation** made using **Arduino + Python**.  
Detects objects via **ultrasonic sensor (HC-SR04)** and displays them on a live radar UI.

---

## ⚙️ Features
✅ Real-time object detection and distance tracking  
✅ Smooth radar sweep with servo motor rotation  
✅ Live radar visualization using Matplotlib  
✅ Works with Arduino UNO or Nano  

---

## 🧩 Hardware Required

| Component | Qty | Description |
|------------|-----|-------------|
| Arduino UNO R3 (Clone) | 1 | Main microcontroller board |
| HC-SR04 Ultrasonic Sensor | 1 | Measures distance |
| SG90 Servo Motor | 1 | Rotates the sensor |
| Jumper Wires | Several | For connections |
| USB Cable | 1 | To connect Arduino to PC |

> 💡 Optional: Use a mini breadboard for cleaner wiring.

---

## 🔌 Wiring Diagram

**HC-SR04 → Arduino**  
| HC-SR04 | Arduino |
|----------|----------|
| VCC | 5V |
| GND | GND |
| TRIG | D9 |
| ECHO | D10 |

**Servo → Arduino**  
| Servo | Arduino |
|--------|----------|
| VCC | 5V |
| GND | GND |
| Signal | D11 |

---

## 💻 Setup & Run

### 1️⃣ Arduino Side
1. Open `arduino/RadarTracker.ino` in **Arduino IDE**
2. Select your board and port
3. Upload the sketch

### 2️⃣ Python Side
1. Install dependencies:
   ```bash
   pip install pyserial matplotlib
   ```
2. Open `python/radar_display.py`  
   Update this line with your correct port:
   ```python
   ser = serial.Serial("COM3", 9600)  # for Windows
   # or /dev/ttyUSB0 for Linux/Mac
   ```
3. Run the radar:
   ```bash
   python radar_display.py
   ```

---

## 🖥️ Output Preview

🟢 Servo sweeps from **0° to 180°**  
🟢 Detected objects shown as **green arcs** on radar  
🟢 Real-time data updates with each scan

---

## 🧠 Tips
- Recommended range: 2–400 cm  
- Use external 5V if servo draws too much current  
- You can tweak scanning speed in Arduino code (delay value)

---

## 📜 License
**MIT License** — Free for educational and personal projects.

---

### 🌐 Created by: Mohammad Amin Foldae  
GitHub: [github.com/mamad1313fld](https://github.com/mamad1313fld)
