from flask import Flask, render_template, request
import joblib
import pandas as pd
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# ---------------- LOAD MODEL ----------------
model_path = os.path.join(os.path.dirname(__file__), "power_prediction.sav")
model = joblib.load(model_path)

# ---------------- LOAD API KEY ----------------
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# ---------------- CITY LIST ----------------
CITIES = [
    "Agartala", "Delhi", "Mumbai", "Chennai", "Bangalore",
    "Hyderabad", "Kolkata", "Ahmedabad", "Jaipur", "Pune",
    "London", "New York", "Los Angeles", "Chicago", "Toronto",
    "Berlin", "Amsterdam", "Sydney", "Tokyo", "Dubai"
]


@app.route("/")
def home():
    return render_template("index.html", cities=CITIES)


@app.route("/predict", methods=["GET", "POST"])
def predict():

    weather_data = None
    prediction = None

    if request.method == "POST":

        # ---------------- WEATHER SECTION ----------------
        if "city" in request.form:
            city = request.form.get("city")

            if city:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

                try:
                    response = requests.get(url)
                    data = response.json()

                    if response.status_code == 200 and "main" in data:
                        weather_data = {
                            "city": city,
                            "temperature": round(data["main"]["temp"], 2),
                            "humidity": data["main"]["humidity"],
                            "pressure": data["main"]["pressure"],
                            "wind_speed": data["wind"]["speed"]
                        }
                    else:
                        weather_data = {"city": city, "temperature": "Error"}

                except:
                    weather_data = {"city": city, "temperature": "API Error"}

        # ---------------- PREDICTION SECTION ----------------
        if "wind_speed" in request.form:

            try:
                wind_speed = float(request.form.get("wind_speed"))
                wind_direction = float(request.form.get("wind_direction"))

                # Feature engineering (must match training)
                wind_speed_cubed = wind_speed ** 3

                input_data = pd.DataFrame(
                    [[wind_speed, wind_speed_cubed, wind_direction]],
                    columns=["WindSpeed", "WindSpeed_Cubed", "Wind Direction (°)"]
                )

                # Predict power in kW
                predicted_power_kw = model.predict(input_data)[0]

                # Convert kW → kWh (10-minute interval)
                energy_kwh = predicted_power_kw * (10 / 60)

                prediction = round(energy_kwh, 2)

            except:
                prediction = "Invalid Input"

    return render_template(
        "output.html",
        cities=CITIES,
        weather_data=weather_data,
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)