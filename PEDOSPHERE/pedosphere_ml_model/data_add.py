import pandas as pd

def determine_plant_type(row):
    try:
        soil_temp = row['soil_temp']
        soil_ph = row['soil_phs']

        if 10 <= soil_temp <= 15 and 4.5 <= soil_ph <= 5.5:
            return 'Berries and Evergreens'
        elif 10 <= soil_temp <= 20 and 5.5 <= soil_ph <= 6.5:
            return 'Leafy Greens and Root Vegetables'
        elif 8 <= soil_temp <= 15 and 6.0 <= soil_ph <= 7.0:
            return 'Cool-Season Grains'
        elif 10 <= soil_temp <= 18 and 5.5 <= soil_ph <= 6.5:
            return 'Root Crops'
        elif 18 <= soil_temp <= 25 and 6.5 <= soil_ph <= 7.5:
            return 'Warm-Season Fruits and Vegetables'
        elif 20 <= soil_temp <= 30 and 7.0 <= soil_ph <= 8.0:
            return 'Herbs and Aromatic Plants'
        elif 25 <= soil_temp <= 35 and 7.5 <= soil_ph <= 9.0:
            return 'Drought-Resistant Plants'
        elif 25 <= soil_temp <= 30 and 6.0 <= soil_ph <= 7.0:
            return 'Tropical and Wetland Plants'
        elif 15 <= soil_temp <= 25 and 6.0 <= soil_ph <= 7.0:
            return 'Legumes and Nitrogen-Fixers'
        elif 15 <= soil_temp <= 25 and 6.5 <= soil_ph <= 7.5:
            return 'Stone Fruits'
        elif 25 <= soil_temp <= 30 and 6.0 <= soil_ph <= 6.8:
            return 'Subtropical Fruits'
        elif 18 <= soil_temp <= 28 and 5.5 <= soil_ph <= 6.5:
            return 'Medicinal Plants'
        else:
            return 'unknown'
    except Exception as e:
        return 'unknown'

# Load the CSV file
try:
    df = pd.read_csv('.\\dataset\\pedo_data_add_1.csv')
except FileNotFoundError:
    print("Error: The file 'input_data.csv' was not found.")
    exit()

# Apply the function to each row
df['Plant_Type'] = df.apply(determine_plant_type, axis=1)

# Save the updated CSV file
df.to_csv('.\\dataset\\pedo_data_add_2.csv', index=False)

print("Processing complete. The updated file is 'output_data_with_plants.csv'.")
