import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if(response.status_code != requests.codes.OK):
    print("Something went wrong")
else:
    print(response.json())



requestBody={
    'title': 'our title',
    'body': 'our content',
    'id': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json = requestBody)

if(response.status_code != requests.codes.created):
    print("Something went wrong")
else:
    print(response.json())