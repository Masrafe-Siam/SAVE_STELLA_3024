import pandas as pd

# Function to classify land type based on air temperature, humidity, and aerosol level
def classify_land(row):
    try:
        air_temp = float(row['air_temp'])
        aerosol_level = float(row['aerosols'])
        
        # Classification scenarios
        if 0 <= air_temp <= 5 and aerosol_level <= 1:
            return "High-Altitude Glacier Protection"
        elif 35 <= air_temp <= 45 and 0 < aerosol_level <= 3:
            return "Heat-Resilient Urban Infrastructure"
        elif 30 <= air_temp <= 40 and 3 <= aerosol_level <= 4:
            return "Green Agriculture Initiatives"
        elif 10 <= air_temp <= 20 and 1 <= aerosol_level <= 3:
            return "Wetland Carbon Sink Restoration"
        elif 25 <= air_temp <= 35 and aerosol_level <= 2:
            return "Heat-Adapted Coastal Ecosystems"
        elif 0 <= air_temp <= 10 and 1 <= aerosol_level <= 2:
            return "Integrated Mountain Ecosystem Management"
        elif 20 <= air_temp <= 30 and 3 <= aerosol_level <= 4:
            return "Urban Air Quality Monitoring Network"
        elif 35 <= air_temp <= 45 and 1 <= aerosol_level <= 3:
            return "Resilient Agricultural Practices in Semi-Arid Regions"
        else:
            return "Unknown"
    except (ValueError, KeyError):
        return "Unknown"

# Load the CSV file
try:
    df = pd.read_csv('.\\dataset\\airnewdata_2.csv')
except FileNotFoundError:
    print("Error: The file 'air_data_add_4.csv' was not found.")
    exit()

# Apply the function to each row
df['Land_Type'] = df.apply(classify_land, axis=1)

# Save the updated CSV file
df.to_csv('.\\dataset\\cleaned_output_data_2.csv', index=False)

print("Processing complete. The updated file is 'air_data_add_5.csv'.")