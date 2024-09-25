import pandas as pd

# Load the CSV file with the 'Aquatic_Environment' column
try:
    df = pd.read_csv('.\\datasets\\output_data_with_environments_1.csv')
except FileNotFoundError:
    print("Error: The file 'output_data_with_plants.csv' was not found.")
    exit()

# Drop rows where 'Aquatic_Environment' is 'unknown'
df_cleaned = df[df['Aquatic_Environment'] != 'unknown']

# Save the cleaned CSV file
df_cleaned.to_csv('.\\datasets\\cleaned_output_data_2.csv', index=False)

print("Rows with 'unknown' Aquatic_Environment have been deleted. The cleaned file is 'cleaned_output_data.csv'.")
