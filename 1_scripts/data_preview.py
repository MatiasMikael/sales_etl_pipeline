import pandas as pd

# Read the CSV file
file_path = "C:/users/matias/desktop/sales_etl_pipeline/2_data/smartphone_sales.csv" # Path to your CSV file
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display the first 5 rows
print("\nFirst 5 rows of the dataset:")
print(data.head())