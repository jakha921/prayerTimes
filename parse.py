import requests
from pprint import pprint


longitude = 40.091922
latitude = 65.367213
elevation = 382
ip = '178.218.200.0'
school = 3

city = 'Navoi'
date = 'today' # 'today', 'tomorrow', 'this_week'

# url = f'https://api.pray.zone/v2/times/today.json?longitude={longitude}&latitude={latitude}&elevation=333'
url = f'https://api.pray.zone/v2/times/{date}.json?city={city}&latitude={latitude}&longitude={longitude}&elevation={elevation}&school={school}'

response_pray = requests.get(url)
times = response_pray.json()


city = times['results']['location']['city']
country = times['results']['location']['country']
timezone = times['results']['location']['timezone']

sunrise = times['results']['datetime'][0]['times']['Sunrise']
sunset = times['results']['datetime'][0]['times']['Sunset']


pprint(times)
