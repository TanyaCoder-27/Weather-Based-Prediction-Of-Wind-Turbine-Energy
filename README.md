# 🌬️ Weather-Based Prediction of Wind Turbine Energy Output

## 📌 Project Overview

This project is a Machine Learning-based web application that predicts wind turbine energy output using weather parameters such as wind speed and wind direction.

The system is trained on historical wind turbine data and deployed using a Flask web application. It also integrates the OpenWeather API to fetch real-time weather data for prediction support.

The trained model achieves an R² score of approximately **0.91**, indicating high prediction accuracy.

---

## 🎯 Objective

The main objective of this project is to:

- Predict wind turbine power output using weather parameters
- Integrate real-time weather data using API
- Demonstrate practical application of Machine Learning in renewable energy
- Build a deployable web-based energy forecasting system

---

## 🧠 Machine Learning Model

- Algorithm: Regression Model
- Model File: `power_prediction.sav`
- Evaluation Metric: R² Score
- Achieved R² Score: **0.91**

This means the model explains about 91% of the variance in turbine energy output.

---

## ⚙️ Features

- Wind energy prediction for 10-minute intervals
- Real-time weather data integration
- REST API endpoints
- Interactive web interface (HTML + CSS)
- Environment variable support using `.env`
- Clean project structure

---

## 📂 Project Structure

```bash
WindTurbineEnergyPredictor/
│
├── data/
│   └── info.csv
│
├── static/
│   ├── styles.css
│   └── wm.jpg
│
├── templates/
│   ├── index.html
│   └── output.html
│
├── .env
├── .gitignore
├── app.py
├── power_prediction.sav
├── train_model.py
├── wind_turbine_energy_prediction.py
└── README.md
```

---

## 🔌 API Endpoints

### 1️⃣ Predict Energy Output

**Endpoint:** `/predict`  
**Method:** POST  

**Request Body (JSON):**
```json
{
  "wind_speed": 5.6,
  "wind_direction": 267
}
```

**Response:**
```json
{
  "predicted_energy_kwh": 67.56
}
```

---

### 2️⃣ Get Weather Data

**Endpoint:** `/weather`  
**Method:** GET  

**Query Parameter Example:**

```
/weather?city=Delhi
```

**Response:**
```json
{
  "city": "Delhi",
  "temperature": 30,
  "humidity": 62,
  "pressure": 1008,
  "wind_speed": 4.8,
  "wind_direction": 250
}
```

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- OpenWeather API
- HTML
- CSS

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/TanyaCoder-27/Weather-Based-Prediction-Of-Wind-Turbine-Energy.git
cd Weather-Based-Prediction-Of-Wind-Turbine-Energy
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

(If requirements.txt is not available, install manually)

```bash
pip install flask pandas numpy scikit-learn requests python-dotenv
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📊 Model Training

To retrain the model:

```bash
python train_model.py
```

This will generate/update the `power_prediction.sav` file.

---

## 🌍 Applications

- Wind farm energy forecasting
- Renewable energy optimization
- Smart grid energy planning
- Academic research in sustainable energy systems

---

## 🔮 Future Improvements

- Add LSTM model for time-series forecasting
- Add data visualization dashboard
- Deploy on cloud (AWS / Azure / Render)
- Add multiple turbine prediction support
- Improve feature engineering

---

## 📂 Project Demo

You can view the complete project demo:

🔗 [Click Here to View on Google Drive](https://drive.google.com/file/d/10CA2H_psp2Wf66pTdh6i-GOLNXWpD_VI/view?usp=sharing)

## 👩‍💻 Author

Tanya Coder  
Machine Learning & Renewable Energy Project  

GitHub Repository:
https://github.com/TanyaCoder-27/Weather-Based-Prediction-Of-Wind-Turbine-Energy

---
