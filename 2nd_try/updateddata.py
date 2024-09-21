import pandas as pd

# Specify the input and output file names
input_file = 'D:\\nasa_2024_farid\\pedoshere_dataset_with_plants.csv'  # Replace with your actual input file name
output_file = 'D:\\nasa_2024_farid\\updated.csv'  # Replace with your desired output file name

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Remove rows where 'plant type' is 'Unknown'
df_cleaned = df[df['Plant Type'] != 'Unknown']

# Write the cleaned DataFrame to a new CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Rows with 'Unknown' in 'plant type' have been removed. The cleaned file is saved as '{output_file}'.")
