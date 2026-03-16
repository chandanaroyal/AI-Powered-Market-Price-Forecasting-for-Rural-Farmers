# 🌾AI-Powered Market Price Forecasting for Rural Farmers
An AI-driven agricultural commodity price forecasting system that predicts market prices using BiLSTM deep learning and sentiment analysis. The system provides insights through an interactive Streamlit dashboard to help farmers and analysts understand price trends and make better market decisions.

## 📌 Project Overview
Agricultural commodity prices fluctuate due to factors such as:

Seasonal demand

Weather conditions

Supply variations

Public market sentiment

Farmers often lack tools to analyze these changes effectively. This project introduces an AI-powered forecasting system that integrates historical price data and sentiment analysis to predict future commodity prices.

The results are visualized through an interactive dashboard, enabling users to explore price trends, volatility, and AI-based recommendations.

## 🎯 Problem Statement
Agricultural markets are highly dynamic and unpredictable. Farmers often rely on local market assumptions or intermediaries when deciding the right time to sell their produce. Traditional prediction systems focus mainly on historical price data and ignore important factors like public sentiment or market behavior, resulting in less accurate predictions.

Therefore, an intelligent system is required that can combine historical market data with sentiment indicators to provide reliable price predictions and actionable insights.

## ✨ Key Features
## 🌱 AI-Based Price Prediction using BiLSTM 📊 Interactive Data Visualization using Plotly 📍 Location-based commodity filtering 📈 Price trend analysis 💬 Sentiment analysis integration ⚡ Market volatility insights 🤖 AI advisory recommendations (Buy / Hold / Sell) 📉 Price change monitoring

## 📂 Dataset Description
The dataset used in this project contains agricultural commodity market information with the following attributes:

Column Description commodity Name of the agricultural commodity

date Date of the record

unit Measurement unit

minimum Minimum market price

maximum Maximum market price

average Average commodity price

season Seasonal category

public_sentiment Public market sentiment

sentiment_score Numerical sentiment score

price_change Change in price trend

location District or market location

## 🧰 Technologies Used
## 💻 Programming Language
Python

## 🤖 Machine Learning & AI

TensorFlow Keras Scikit-learn

## 📊 Data Processing

Pandas NumPy

## 📉 Visualization

Plotly Folium

## 🌐 Dashboard Framework

Streamlit

🛠 Development Tools

Visual Studio Code GitHub
'''bash
## 📁 Project Structure
AI-Powered-Market-Price-Forecasting-For-Rural-Farmers
│ ├── src │ 
├── app.py │
├── train_bilstm.py │ 
├── data │ 
└── finalcapdata_india_all_districts.csv │ 
├── docs │
└── project_documentation │ 
├── architecture.png
├── requirements.txt 
├── README.md 
└── setup_instructions.md

## ⚙ Installation Guide
## 1️⃣ Clone the Repository git clone https://github.com/MBKavyasree/AI-Powered-Market-Price-Forecasting-For-Rural-Farmers.git

## 2️⃣ Navigate to Project Folder
cd AI-Powered-Market-Price-Forecasting-For-Rural-Farmers

## 3️⃣ Install Required Libraries
pip install -r requirements.txt

## 4️⃣ Run the Streamlit Dashboard
streamlit run src/app.py

# 📊 Results
The system successfully predicts agricultural commodity prices using the BiLSTM deep learning model trained on historical data. The integration of sentiment indicators improves prediction reliability.

The Streamlit dashboard provides insights through interactive charts, sentiment analysis graphs, and price trend visualizations.
