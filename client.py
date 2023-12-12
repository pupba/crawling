import requests

url = 'http://127.0.0.1:8080/pirate'
data = {'country_name': 'India'}

try:
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.text
        print(result)
    else:
        print('Error:', response.status_code)
except requests.exceptions.ConnectTimeout as ct:
    print("error")