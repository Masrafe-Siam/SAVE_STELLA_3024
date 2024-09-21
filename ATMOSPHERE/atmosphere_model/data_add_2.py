import pandas as pd

def determine_land_type(row):
    try:
        air_temp = row['air_temp']
        humidity = row['humidity']
        #surface_temp = row['surface_temperatures']

        if 25 <= air_temp <= 35 and 30 <= humidity <= 50:
            return 'Urban Cool Roofs'
        elif 35 <= air_temp <= 45 and 10 <= humidity <= 30:
            return 'Desert Oasis Management'
        elif 25 <= air_temp <= 35 and 80 <= humidity <= 100:
            return 'Tropical Storm Surge Defense'
        elif -10 <= air_temp <= 0 and 40 <= humidity <= 60:
            return 'Arctic Permafrost Protection'
        elif 20 <= air_temp <= 30 and 30 <= humidity <= 50:
            return 'Mediterranean Drought Management'
        elif 30 <= air_temp <= 40 and 5 <= humidity <= 20:
            return 'Arid Desertification Prevention'
        elif 20 <= air_temp <= 30 and 60 <= humidity <= 80:
            return 'Tropical Urban Green Spaces'
        elif 10 <= air_temp <= 20 and 50 <= humidity <= 70:
            return 'Sub-Arctic Summer Heat Management'
        elif 25 <= air_temp <= 35 and 80 <= humidity <= 100:
            return 'Equatorial Rainforest Preservation'
        elif 10 <= air_temp <= 20 and 60 <= humidity <= 80:
            return 'Temperate Wetland Restoration'
        else:
            return 'unknown'
    except Exception as e:
        return 'unknown'


# def determine_land_type(row):
#     try:
#         air_temp = row['air_temp']
#         humidity = row['humidity']
#         surface_temp = row['surface_temperatures']

#         if 25 <= air_temp <= 35 and 30 <= humidity <= 50 and 30 <= surface_temp <= 35:
#             return 'Urban Cool Roofs'
#         elif 35 <= air_temp <= 45 and 10 <= humidity <= 30 and 45 <= surface_temp <= 50:
#             return 'Desert Oasis Management'
#         elif 25 <= air_temp <= 35 and 80 <= humidity <= 100 and 25 <= surface_temp <= 35:
#             return 'Tropical Storm Surge Defense'
#         elif -10 <= air_temp <= 0 and 40 <= humidity <= 60 and 0 <= surface_temp <= -10:
#             return 'Arctic Permafrost Protection'
#         elif 20 <= air_temp <= 30 and 30 <= humidity <= 50 and 25 <= surface_temp <= 30:
#             return 'Mediterranean Drought Management'
#         elif 30 <= air_temp <= 40 and 5 <= humidity <= 20 and 40 <= surface_temp <= 50:
#             return 'Arid Desertification Prevention'
#         elif 20 <= air_temp <= 30 and 60 <= humidity <= 80 and 20 <= surface_temp <= 30:
#             return 'Tropical Urban Green Spaces'
#         elif 10 <= air_temp <= 20 and 50 <= humidity <= 70 and 10 <= surface_temp <= 15:
#             return 'Sub-Arctic Summer Heat Management'
#         elif 25 <= air_temp <= 35 and 80 <= humidity <= 100 and 25 <= surface_temp <= 30:
#             return 'Equatorial Rainforest Preservation'
#         elif 10 <= air_temp <= 20 and 60 <= humidity <= 80 and 10 <= surface_temp <= 20:
#             return 'Temperate Wetland Restoration'
#         else:
#             return 'unknown'
#     except Exception as e:
#         return 'unknown'
# Function to classify land type based on air temperature, humidity, and surface temperature
# def classify_land(row):
#     try:
#         air_temp = float(row['air_temp'])
#         humidity = float(row['humidity'])
#         #surface_temp = float(row['surface_temp'])
#         if air_temp >= 30 and 40 <= humidity <= 60:
#             return "Cooling Urban Ecosystems"
#         elif 25 <= air_temp <= 35 and 20 <= humidity <= 40:
#             return "Drought-Resilient Landscapes"
#         elif 20 <= air_temp <= 30 and 70 <= humidity <= 100:
#             return "Flood-Adapted Wetlands"
#         elif 0 <= air_temp <= 10 and 30 <= humidity <= 50:
#             return "Cold Climate Resilience"
#         elif 10 <= air_temp <= 20 and 40 <= humidity <= 70:
#             return "Temperate Zone Restoration"
#         else:
#             return "Unknown"
#     except:
#         return "Unknown"
#if air_temp >= 30 and 40 <= humidity <= 60 and surface_temp > 40:
    #         return "Cooling Urban Ecosystems"
    #     elif 25 <= air_temp <= 35 and 20 <= humidity <= 40 and 30 <= surface_temp <= 40:
    #         return "Drought-Resilient Landscapes"
    #     elif 20 <= air_temp <= 30 and 70 <= humidity <= 100 and 20 <= surface_temp <= 30:
    #         return "Flood-Adapted Wetlands"
    #     elif 0 <= air_temp <= 10 and 30 <= humidity <= 50 and 5 <= surface_temp <= 10:
    #         return "Cold Climate Resilience"
    #     elif 10 <= air_temp <= 20 and 40 <= humidity <= 70 and 10 <= surface_temp <= 20:
    #        return "Temperate Zone Restoration"
    #     else:
    #         return "Unknown"
    # except:
    #     return "Unknown"
# Load the CSV file
try:
    df = pd.read_csv('.\\dataset\\air_data_add_4.csv')
except FileNotFoundError:
    print("Error: The file 'input_data.csv' was not found.")
    exit()

# Apply the function to each row
df['Land_Type'] = df.apply(determine_land_type, axis=1)

# Save the updated CSV file
df.to_csv('.\\dataset\\air_data_add_7.csv', index=False)

print("Processing complete. The updated file is 'output_data_with_plants.csv'.")
