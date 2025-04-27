# Import Required Python Libraries
import pandas as pd
import numpy as np

# Input: Number of Rows
num_rows = int(input("Enter the number of rows for orders: "))

# Create a series of random dates between 2014-01-01 and 2025-04-16
random_dates = np.random.choice(np.arange(np.datetime64("2014-01-01"),np.datetime64("2025-04-19")),size=num_rows)

# Format dates as 'YYYYMMDD' strings
formatted_dates = pd.to_datetime(random_dates).strftime('%Y%m%d')

# Create Base Data Columns
data = {
    'DateID': formatted_dates,
    'ProductID': np.random.randint(1, 1001, size=num_rows),    # Random IDs from 1 to 1000
    'StoreID': np.random.randint(1, 101, size=num_rows),       # Random IDs from 1 to 100
    'CustomerID': np.random.randint(1, 1001, size=num_rows),   # Random IDs from 1 to 1000
    'QuantityOrdered': np.random.randint(1, 21, size=num_rows),# Random quantities from 1 to 20
    'OrderAmount': np.random.randint(100, 1001, size=num_rows) # Random amounts from ₹100 to ₹1000
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Generate random discount % and shipping cost %
discount_perc = np.random.uniform(0.02, 0.15, size=num_rows)   # 2% to 15%
shipping_perc = np.random.uniform(0.05, 0.15, size=num_rows)   # 5% to 15%

# Apply calculations
df['DiscountAmount'] = df['OrderAmount'] * discount_perc
df['Shipping Cost'] = df['OrderAmount'] * shipping_perc
df['TotalAmount'] = df['OrderAmount'] - (df['DiscountAmount'] + df['Shipping Cost'])

# Save to CSV File
df.to_csv("DimFactOrders.csv", index=False)

print("DimFactOrders.csv generated successfully!")