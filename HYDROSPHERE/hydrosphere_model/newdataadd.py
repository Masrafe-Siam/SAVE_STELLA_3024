import pandas as pd

def determine_fish_type(row):
    try:
        # Extract 'dissolved_oxygen' (first column) and 'pH' (second column)
        do = row['dissolved_oxygen']  # Dissolved Oxygen (mg/L)
        ph = row['pH']                # pH value

        # Scenario 1: Slightly Alkaline, Low Oxygen Lake
        if 7.5 <= ph <= 8.0 and 1 <= do <= 5:
            return 'Slightly Alkaline, Low Oxygen Lake'

        # Scenario 2: Acidic, Moderate Oxygen River
        elif 5.5 <= ph <= 6.0 and 5 <= do <= 7:
            return 'Acidic, Moderate Oxygen River'

        # Scenario 3: Neutral, High Oxygen Pond
        elif 6.8 <= ph <= 7.2 and 7 <= do <= 10:
            return 'Neutral, High Oxygen Pond'

        # Scenario 4: Alkaline, Very Low Oxygen Stream
        elif 8.1 <= ph <= 8.5 and 1 <= do <= 3:
            return 'Alkaline, Very Low Oxygen Stream'

        # Scenario 5: Slightly Acidic, Very High Oxygen Wetland
        elif 6.0 <= ph <= 6.5 and 10 <= do <= 15:
            return 'Slightly Acidic, Very High Oxygen Wetland'

        # Scenario 6: Neutral, Moderate Oxygen Tropical Lake
        elif 6.5 <= ph <= 7.5 and 4 <= do <= 7:
            return 'Neutral, Moderate Oxygen Tropical Lake'

        # Scenario 7: Neutral, High Oxygen Stream
        elif 6.8 <= ph <= 7.5 and 8 <= do <= 12:
            return 'Neutral, High Oxygen Stream'

        # Scenario 8: Slightly Acidic, Low to Moderate Oxygen Pond
        elif 6.0 <= ph <= 6.5 and 3 <= do <= 6:
            return 'Slightly Acidic, Low to Moderate Oxygen Pond'

        # Scenario 9: Neutral, Moderate Oxygen River
        elif 6.5 <= ph <= 7.2 and 5 <= do <= 7:
            return 'Neutral, Moderate Oxygen River'

        # Scenario 10: Slightly Alkaline, Low Oxygen Lake
        elif 7.0 <= ph <= 7.8 and 2 <= do <= 5:
            return 'Slightly Alkaline, Low Oxygen Lake'

        else:
            return 'unknown'
    except Exception as e:
        return 'unknown'

# Load the CSV file
try:
    df = pd.read_csv('.\\datasets\\hydro_data_clean_2.csv')
except FileNotFoundError:
    print("Error: The file 'hydro_data_clean_1.csv' was not found.")
    exit()

# Apply the function to each row
df['fish_type'] = df.apply(determine_fish_type, axis=1)

# Save the updated CSV file
df.to_csv('.\\datasets\\hydro_data_add_4.csv', index=False)

print("Processing complete. The updated file is 'hydro_data_add_4.csv'.")
