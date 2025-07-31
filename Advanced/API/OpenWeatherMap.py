import requests
url = 'https://api.openweathermap.org/data/2.5/weather'
appid = '6ad934a76186d5d2fb596a8e925a0cae'
q = 'tehran'
units = 'metric'
# response = requests.get(url = url, params = {'q':q, 'units':units, 'appid':appid}).json()
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={appid}&units={units}').json()
print(response['weather'][0]['description'])
print(response['main']['temp'])