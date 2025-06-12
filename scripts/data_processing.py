import pandas as pd

def clean_and_preprocess_data(raw_data_path, processed_data_path):
    """
    Cleans and preprocesses the raw Amazon sales data.

    Args:
        raw_data_path (str): The file path for the raw data CSV file.
        processed_data_path (str): The file path to save the cleaned data CSV file.
    """
    try:
        df = pd.read_csv(raw_data_path)

        # Handle missing values
        df.dropna(inplace=True)

        # Convert 'Order Date' to datetime objects
        df['Order Date'] = pd.to_datetime(df['Order Date'])

        # Extract year and month
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month_name()

        # Ensure correct data types for numerical columns
        numerical_cols = ['Unit Price', 'Total Price', 'Units Sold']
        for col in numerical_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Drop rows with any remaining null values after coercion
        df.dropna(subset=numerical_cols, inplace=True)

        # Save the cleaned data
        df.to_csv(processed_data_path, index=False)
        print(f"Data cleaned and saved to {processed_data_path}")

    except FileNotFoundError:
        print(f"Error: The file at {raw_data_path} was not found.")
    except Exception as e:
        print(f"An error occurred during data processing: {e}")

if __name__ == '__main__':
    # Define file paths
    raw_data_path = 'data/raw/amazon_sales_data.csv'
    processed_data_path = 'data/processed/cleaned_sales_data.csv'

    # Run the data processing function
    clean_and_preprocess_data(raw_data_path, processed_data_path)