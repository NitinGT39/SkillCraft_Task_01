import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the path to your downloaded file)
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_5830.csv', skiprows=4)

# Select a country, e.g., 'India'
country = 'India'
country_data = df[df['Country Name'] == country]

# Extract years and population values
years = [str(year) for year in range(1960, 2024)]
population = country_data[years].values.flatten()

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(years, population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Total Population of {country} (1960-2023)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('population_india.png') 