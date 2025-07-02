# Population Visualization Project

This project visualizes the total population of India from 1960 to 2023 using data from the World Bank.

## Dataset
- **Source:** [World Bank - Population, total](https://data.worldbank.org/indicator/SP.POP.TOTL)
- **File:** `API_SP.POP.TOTL_DS2_en_csv_v2_5830.csv`

## Files
- `population_bar_chart.py`: Python script to generate a bar chart of India's population over time.
- `population_india.png`: Output image showing the population bar chart.
- `API_SP.POP.TOTL_DS2_en_csv_v2_5830.csv`: Raw dataset downloaded from the World Bank.

## How to Run
1. Ensure you have Python 3 and the required libraries:
   ```bash
   pip install pandas matplotlib
   ```
2. Run the script:
   ```bash
   python population_bar_chart.py
   ```
3. The output image `population_india.png` will be generated in the same directory.

## Customization
- To visualize a different country, change the `country` variable in `population_bar_chart.py`.

## License
This project uses data provided under the [CC BY-4.0](https://creativecommons.org/licenses/by/4.0/) license by the World Bank. 