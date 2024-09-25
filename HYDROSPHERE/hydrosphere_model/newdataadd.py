import pandas as pd

# Define the function to determine the aquatic environment type
def determine_aquatic_environment(row):
    try:
        do = float(row['Dissolved_Oxygen'])
        salinity = float(row['salinities'])
        
        if 0 <= do <= 3 and 0 <= salinity <= 5:
            return 'Very Low Oxygen, Freshwater Pond - Fish: Carp, Goldfish'
        elif 3 <= do <= 5 and 5 <= salinity <= 15:
            return 'Low Oxygen, Brackish Water Lagoon - Fish: Flounder, Sea Bass'
        elif 5 <= do <= 8 and 15 <= salinity <= 25:
            return 'Moderate Oxygen, Medium Salinity Coastal Estuary - Fish: Salmon, Eel'
        elif 8 <= do <= 12 and 0 <= salinity <= 10:
            return 'High Oxygen, Low Salinity Stream - Fish: Rainbow Trout, Perch'
        elif 12 <= do <= 20 and 30 <= salinity <= 50:
            return 'Very High Oxygen, High Salinity Sea - Fish: Tuna, Mackerel'
        elif 0 <= do <= 2 and 50 <= salinity <= 60:
            return 'Very Low Oxygen, Hypersaline Inland Sea - Fish: Brine Shrimp, Saltwater Tilapia'
        elif 2 <= do <= 5 and 10 <= salinity <= 20:
            return 'Low Oxygen, Medium Salinity Tropical Lake - Fish: Tilapia, Guppy'
        elif 5 <= do <= 7 and 0 <= salinity <= 10:
            return 'Moderate Oxygen, Low Salinity Freshwater Lake - Fish: Bass, Carp'
        elif 10 <= do <= 15 and 15 <= salinity <= 25:
            return 'High Oxygen, Brackish Estuary - Fish: Sea Trout, Striped Bass'
        elif 12 <= do <= 18 and 20 <= salinity <= 40:
            return 'Very High Oxygen, Coastal Saltwater - Fish: Snapper, Grouper'
        elif 1 <= do <= 4 and 40 <= salinity <= 60:
            return 'Low Oxygen, Hypersaline Salt Lake - Fish: Artemia (Brine Shrimp), Tilapia'
        elif 5 <= do <= 9 and 35 <= salinity <= 45:
            return 'Moderate Oxygen, High Salinity Coral Reef - Fish: Clownfish, Parrotfish'
        elif 15 <= do <= 20 and 0 <= salinity <= 5:
            return 'Very High Oxygen, Low Salinity Wetland - Fish: Catfish, Pike'
        elif 2 <= do <= 5 and 5 <= salinity <= 15:
            return 'Low Oxygen, Coastal Salt Marsh - Fish: Mullets, Flatfish'
        elif 6 <= do <= 10 and 0 <= salinity <= 5:
            return 'Moderate Oxygen, Freshwater River - Fish: Trout, Whitefish'
        elif 10 <= do <= 14 and 25 <= salinity <= 35:
            return 'High Oxygen, Medium Salinity Oceanic Zone - Fish: Tuna, Sardines'
        elif 0 <= do <= 2 and 10 <= salinity <= 20:
            return 'Very Low Oxygen, Medium Salinity Lagoon - Fish: Eels, Gobies'
        elif 2 <= do <= 5 and 30 <= salinity <= 50:
            return 'Low Oxygen, High Salinity Coastal Waters - Fish: Haddock, Halibut'
        elif 5 <= do <= 7 and 40 <= salinity <= 60:
            return 'Moderate Oxygen, Hypersaline Lake - Fish: Brine Shrimp, Saltwater Tilapia'
        elif 10 <= do <= 12 and 0 <= salinity <= 5:
            return 'High Oxygen, Low Salinity Mountain Stream - Fish: Brown Trout, Arctic Char'
        else:
            return 'unknown'
    except (ValueError, KeyError):
        return 'unknown'

# Load the CSV file
try:
    df = pd.read_csv('.\\datasets\\hydronewdata_2.csv')
except FileNotFoundError:
    print("Error: The file 'hydronewdata_2.csv' was not found.")
    exit()

# Apply the function to each row
df['Aquatic_Environment'] = df.apply(determine_aquatic_environment, axis=1)

# Save the updated CSV file
df.to_csv('.\\datasets\\output_data_with_environments_1.csv', index=False)

print("Processing complete. The updated file is 'output_data_with_environments_3.csv'.")
