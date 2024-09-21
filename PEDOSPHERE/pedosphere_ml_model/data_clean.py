import pandas as pd

# Load the CSV file with the 'plant Type' column
try:
    df = pd.read_csv('.\\dataset\\pedo_data_add_2.csv')
except FileNotFoundError:
    print("Error: The file 'output_data_with_plants.csv' was not found.")
    exit()

# Drop rows where 'plant Type' is 'unknown'
df_cleaned = df[df['Plant_Type'] != 'unknown']

# Save the cleaned CSV file
df_cleaned.to_csv('.\\dataset\\cleaned_output_data.csv', index=False)

print("Rows with 'unknown' plant types have been deleted. The cleaned file is 'cleaned_output_data.csv'.")
