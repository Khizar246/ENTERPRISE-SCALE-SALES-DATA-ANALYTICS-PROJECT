# Import Required Python Libraries
import pandas as pd
import numpy as np
import os

# Constants and Directory
DATE_ID = '20250420'  # Fixed date for this run
directory = r"C:\Users\khizer\Study_Material\Projects\DWBI_Project\Data\DailyStoreData"

# Loop Through Store IDs (1 to 100)
for store_id in range(1, 101):
    
    # Generate Random Row Count
    num_rows = np.random.randint(100, 1000)

    # Create Base Data Columns
    data = {
        'DateID': [DATE_ID] * num_rows,
        'ProductID': np.random.randint(1, 1001, size=num_rows),
        'StoreID': [store_id] * num_rows,
        'CustomerID': np.random.randint(1, 1001, size=num_rows),
        'QuantityOrdered': np.random.randint(1, 21, size=num_rows),
        'OrderAmount': np.random.randint(100, 1001, size=num_rows)
    }

    df = pd.DataFrame(data)

    # Calculate Derived Columns
    discount_perc = np.random.uniform(0.02, 0.15, size=num_rows)
    shipping_perc = np.random.uniform(0.05, 0.15, size=num_rows)

    df['DiscountAmount'] = df['OrderAmount'] * discount_perc
    df['Shipping Cost'] = df['OrderAmount'] * shipping_perc
    df['TotalAmount'] = df['OrderAmount'] - (df['DiscountAmount'] + df['Shipping Cost'])

    # Save to CSV File
    file_name = f"Store_{store_id}_{DATE_ID}.csv"
    file_path = os.path.join(directory, file_name)

    # Remove file if it already exists
    if os.path.exists(file_path):
        os.remove(file_path)

    # Save DataFrame to CSV without index column
    df.to_csv(file_path, index=False)

print("success")