import pandas as pd

# Step 1: Read the dataset
print("Step 1: Reading the dataset...")
file_path = "C:/users/matias/desktop/sales_etl_pipeline/2_data/smartphone_sales.csv"
data = pd.read_csv(file_path)

# Step 2: Drop unnecessary columns
print("Step 2: Dropping unnecessary columns...")
columns_to_drop = ["Camera", "Mobile"]
data = data.drop(columns=columns_to_drop)

# Step 3: Fill missing values
print("Step 3: Filling missing values...")
data["Memory"] = data["Memory"].fillna("Unknown")
data["Storage"] = data["Storage"].fillna("Unknown")
data["Rating"] = data["Rating"].fillna(data["Rating"].mean())

# Step 4: Remove duplicate rows
print("Step 4: Removing duplicate rows...")
data = data.drop_duplicates()

# Step 5: Save cleaned data
print("Step 5: Saving cleaned data...")
data.to_csv("C:/users/matias/desktop/sales_etl_pipeline/2_data/cleaned_smartphone_sales.csv", index=False)

print("Data cleaning process completed.")