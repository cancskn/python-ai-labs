import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
print(response)
if response.status_code == 200:
    print(response.json())
else:
    print('unable to receive data')