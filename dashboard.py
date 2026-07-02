import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create month and year columns
df['Month'] = df['Order Date'].dt.month_name()
df['Year'] = df['Order Date'].dt.year

# Calculate statistics
total_Sales = df['Sales'].sum()
avg_Sales = df['Sales'].mean()
total_revenue = df['Sales'].sum()

# Monthly Sales
monthly_Sales = df.groupby('Month')['Sales'].sum()

# Yearly Sales
yearly_Sales = df.groupby('Year')['Sales'].sum()

# Create dashboard
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Total Sales
axs[0,0].text(0.5, 0.6, f'Total Sales\n${total_Sales:,.0f}',
              fontsize=18, ha='center')
axs[0,0].axis('off')


axs[0,1].text(
    0.5, 0.5,
    f'Total Revenue\n${total_revenue:,.0f}\n\nAverage Sale\n${avg_Sales:.2f}',
    fontsize=14,
    ha='center'
)

axs[0,1].axis('off')
axs[0,1].set_title('Key Metrics')


# Monthly Sales chart
monthly_Sales.plot(kind='bar', ax=axs[1,0])
axs[1,0].set_title('Monthly Sales')

# Yearly Sales chart
yearly_Sales.plot(kind='bar', ax=axs[1,1])
axs[1,1].set_title('Yearly Revenue')

plt.suptitle('Sales & Demand Forecasting Dashboard', fontsize=18)
plt.tight_layout()

# Save dashboard
plt.savefig('Sales_dashboard.png')

# Show dashboard
plt.show()