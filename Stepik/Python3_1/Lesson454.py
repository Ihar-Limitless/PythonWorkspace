import json, requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Moscow',
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers['Content-Type'])
data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(params['q'] ,data['main']['temp']))