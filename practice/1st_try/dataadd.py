import pandas as pd

# Function to classify plant type based on pH value
def classify_plant(ph):
    try:
        ph = float(ph)
        if 4.0 <= ph <= 5.0:
            return "Acidic Specialists"
        elif 5.1 <= ph <= 6.0:
            return "Acidic Nurturers"
        elif 6.1 <= ph <= 7.0:
            return "Neutral Sustainers"
        elif 7.1 <= ph <= 8.0:
            return "Alkaline Adapters"
        elif 8.1 <= ph <= 8.5:
            return "Alkaline Enthusiasts"
        elif 8.6 <= ph <= 9.0:
            return "Extreme Alkaline Survivors"
        else:
            return "Unknown"
    except ValueError:
        return "Unknown"

# Load the CSV file
input_csv_path = r'D:\Masrafe\Coding\Git_Hub_code\ml_project\GURDIANS_OF_THE_GALAXY\ph.csv'
output_csv_path = r'D:\Masrafe\Coding\Git_Hub_code\ml_project\GURDIANS_OF_THE_GALAXY\ph_soil_data_added_data.csv'

# Try reading the CSV file with debugging
try:
    df = pd.read_csv(input_csv_path, encoding='ISO-8859-1')
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

# Check if 'pH' column exists
if 'pH' not in df.columns:
    print("Error: The CSV file must contain a 'pH' column.")
    exit()

# Add a new 'Plant Type' column based on pH values
df['Plant Type'] = df['pH'].apply(lambda x: classify_plant(x))

# Save the updated dataframe to a new CSV file
df.to_csv(output_csv_path, index=False)

# Print confirmation message
print(f"Updated CSV file saved to {output_csv_path}")
