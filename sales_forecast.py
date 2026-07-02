import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Read the dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Group sales by date
sales = df.groupby('Order Date')['Sales'].sum().reset_index()

# Create day number
sales['Day'] = np.arange(len(sales))

# Train model
X = sales[['Day']]
y = sales['Sales']

model = LinearRegression()
model.fit(X, y)

# Predict sales
sales['Predicted Sales'] = model.predict(X)

# Plot graph
plt.figure(figsize=(12,6))
plt.plot(sales['Order Date'], sales['Sales'], label='Actual Sales')
plt.plot(sales['Order Date'], sales['Predicted Sales'], label='Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecasting')
plt.legend()
plt.show()