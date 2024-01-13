import csv
import matplotlib.pyplot as plt

def read_and_analyze_data(filename):
    """
    Processes environmental data from a CSV file.
    Calculates averages and identifies extremes in temperature and humidity.
    """
    data = []
    temperatures = []
    humidities = []
    locations = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            temp = float(row['Temperature'])
            humid = float(row['Humidity'])
            locations.append(row['Location'])
            temperatures.append(temp)
            humidities.append(humid)
            
            # Define extremes
            extreme_temp = temp > 30 or temp < 20
            extreme_humid = humid > 80 or humid < 40

            # Append analyzed data
            data.append({
                'Location': row['Location'],
                'Temperature': temp,
                'Humidity': humid,
                'Extreme Temperature': 'Yes' if extreme_temp else 'No',
                'Extreme Humidity': 'Yes' if extreme_humid else 'No'
            })

    # Plotting
    fig, ax = plt.subplots()
    ax.bar(locations, temperatures, label='Temperature')
    ax.bar(locations, humidities, label='Humidity', alpha=0.5)
    ax.set_ylabel('Values')
    ax.set_title('Temperature and Humidity at Different Locations')
    ax.legend()

    # Save the plot
    plt.savefig('environmental_data_plot.png')

    return data

# File path for data file
file_path = 'C:\\Users\\mariaepi\\OneDrive - Universitetet i Oslo\\Documents\\OpenScience\\DataStewardCertificate\\Module2\\Phyton assignment\\environmental_data.csv'

# Analyze data and create plot
analysis_results = read_and_analyze_data(file_path)

# Output results
for result in analysis_results:
    print(f"{result['Location']}: Temp {result['Temperature']}°C, Humidity {result['Humidity']}%, Extremes - Temp: {result['Extreme Temperature']}, Humidity: {result['Extreme Humidity']}")

    main()
