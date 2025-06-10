import plotly.express as px

def create_top_selling_products_chart(df, top_n=10):
    """
    Creates a bar chart for the top N selling products.

    Args:
        df (pd.DataFrame): The preprocessed sales data.
        top_n (int): The number of top products to display.

    Returns:
        A Plotly figure object.
    """
    top_products = df.groupby('Product Name')['Units Sold'].sum().nlargest(top_n).reset_index()
    fig = px.bar(top_products, x='Units Sold', y='Product Name', orientation='h',
                 title=f'Top {top_n} Selling Products',
                 labels={'Units Sold': 'Total Units Sold'})
    return fig

def create_sales_by_category_chart(df):
    """
    Creates a pie chart showing sales distribution by product category.

    Args:
        df (pd.DataFrame): The preprocessed sales data.

    Returns:
        A Plotly figure object.
    """
    category_sales = df.groupby('Category')['Total Price'].sum().reset_index()
    fig = px.pie(category_sales, values='Total Price', names='Category',
                 title='Sales by Product Category',
                 hole=0.3)
    return fig