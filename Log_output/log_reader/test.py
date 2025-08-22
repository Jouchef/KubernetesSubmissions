import requests

x = requests.get('http://127.0.0.1:8081/pingpong').text

x = x[5:]
print(x)


