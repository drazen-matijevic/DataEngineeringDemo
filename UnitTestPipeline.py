import pandas as pd

# Load data for transportation into dataframe
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Clean the data
def clean_data(df):
    cleaned_df = df.dropna()
    return cleaned_df

