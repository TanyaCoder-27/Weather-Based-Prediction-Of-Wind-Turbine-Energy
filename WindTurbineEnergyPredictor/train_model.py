# Import Libraries
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load Dataset
df = pd.read_csv("data/info.csv")

# Rename columns
df.rename(columns={
    'Date/Time': 'Time',
    'LV ActivePower (kW)': 'ActivePower',
    'Wind Speed (m/s)': 'WindSpeed',
    'Theoretical_Power_Curve (KWh)': 'TheoreticalPower'
}, inplace=True)

# Drop only Time
df.drop(['Time'], axis=1, inplace=True)

# Remove nulls
df = df.dropna()

# Feature Engineering
df['WindSpeed_Cubed'] = df['WindSpeed'] ** 3

# Define Features
X = df[['WindSpeed', 'WindSpeed_Cubed', 'Wind Direction (°)']]
y = df['ActivePower']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Train Improved Model
model = RandomForestRegressor(
    n_estimators=400,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=0,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# Plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Power (kW)")
plt.ylabel("Predicted Power (kW)")
plt.title("Actual vs Predicted Power Output")
plt.show()

# Save Model
joblib.dump(model, "power_prediction.sav")
print("Model Saved Successfully!")