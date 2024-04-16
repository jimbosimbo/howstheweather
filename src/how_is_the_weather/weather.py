import os
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def categorize_temperature(temp):
    if temp > 20:
        return "nice and warm"
    elif temp > 10:
        return "mild"
    else:
        return "cold!"

def print_weather(data):
    try:
        temperature = data['main']['temp']
        category = categorize_temperature(temperature)
        print(f"The weather is {category}")
    except KeyError:
        print("Error: Could not parse the weather data. Check your API key and city name.")

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: No API key provided. Set the OPENWEATHER_API_KEY environment variable.")
        return

    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    print_weather(weather_data)

if __name__ == "__main__":
    main()
