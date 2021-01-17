import pytest
import requests
import time
import pyhttptest
import unittest




url = "https://www.alphavantage.co/querY?function=TIME_SERIES_DAILY&symbol=IBM&apikey=H3RF2EQFQIC7O1R8"
start_time = time.time()
response = requests.get(url)
print('HTTP Request URL is: ',response.url)
print("*********************")
print('HTTP Request Path_URL is: ',response.request.path_url)
print("*********************")
print('HTTP Response code is: ',response)
print("*********************")
end_time = time.time()
final = end_time - start_time
print('Response Total time is',final)
print("*********************")
print('HTTP Response Body is: ',response.content)
print("*********************")
print('HTTP Response Headers are: ',response.headers)