from pyspark.sql import SparkSession

# Step 1: Create a Spark session
print("Step 1: Creating Spark session...")
spark = SparkSession.builder.appName("Smartphone Sales Analysis").getOrCreate()

# Step 2: Read the cleaned CSV file
print("Step 2: Reading the cleaned CSV file into Spark DataFrame...")
file_path = "C:/users/matias/desktop/sales_etl_pipeline/2_data/cleaned_smartphone_sales.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Step 3: Perform analysis
print("Step 3: Calculating the average discount percentage...")
avg_discount = df.selectExpr("avg(`discount percentage`) as avg_discount").collect()[0]["avg_discount"]

# Step 4: Print the result
print(f"Step 4: The average discount percentage is {avg_discount:.2f}%")