# AI-Powered Smart Grid Digital Twin

A student prototype for monitoring low-voltage demonstration circuits using an ESP32, sensors, a Python AI model, and a Streamlit dashboard.

## Features
- Read voltage, current, and transformer temperature (after sensor calibration).
- Demonstrate Normal, Overload, and Fault states.
- Display local readings on an OLED and a browser dashboard.
- Train a baseline Random Forest classifier from labelled data.
- Extend the system to receive live ESP32 data over Wi-Fi.

## Hardware
- ESP32 DevKit
- ZMPT101B voltage sensor module
- ACS712 current sensor module
- DS18B20 temperature sensor
- I2C OLED (often address 0x3C)
- Two-channel relay module
- Three push buttons
- Isolated low-voltage demo supply and loads

## Repository layout
- `esp32-code/SmartGrid.ino`: Arduino starter firmware
- `ai-model/train_model.py`: train/evaluate/save a Random Forest model
- `ai-model/smart_grid_data.csv`: small illustrative example dataset
- `dashboard/app.py`: Streamlit demonstration dashboard
- `requirements.txt`: Python dependencies

## Quick start: dashboard
1. Install Python 3.10 or later.
2. From this repository folder, run `pip install -r requirements.txt`.
3. Run `streamlit run dashboard/app.py`.
4. Use the sidebar to simulate conditions. These values are simulated, not live hardware readings.

## Train the AI model
From the repository folder:
`python ai-model/train_model.py`
This creates `ai-model/smart_grid_model.joblib`. The included CSV is tiny and illustrative only; it is not suitable for real protection or credible accuracy claims. Collect a larger, correctly labelled dataset and evaluate it on separate test data.

## ESP32 firmware
Open `esp32-code/SmartGrid.ino` in Arduino IDE. Install Adafruit SSD1306, Adafruit GFX Library, OneWire, and DallasTemperature. Confirm your actual board/module pinouts before powering. Voltage and current conversion factors are placeholders and must be calibrated.

## Safety
- The 230 V AC primary is hazardous. Mains wiring must be enclosed and handled by a qualified electrician.
- Never connect mains voltage or an unconditioned sensor output directly to ESP32 GPIO.
- ESP32 analog inputs must stay within the board's permitted range (typically 0–3.3 V).
- ZMPT101B modules vary; confirm supply and input/output specifications.
- ACS712 boards commonly use 5 V; scale its output and verify the full waveform stays within the ESP32 ADC range.
- Use only isolated, low-voltage demo loads during development. Do not rely on this prototype or its AI output for real electrical protection.
