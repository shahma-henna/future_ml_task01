
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Calculate metrics
total_sales = df['Sales'].sum()
avg_sales = df['Sales'].mean()

# Monthly sales
monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

# Yearly sales
yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum()

# Category sales
category_sales = df.groupby('Category')['Sales'].sum()

# Region sales
region_sales = df.groupby('Region')['Sales'].sum()

# Create dashboard
fig, axs = plt.subplots(3, 2, figsize=(15, 12))

# Total Revenue
axs[0,0].text(
    0.5, 0.5,
    f'Total Revenue\n${total_sales:,.0f}',
    fontsize=18,
    ha='center'
)
axs[0,0].axis('off')
axs[0,0].set_title('Total Revenue')

# Average Sales
axs[0,1].text(
    0.5, 0.5,
    f'Average Sales\n${avg_sales:,.2f}',
    fontsize=18,
    ha='center'
)
axs[0,1].axis('off')
axs[0,1].set_title('Average Sales')

# Monthly Sales
axs[1,0].plot(monthly_sales.index, monthly_sales.values)
axs[1,0].set_title('Monthly Sales Trend')

# Yearly Revenue
axs[1,1].bar(yearly_sales.index.astype(str), yearly_sales.values)
axs[1,1].set_title('Yearly Revenue')

# Sales by Category
axs[2,0].bar(category_sales.index, category_sales.values)
axs[2,0].set_title('Sales by Category')

# Sales by Region
axs[2,1].pie(
    region_sales.values,
    labels=region_sales.index,
    autopct='%1.1f%%'
)
axs[2,1].set_title('Sales by Region')

plt.suptitle(
    'Sales & Demand Forecasting Dashboard',
    fontsize=20
)

plt.tight_layout()

# Save dashboard
plt.savefig('sales_dashboard.png')

# Show dashboard
plt.show()

plt.show()
