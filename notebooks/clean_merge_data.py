import pandas as pd
import os

# Define file paths
base_dir = 'data' 
raw_dir = os.path.join(base_dir, 'raw')
processed_dir = os.path.join(base_dir, 'processed')

# Process Instagram Posts
instagram_path = os.path.join(raw_dir, 'instagram_posts.csv')
try:
    instagram_df = pd.read_csv(instagram_path)
except FileNotFoundError:
    print(f"File not found: {instagram_path}")
    exit(1)

instagram_df['date'] = pd.to_datetime(instagram_df['date'])
instagram_grouped = instagram_df.groupby('date').agg(
    Likes=('likes', 'sum'),
    Comments=('comments', 'sum')
).reset_index()
instagram_grouped['Instagram Post?'] = 'Yes'

# Process Sessions
sessions_path = os.path.join(raw_dir, 'sessions_by_refferer_decive_type_and_day.csv')
try:
    sessions_df = pd.read_csv(sessions_path)
except FileNotFoundError:
    print(f"File not found: {sessions_path}")
    exit(1)

sessions_df['Day'] = pd.to_datetime(sessions_df['Day'])
sessions_grouped = sessions_df.groupby('Day')['Sessions'].sum().reset_index().rename(columns={'Day': 'Date'})

# Process Net Sales
sales_path = os.path.join(raw_dir, 'total_sales_over_time.csv')
try:
    sales_df = pd.read_csv(sales_path)
except FileNotFoundError:
    print(f"File not found: {sales_path}")
    exit(1)

# Clean and prepare sales data
sales_df['Day'] = pd.to_datetime(sales_df['Day'])
sales_grouped = sales_df[['Day', 'Net sales']].rename(
    columns={'Day': 'Date', 'Net sales': 'Net Sales'}
)

# Merge Data
master_df = pd.merge(sessions_grouped, sales_grouped, on='Date', how='outer')
master_df = pd.merge(master_df, instagram_grouped, left_on='Date', right_on='date', how='left')
master_df.drop('date', axis=1, inplace=True)

# Handle Missing Values
master_df['Instagram Post?'] = master_df['Instagram Post?'].fillna('No')
for col in ['Sessions', 'Net Sales', 'Likes', 'Comments']:
    master_df[col] = master_df[col].fillna(0)

# Format Net Sales as Currency
master_df['Net Sales'] = master_df['Net Sales'].apply(lambda x: f'£{x:.2f}')

# Save Results
output_csv = os.path.join(processed_dir, 'master_data.csv')
master_df.to_csv(output_csv, index=False)

print("Master dataset created successfully with complete sales data!")