import pandas as pd
import os

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']}

df = pd.DataFrame(data)

#adding new row to df
new_row = {'Name': 'Mike', 'Age': 30, 'City': 'San Francisco'}
df.loc[len(df)] = new_row



data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}") 