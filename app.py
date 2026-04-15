from flask import Flask, request, jsonify, send_file
import random

app = Flask(__name__)

# ===== AI + CYBERSECURITY LOGIC =====
def analyze_system(vibration, sound, temperature, rpm, network_delay):

    # ===== AI PREDICTION =====
    if vibration == 1 or sound > 600 or temperature > 50:
        prediction = " Anomaly Detected"
    else:
        prediction = " Normal"

    # ===== CYBERSECURITY ANALYSIS =====
    cyber_alerts = []

    # Sensor spoofing (RPM mismatch)
    if rpm < 300 and vibration == 1:
        cyber_alerts.append(" Possible Sensor Spoofing (RPM mismatch)")

    # MITM attack (network delay)
    if network_delay > 80:
        cyber_alerts.append(" Possible MITM Attack (High Network Delay)")

    # System tampering
    if temperature > 60 and sound < 200:
        cyber_alerts.append(" Possible System Tampering")

    if len(cyber_alerts) == 0:
        cyber_result = " No cyber threat detected"
    else:
        cyber_result = " | ".join(cyber_alerts)

    return prediction, cyber_result


# ===== HOME =====
@app.route('/')
def home():
    return send_file("frontend.html")


# ===== MANUAL PREDICT =====
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    try:
        vibration = float(data["vibration"])
        sound = float(data["sound"])
        temperature = float(data["temperature"])
        rpm = float(data["rpm"])
        network_delay = float(data["network_delay"])
    except:
        return jsonify({"result": "Fill required fields correctly"})

    prediction, cyber = analyze_system(vibration, sound, temperature, rpm, network_delay)

    return jsonify({
        "prediction": prediction,
        "cyber": cyber
    })


# ===== AUTO SIMULATION =====
@app.route('/simulate')
def simulate():

    # Core sensors
    vibration = random.choice([0, 1])
    sound = random.randint(200, 800)
    temperature = random.randint(25, 70)

    # Extra parameters
    pressure = random.randint(1, 10)
    voltage = random.randint(200, 250)
    current = random.uniform(0.5, 5.0)
    rpm = random.randint(100, 2000)
    network_delay = random.randint(1, 120)
    device_id = random.randint(1, 5)
    humidity = random.randint(30, 80)

    prediction, cyber = analyze_system(vibration, sound, temperature, rpm, network_delay)

    return jsonify({
        "vibration": vibration,
        "temperature": temperature,
        "pressure": pressure,
        "voltage": voltage,
        "current": round(current, 2),
        "rpm": rpm,
        "network_delay": network_delay,
        "device_id": device_id,
        "sound": sound,
        "humidity": humidity,
        "prediction": prediction,
        "cyber": cyber
    })


if __name__ == '__main__':
    app.run(debug=True)