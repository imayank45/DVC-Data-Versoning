import pandas as pd
import os

# create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Adding new row to the dataset v2
new_row_loc1 = {'Name': 'Mayank', 'Age':24, 'City': 'Mumbai'}
df.loc[len(df.index)] = new_row_loc1

## Adding new row to the dataset v3
# new_row_loc2 = {'Name': 'Mahesh', 'Age':25, 'City': 'Dubai'}
# df.loc[len(df.index)] = new_row_loc2

# Ensure the data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# save the dataframe to a CSV file, including the columns name
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")