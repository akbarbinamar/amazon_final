import streamlit as st
import pandas as pd
from scripts.analysis import sales_trends, product_analysis

# --- Page Configuration ---
st.set_page_config(
    page_title="Amazon Sales Analysis Dashboard",
    page_icon="🛒",
    layout="wide"
)

# --- Title and Introduction ---
st.title("Amazon Sales Analysis Dashboard")
st.markdown("""
This interactive dashboard provides a comprehensive analysis of Amazon sales data.
Use the filters on the sidebar to explore the data.
""")

# --- Data Loading ---
@st.cache_data
def load_data(path):
    """Loads the preprocessed data."""
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        st.error(f"Error: The file at {path} was not found. Please run the data processing script first.")
        return None

cleaned_data_path = 'data/processed/cleaned_sales_data.csv'
df = load_data(cleaned_data_path)

if df is not None:
    # --- Sidebar Filters ---
    st.sidebar.header("Filters")
    selected_year = st.sidebar.multiselect(
        "Select Year",
        options=df["Year"].unique(),
        default=df["Year"].unique()
    )

    selected_category = st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )

    # --- Filter Data ---
    filtered_df = df[
        (df["Year"].isin(selected_year)) &
        (df["Category"].isin(selected_category))
    ]

    # --- Main Dashboard ---
    st.header("Sales Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", f"${filtered_df['Total Price'].sum():,.2f}")
    with col2:
        st.metric("Total Units Sold", f"{filtered_df['Units Sold'].sum():,}")
    with col3:
        st.metric("Number of Orders", f"{filtered_df['Order ID'].nunique():,}")

    st.markdown("---")

    # --- Sales Trends ---
    st.header("Sales Trends")
    st.plotly_chart(sales_trends.create_monthly_sales_trend(filtered_df), use_container_width=True)
    st.plotly_chart(sales_trends.create_yearly_sales_summary(filtered_df), use_container_width=True)

    st.markdown("---")

    # --- Product Analysis ---
    st.header("Product Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(product_analysis.create_top_selling_products_chart(filtered_df), use_container_width=True)
    with col2:
        st.plotly_chart(product_analysis.create_sales_by_category_chart(filtered_df), use_container_width=True)

else:
    st.warning("Please ensure the dataset is available at 'data/raw/amazon_sales_data.csv' and run 'scripts/data_processing.py'.")