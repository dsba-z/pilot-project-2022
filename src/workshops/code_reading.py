def task1(city):
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

    def get_humidity(json_data):
        hum = json_data['main']['humidity']
        return hum

    def get_coordinates(json_data):
        coords = tuple(json_data['coord'].values())
        return coords

    def get_weather_data(json_data, city):
        description_of_weather = json_data['weather'][0]['description']
        weather_type = get_weather_type(json_data)
        temperature = get_temperature(json_data)
        wind_speed = get_wind_speed(json_data)
        humidity = get_humidity(json_data)
        coords = get_coordinates(json_data)
        weather_details = ''
        return weather_details + (
            "The weather in {} ({}, {}) is currently {} with a temperature of {} degrees, humidity of {}% and wind "
            "speeds reaching {} km/ph".format(
                city, *coords, weather_type, temperature, humidity, wind_speed))

    def main():
        nonlocal city
        api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
        units_format = "&units=metric"
        final_url = api_address + city + units_format
        try:
            json_data = requests.get(final_url).json()
            weather_details = get_weather_data(json_data, city)
            # print formatted data
            return weather_details
        except:
            return ''

    return main()


def task2(repo):
    from github import Github
    import argparse
    import os
    import sys

    github = Github()

    def sanitize_for_md(s):
        s = s.replace("*", "\*")
        return s

    try:
        r = github.get_repo(repo)
    except:
        return ''

    content = "Name | Stargazers | Description | Topics\n" + "|".join(["----"] * 4) + "\n" + " | ".join([
        "[{}]({})".format(r.full_name, r.html_url),
        str(r.stargazers_count),
        sanitize_for_md(r.description),
        ", ".join(r.topics)
    ])
    return content
