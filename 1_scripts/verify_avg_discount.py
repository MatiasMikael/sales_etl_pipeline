import pandas as pd

# Step 1: Load the cleaned CSV file
file_path = "C:/users/matias/desktop/sales_data_project/2_data/cleaned_smartphone_sales.csv"
data = pd.read_csv(file_path)

# Step 2: Calculate the average discount percentage
avg_discount = data["discount percentage"].mean()

# Step 3: Print the result
print(f"The average discount percentage (Pandas) is {avg_discount:.2f}%")
