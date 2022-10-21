import requests


# Settings - Project - Python Interpreter
# pip
# setup-tools
# click +

def get_temperature(json_data):
    temp_in_celcius = json_data['main']['temp']
    return temp_in_celcius


def get_weather_type(json_data):
    weather_type = json_data['weather'][0]['description']
    return weather_type


def get_wind_speed(json_data):
    wind_speed = json_data['wind']['speed']
    return wind_speed


def get_coordinates(json_data):
    coords = json_data['coord']
    lat, lon = coords['lat'], coords['lon']
    return lat, lon


def get_humidity(json_data):
    humidity = json_data['main']['humidity']
    return humidity


def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    lat, long = get_coordinates(json_data)
    humidity = get_humidity(json_data)
    weather_details = ''
    return weather_details + (
        "The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph. Coords are: {}, {}. Humidity is {}%".format(
            city, weather_type, temperature, wind_speed, lat, long, humidity))


def main(city):
    """Get current weather in a city."""
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    units_format = "&units=metric"
    final_url = api_address + city + units_format
    json_data = requests.get(final_url).json()
    weather_details = get_weather_data(json_data, city)
    # print formatted data
    return weather_details
