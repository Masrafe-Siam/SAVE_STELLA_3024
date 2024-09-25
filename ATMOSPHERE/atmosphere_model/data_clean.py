import pandas as pd

# Load the CSV file with the 'land Type' column
try:
    df = pd.read_csv('.\\dataset\\cleaned_output_data_2.csv')
except FileNotFoundError:
    print("Error: The file 'output_data_with_plants.csv' was not found.")
    exit()

# Drop rows where 'land Type' is 'unknown'
df_cleaned = df[df['Land_Type'] != 'Unknown']

# Save the cleaned CSV file
df_cleaned.to_csv('.\\dataset\\cleaned_output_data_3.csv', index=False)

print("Rows with 'unknown' land types have been deleted. The cleaned file is 'cleaned_output_data.csv'.")
