import plotly.express as px

def create_monthly_sales_trend(df):
    """
    Creates a line chart showing the monthly sales trend.

    Args:
        df (pd.DataFrame): The preprocessed sales data.

    Returns:
        A Plotly figure object.
    """
    monthly_sales = df.groupby(['Year', 'Month'])['Total Price'].sum().reset_index()
    monthly_sales['Month'] = pd.Categorical(monthly_sales['Month'], categories=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
    monthly_sales = monthly_sales.sort_values(['Year', 'Month'])
    fig = px.line(monthly_sales, x='Month', y='Total Price', color='Year',
                  title='Monthly Sales Trend', markers=True)
    return fig

def create_yearly_sales_summary(df):
    """
    Creates a bar chart showing the total sales for each year.

    Args:
        df (pd.DataFrame): The preprocessed sales data.

    Returns:
        A Plotly figure object.
    """
    yearly_sales = df.groupby('Year')['Total Price'].sum().reset_index()
    fig = px.bar(yearly_sales, x='Year', y='Total Price', title='Yearly Sales Summary',
                 labels={'Total Price': 'Total Sales (in USD)'})
    return fig