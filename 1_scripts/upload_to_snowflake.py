import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Snowflake connection parameters from environment variables
connection_params = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": "COMPUTE_WH",
    "database": "SALES_ANALYSIS",
    "schema": "PUBLIC"
}

def copy_csv_to_snowflake(file_path, table_name, connection_params):
    print("Step 1: Connecting to Snowflake...")
    conn = snowflake.connector.connect(**connection_params)
    cursor = conn.cursor()

    try:
        print("Step 2: Creating or using target table...")
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            Brands STRING,
            Models STRING,
            Colors STRING,
            Memory STRING,
            Storage STRING,
            Rating FLOAT,
            Selling_Price INT,
            Original_Price INT,
            Discount INT,
            Discount_Percentage FLOAT
        )
        """)

        print("Step 3: Preparing file stage for upload...")
        cursor.execute(f"CREATE OR REPLACE TEMPORARY STAGE my_temp_stage")

        print("Step 4: Uploading file to Snowflake stage...")
        cursor.execute(f"PUT file://{file_path} @my_temp_stage AUTO_COMPRESS=TRUE")

        print("Step 5: Copying data from stage to table...")
        cursor.execute(f"""
        COPY INTO {table_name}
        FROM @my_temp_stage
        FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '"' ESCAPE_UNENCLOSED_FIELD = NONE);
        """)

        print("Data successfully loaded into table.")
    finally:
        print("Closing connection to Snowflake...")
        conn.close()

if __name__ == "__main__":
    file_path = "C:/users/matias/desktop/sales_data_project/2_data/cleaned_smartphone_sales.csv"
    table_name = "SMARTPHONE_SALES"

    print("Starting COPY INTO process...")
    copy_csv_to_snowflake(file_path, table_name, connection_params)
    print("COPY INTO process completed successfully!")