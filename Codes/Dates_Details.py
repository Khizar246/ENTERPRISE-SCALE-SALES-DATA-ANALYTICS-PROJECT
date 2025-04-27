import pandas as pd

# Define Start and End Date
start_date = "2014-01-01"
end_date = "2027-12-31"

# Generate Date Range Between Start and End Date
date_range = pd.date_range(start=start_date, end=end_date)

# Create DataFrame from Date Range
date_dimension = pd.DataFrame(date_range, columns=["Date"])

# Add Date Attributes/Columns
date_dimension["DayOfWeek"] = date_dimension["Date"].dt.dayofweek  # Monday=0, Sunday=6
date_dimension["Month"] = date_dimension["Date"].dt.month
date_dimension["Quarter"] = date_dimension["Date"].dt.quarter
date_dimension["Year"] = date_dimension["Date"].dt.year
date_dimension["IsWeekend"] = date_dimension["DayOfWeek"].isin([5, 6])  # Saturday or Sunday
date_dimension["DateID"] = date_dimension["Date"].dt.strftime("%Y%m%d").astype(int)

# Reorder Columns: Make DateID the First Column
cols = ["DateID"] + [col for col in date_dimension.columns if col != "DateID"]
date_dimension = date_dimension[cols]

# Export to CSV (No Index Column)
date_dimension.to_csv("DimDate.csv", index=False)

print("DimDate.csv generated successfully.")