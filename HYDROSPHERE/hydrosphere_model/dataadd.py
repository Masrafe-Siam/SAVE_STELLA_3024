import pandas as pd

# Define the function to determine the plant type
def determine_plant_type(row):
    try:
        do = float(row['Dissolved_Oxygen'])
        temp = float(row['Temperature'])
        ph = float(row['pH'])
        
        if 3.1 <= do <= 5 and 25 <= temp <= 30 and 7.5 <= ph <= 8.0:
            return 'Tropical, Alkaline Lake with Limited Oxygen'
        elif 5.1 <= do <= 7 and 8 <= temp <= 15 and 5.5 <= ph <= 6.0:
            return 'Cool, Acidic River with Balanced Oxygen'
        elif 7.1 <= do <= 10 and 20 <= temp <= 30 and 6.8 <= ph <= 7.2:
            return 'Warm, Neutral Pond with Abundant Oxygen'
        elif 1 <= do <= 3 and 5 <= temp <= 10 and 8.1 <= ph <= 8.5:
            return 'Cold, Alkaline Stream with Sparse Oxygen'
        elif 10.1 <= do <= 15 and 10 <= temp <= 20 and 6.0 <= ph <= 6.5:
            return 'Temperate, Acidic Wetland with Optimal Oxygen'
        else:
            return 'unknown'
    except (ValueError, KeyError):
        return 'unknown'

# Load the CSV file
try:
    df = pd.read_csv('.\\datasets\\sampled_data_Model_2.csv')
except FileNotFoundError:
    print("Error: The file 'input_data.csv' was not found.")
    exit()

# Apply the function to each row
df['Plant Type'] = df.apply(determine_plant_type, axis=1)

# Save the updated CSV file
df.to_csv('.\\datasets\\output_data_with_plants.csv', index=False)

print("Processing complete. The updated file is 'output_data_with_plants.csv'.")
