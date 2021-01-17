import  requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print('HTTP Response code is: ',response)
print("*********************")
print(response.content)
print("*********************")
print(response.headers)