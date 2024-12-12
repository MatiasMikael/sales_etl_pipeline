# sales_etl_pipeline

This project demonstrates the creation of a data pipeline and an interactive dashboard for analyzing smartphone sales data. The data was cleaned, processed, and visualized to provide insights into discounts and sales trends.

## Tools Used

1. Python: Data cleaning and processing.
2. Pandas: Data manipulation and preparation.
3. Apache Spark: Data validation.
4. Snowflake: Data storage and SQL queries.
5. Dash & Plotly: Interactive dashboard creation.

## Process Overview

1. The dataset was sourced from Kaggle: Smartphone Sale Dataset.
2. Data was cleaned and saved as cleaned_smartphone_sales.csv.
3. Cleaned data was processed and analyzed using Apache Spark for large-scale data transformations. The analysis, along with the verify_avg_discount.py script, was specifically designed to test the reliability of the dataset.
4. The transformed data was uploaded to Snowflake for structured analysis using SQL.
5. Insights from the data were visualized using Dash.

## Visualizations

The dashboard provides the following visual insights:
- Average Discount by Brand.
- Top 5 Selling Brands.
- Top 10 Colors by Sales.

## License

This project is licensed under the MIT License. The dataset is licensed under Apache 2.0: [Smartphone Sale Dataset] https://www.kaggle.com/datasets/yaminh/smartphone-sale-dataset.
