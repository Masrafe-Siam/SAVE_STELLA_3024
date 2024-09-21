import pandas as pd

# Function to classify plant type based on pH, humidity, and air temperature
def classify_plant(row):
    try:
        ph = float(row['pH'])
        humidity = float(row['Humidity'])
        air_temp = float(row['Air Temp'])
        
        if 4.0 <= ph <= 5.5 and 20 <= humidity <= 40 and 0 <= air_temp <= 10:
            return "Berries and Evergreens"
        elif 5.6 <= ph <= 6.5 and 30 <= humidity <= 60 and 10 <= air_temp <= 20:
            return "Leafy Greens and Root Vegetables"
        elif 6.6 <= ph <= 7.5 and 40 <= humidity <= 70 and 20 <= air_temp <= 30:
            return "Warm-Season Fruits and Vegetables"
        elif 7.0 <= ph <= 8.0 and 40 <= humidity <= 60 and 15 <= air_temp <= 25:
            return "Herbs and Aromatic Plants"
        elif 7.5 <= ph <= 9.0 and 20 <= humidity <= 40 and air_temp >= 30:
            return "Drought-Resistant Plants"
        elif 6.0 <= ph <= 7.0 and 70 <= humidity <= 100 and 25 <= air_temp <= 35:
            return "Tropical and Wetland Plants"
        else:
            return "Unknown"
    except ValueError:
        return "Unknown"

# Load the CSV file
input_csv_path = r'.\dataset\pedoshere_dataset_2.csv'
output_csv_path = r'.\dataset\pedoshere_dataset_with_plants.csv'

# Try reading the CSV file with BOM handling
try:
    df = pd.read_csv(input_csv_path, encoding='utf-8-sig')
    print("CSV file loaded successfully.")
    print("First few rows of the file:")
    print(df.head())
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
    exit()
except pd.errors.ParserError:
    print("Error: There was a problem parsing the CSV file.")
    exit()
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit()

# Clean column names by stripping whitespace
df.columns = df.columns.str.strip()

# Check if 'pH', 'Humidity', and 'Air Temp' columns exist
if 'pH' not in df.columns or 'Humidity' not in df.columns or 'Air Temp' not in df.columns:
    print("Error: The CSV file must contain 'pH', 'Humidity', and 'Air Temp' columns.")
    exit()

# Add a new 'Plant Type' column based on pH, humidity, and air temp values
df['Plant Type'] = df.apply(classify_plant, axis=1)

# Save the updated dataframe to a new CSV file
df.to_csv(output_csv_path, index=False)

# Print confirmation message
print(f"Updated CSV file saved to {output_csv_path}")
