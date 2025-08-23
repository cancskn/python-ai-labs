import requests

URL = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(URL)

# print(response.status_code)
# print(response.json())
data = response.json()
# print(data[0]["name"])
# print(data[0]["email"])

names = []
for user in data:
    # print(user['name'])
    # print(user['company']['name'])
    if user['name'] == 'Leanne Graham':
        print(user['address']['city'])

    if user['id'] == 4:
        print(user['address']['zipcode'])

    names.append(user['name'])

print(len(names))



