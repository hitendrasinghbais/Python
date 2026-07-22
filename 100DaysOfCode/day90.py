# Exercise 10
import requests
url="https://newsapi.org/v2/top-headlines?country=us&apiKey=50e972fb1fd743589aaf86d80b0b74e2"

response=requests.get(url)

data=response.json()
# print(data)
print(data["articles"][6]["title"])
print(data["articles"][6]["description"])
print(data["articles"][6]["content"])
