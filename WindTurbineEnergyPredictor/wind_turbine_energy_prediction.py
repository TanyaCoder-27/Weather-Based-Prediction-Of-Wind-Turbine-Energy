import joblib
import pandas as pd

# Load trained model
model = joblib.load("power_prediction.sav")

# Example inputs
wind_speed = 8.5
wind_direction = 180  # degrees

# Feature engineering (must match training)
wind_speed_cubed = wind_speed ** 3

# Create DataFrame
input_data = pd.DataFrame(
    [[wind_speed, wind_speed_cubed, wind_direction]],
    columns=["WindSpeed", "WindSpeed_Cubed", "Wind Direction (°)"]
)

# Predict power (kW)
predicted_power_kw = model.predict(input_data)[0]

# Convert to energy (kWh for 10 minutes)
energy_kwh = predicted_power_kw * (10 / 60)

print("Predicted Power Output (kW):", round(predicted_power_kw, 2))
print("Predicted Energy (kWh, 10 min):", round(energy_kwh, 2))