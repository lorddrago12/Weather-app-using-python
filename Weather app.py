import requests

api_key = 'b63c0b56b92b202359ee3f42951430fc'

user_input = input("Enter city name: ")

# Make the API request
weather_data = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric'
)

# Check if city exists
if weather_data.json().get('cod') == '404':
    print('City not found. Please check the city name and try again.')
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = round(weather_data.json()['main']['temp'])
    print(f"The weather in {user_input} is {weather} with a temperature of {temperature}°C.")
