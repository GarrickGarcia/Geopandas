import pandas as pd

file_path = 's3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/places-00000.snappy.parquet'

# Read directly from S3
df = pd.read_parquet(file_path, storage_options={'anon': True})

# Display the first few rows
print(df.head())