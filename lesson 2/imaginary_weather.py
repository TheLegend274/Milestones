import random

import random

# Data Collection
weather = []


def generate_weather_data(num_days):
    # checking if the input is valid
    if not isinstance(num_days,int) or ( num_days < 0):
        raise ValueError("Number have to be greater than 1")

    # Loop through each day
    for i in range(1, num_days + 1):
        # get a random temp
        temp = random.randint(20, 40)
        # get humidity
        humid = random.randint(30, 90)
        data = {"day": i, "temperature": temp, "humidity": humid}
        weather.append(data)

    return weather


# Data Processing
def filter_data(weather_data, temp_threshold):
    if not isinstance(weather_data,list):
        raise ValueError("Incorrect weather data")
    filter_weather = []
    # Loop thorough the data
    for i in weather_data:
        # see if the temp is > threshold
        if (i["temperature"] < temp_threshold):
            # add the data to the filter data
            filter_weather.append(i)
    return filter_weather


# Data Analysis
def calculate_average_humidity(weather_data):
    if not isinstance(weather_data, list) :
        raise ValueError("Incorrect Format")
    # Store all the humidity values
    humid = 0
    total = 0
    # Loop through the dictionary
    for i in weather_data:
        # Get all the humid values
        total += i["humidity"]
        humid = total/len(weather_data)
    return humid




def sort_data_by_temperature(weather_data):
    """Sorts the weather data by temperature in descending order."""
    if not isinstance(weather_data, list) :
        raise ValueError("Incorrect Format")
    sorted_data = sorted(weather_data,key=lambda x:x["temperature"], reverse = True)
    return sorted_data





num_days = int(input("Enter the amount of days: "))
weather_data = generate_weather_data(num_days)
print("Original Data: " + str(weather_data))

# Filter
threshold = int(input("Enter the threshold: "))
print('Filtered Data: ' + str(filter_data(weather, threshold)))

# Calculate Humidity
print("Average Humidity: " + str(calculate_average_humidity(weather)))
#Sort Data
print("Sorted Data By Temperature: " + str(sort_data_by_temperature(weather)))
