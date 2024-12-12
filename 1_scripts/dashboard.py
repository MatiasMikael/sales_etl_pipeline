import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Step 1: Load datasets
print("Step 1: Loading datasets...")
# Load datasets
average_discount_by_brand = pd.read_csv("C:/users/matias/desktop/sales_data_project/3_sql_queries/average_discount_by_brand.csv")
top_selling_brands = pd.read_csv("C:/users/matias/desktop/sales_data_project/3_sql_queries/top_5_selling_brands.csv")
top_colors_by_sales = pd.read_csv("C:/users/matias/desktop/sales_data_project/3_sql_queries/top_10_colors_by_sales.csv")
print("Datasets loaded successfully.")

# Step 2: Create Dash app
print("Step 2: Creating Dash app...")
app = Dash(__name__)

# Step 3: Visualization 1 - Average Discount by Brand
print("Step 3: Creating Visualization 1 - Average Discount by Brand...")
fig1 = px.bar(
    average_discount_by_brand,
    x="BRANDS",
    y="AVERAGE_DISCOUNT_PERCENTAGE",
    title="Average Discount by Brand",
    labels={"AVERAGE_DISCOUNT_PERCENTAGE": "Average Discount (%)", "BRANDS": "Brands"}
)

# Step 4: Visualization 2 - Top Selling Brands
print("Step 4: Creating Visualization 2 - Top Selling Brands...")
fig2 = px.bar(
    top_selling_brands,
    x="BRANDS",
    y="TOTAL_SALES",
    title="Top 5 Selling Brands",
    labels={"TOTAL_SALES": "Total Sales", "BRANDS": "Brands"},
    color="BRANDS"
)

# Step 5: Visualization 3 - Top Colors by Sales
print("Step 5: Creating Visualization 3 - Top Colors by Sales...")
fig3 = px.bar(
    top_colors_by_sales,
    x="COLORS",
    y="TOTAL_SALES",
    title="Top 10 Colors by Sales",
    labels={"TOTAL_SALES": "Total Sales", "COLORS": "Colors"},
    color="COLORS"
)

# Step 6: Set up the app layout
print("Step 6: Setting up app layout...")
app.layout = html.Div(children=[
    html.H1(children="Smartphone Sales Dashboard"),
    dcc.Graph(figure=fig1),  # Average Discount by Brand
    dcc.Graph(figure=fig2),  # Top Selling Brands
    dcc.Graph(figure=fig3),  # Top Colors by Sales
])

# Step 7: Run the Dash server
print("Step 7: Running Dash server...")
if __name__ == "__main__":
    app.run_server(debug=True)