import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
        "userId" : 1
}

response = requests.get(url, data=data)

print(response.status_code)
print(response.text)



