def task1():
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
            "The weather in {} ({}, {}) is currently {} with a temperature of {} degrees, humidity of {}% and wind speeds reaching {} km/ph".format(
                city, *coords, weather_type, temperature, humidity, wind_speed))

    def main():
        api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
        city = input("City Name : ")
        units_format = "&units=metric"
        final_url = api_address + city + units_format
        json_data = requests.get(final_url).json()
        weather_details = get_weather_data(json_data, city)
        # print formatted data
        print(weather_details)

    main()


def task2():
    from github import Github
    import argparse
    import os
    import sys

    repos = ['hastagAB/Awesome-Python-Scripts', 'google/googletest', 'dsba-z/workshops']
    github = Github()

    def sanitize_for_md(s):
        s = s.replace("*", "\*")
        return s

    # print("Generated on {}.\n".format(time.strftime("%Y-%m-%d")))
    print("Name | Stargazers | Description | Topics")
    print("|".join(["----"] * 4))
    for r_name in sorted(repos, key=lambda v: v.upper()):
        try:
            r = github.get_repo(r_name)
        except:
            sys.stderr.write("Error: Repository '{}' not found.\n".format(r_name))
            sys.exit(-1)
        content = " | ".join([
            "[{}]({})".format(r.full_name, r.html_url),
            str(r.stargazers_count),
            sanitize_for_md(r.description),
            ", ".join(r.topics)
        ])
        print(content)
