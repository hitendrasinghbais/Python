# request module
import requests
# response=requests.get("https://www.google.com/search?q=google&oq=goo&gs_lcrp=EgZjaHJvbWUqEAgAEAAYgwEY4wIYsQMYgAQyEAgAEAAYgwEY4wIYsQMYgAQyEwgBEC4YgwEYxwEYsQMY0QMYgAQyDQgCEAAYgwEYsQMYgAQyBggDEEUYOTIGCAQQRRg7MgYIBRBFGDsyDQgGEAAYgwEYsQMYgAQyCggHEAAYsQMYgAQyDQgIEAAYgwEYsQMYgAQyDQgJEAAYgwEYsQMYgATSAQk1NjMwajBqMTWoAgiwAgHxBa9FyvTSGgTm8QWvRcr00hoE5g&sourceid=chrome&source=chrome.rb&ie=UTF-8")

# print(response.text)
# -----------------------------------------------------------------------
# url="https://jsonplaceholder.typicode.com/posts"

# data={
#     "title":'harry',
#     "body":'bhai',
#     "userId" : 12,
# }
# header={
    # 'Content-type':'application/json; charset=UTF-8',
#     }
# response=requests.post(url,headers=header,json=data)

# print(response.text)

# -----------------------------------------------------------------
# url="https://official-joke-api.appspot.com/random_joke"

# response=requests.get(url)

# data=response.json()
# print(data["setup"])
# print(data["punchline"])

# -----------------------------------------------
# name=input("Enter your name : ")
# url=f"https://api.agify.io/?name={name}"

# response=requests.get(url)

# data=response.json()

# print(f"age : {data["age"]}")
# -------------------------------------------------------
url="https://api.github.com/users/hitendrasinghbais "

response=requests.get(url)
data=response.json()

print(f"login : {data["login"] }")
print(f"public repo : {data["public_repos"] }")
print(f"following : {data["following"] }")
