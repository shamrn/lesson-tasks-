
# В качестве примера хорошего и несложного API, созданного по принципам REST, рассмотрим сервис SWAPI — Star Wars API.
# Ваша задача: узнать диаметр родной планеты Люка Скайуокера. Подумайте, как это сделать. Документация — к вашим услугам.



import requests

URL = 'https://swapi.dev/api/'

result = requests.get(URL).json()

result = requests.get(result['people']).json()

for item in result['results']:
    result = requests.get(item['homeworld']).json()
    print(f'{item["name"]} с планеты {result["name"]} , диаметр планеты {result["diameter"]}')
