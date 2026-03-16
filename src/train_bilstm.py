import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Bidirectional

# Load dataset
df = pd.read_csv("data/finalcapdata_india_all_districts.csv")

# Use correct column
prices = df["average"].values.reshape(-1,1)

# Scaling
scaler = MinMaxScaler()
scaled_prices = scaler.fit_transform(prices)

# Create sequences
X, y = [], []
seq_length = 10

for i in range(seq_length, len(scaled_prices)):
    X.append(scaled_prices[i-seq_length:i])
    y.append(scaled_prices[i])

X, y = np.array(X), np.array(y)

# Build BiLSTM Model
model = Sequential()
model.add(Bidirectional(LSTM(50, return_sequences=True), input_shape=(X.shape[1],1)))
model.add(Bidirectional(LSTM(50)))
model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

# Train
model.fit(X, y, epochs=10, batch_size=32)

# Save model
model.save("bilstm_model.keras ")
joblib.dump(scaler, "scaler.pkl")

print("Training completed. Model saved.")
