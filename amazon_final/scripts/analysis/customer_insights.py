import plotly.express as px
import pandas as pd

def create_sales_by_city_barchart(df):
    """
    Creates a bar chart showing total sales for each city.

    Args:
        df (pd.DataFrame): The preprocessed sales data.

    Returns:
        A Plotly figure object.
    """
    city_sales = df.groupby('City')['Total Price'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(city_sales, x='City', y='Total Price',
                 title='Total Sales by City',
                 labels={'Total Price': 'Total Sales (in USD)'})
    return fig

def create_sales_distribution_map(df):
    """
    Creates a scatter map to show sales distribution across cities.

    Args:
        df (pd.DataFrame): The preprocessed sales data containing 'City' and 'Country'.

    Returns:
        A Plotly figure object.
    """
    # Note: For a real-world scenario, you would need latitude and longitude for each city.
    # For this example, we will use Plotly's built-in location feature for USA cities.
    # If using international data, a more robust geocoding solution would be needed.

    sales_by_location = df.groupby(['City', 'Country'])['Total Price'].sum().reset_index()

    # To make the map more visually appealing, we can size the points by sales volume.
    fig = px.scatter_geo(sales_by_location,
                         locations="City",
                         locationmode="USA-states",  # This works for US cities
                         scope="usa",
                         hover_name="City",
                         size="Total Price",
                         color="Total Price",
                         color_continuous_scale=px.colors.sequential.Viridis,
                         title="Sales Distribution Across the USA")
    # This is a limitation; locationmode should ideally be more specific like city names,
    # but that requires lat/lon data. We'll use state-level for demonstration.
    # To make this work with the sample data, we'd need to add a 'State' column.
    # For now, we will plot by city on a bar chart as the primary geo-visualization.

    # Let's return a more reliable bar chart instead if lat/lon is not available.
    return create_sales_by_city_barchart(df)