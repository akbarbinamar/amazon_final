import streamlit as st

def format_number(num):
    """
    Formats a large number into a more readable string (e.g., 1.2M, 3.4k).

    Args:
        num (float): The number to format.

    Returns:
        str: The formatted number as a string.
    """
    if num > 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    if num > 1_000:
        return f"{num / 1_000:.1f}k"
    return f"{num:,.2f}"

def add_sidebar_logo():
    """
    Adds a logo to the Streamlit sidebar.
    Replace the URL with your own logo's URL or a local file path.
    """
    st.sidebar.markdown(
        f"""
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" width="150">
        </div>
        """,
        unsafe_allow_html=True,
    )