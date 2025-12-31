
import requests

url= "https://jsonplaceholder.typicode.com/posts"

response=requests.get(url=url)
print(response.json())