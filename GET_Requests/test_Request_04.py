import requests
import resp as resp
from alpha_vantage.timeseries import TimeSeries
import json
from requests_toolbelt.utils import dump
import pytest
import sys




def test_mytest_1_Interval_60_Min():

        API_URL = "https://www.alphavantage.co/query"
        symbols = ['IBM']

        for symbol in symbols:
                data = { "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval" : "60min",
                "datatype": "json",
                "apikey": "H3RF2EQFQIC7O1R8" }
                response = requests.get(API_URL, data)
                data = response.json()


                print('URL is: ',response.url)
                print('**************************************************************************')
                print('Headers are: ')
                print(response.request.headers)
                print('**************************************************************************')
                print('Content is: ',response.content)
                print('**************************************************************************')
                print('Response code is: ',response.status_code)
                print('**************************************************************************')
                print('Response is: ')
                print(data)
                print('**************************************************************************')
                print('Symbol is: ',symbol)
                print('**************************************************************************')
                print('IBM_TIME_SERIES_60_Mins_DAILY:')
                a = (data['Time Series (60min)'])
                keys = (a.keys())
                for key in keys:

                 print(a[key]['1. open'] + " " + a[key]['2. high'] + " " + a[key]['3. low'] + " " + a[key][
                                '4. close'] + " " + a[key]['5. volume'])

                print('**************************************************************************')
                print('Print the Request with Entire Results:')
                data = dump.dump_all(response)
                #sys.stdout = open("results.html", "w")
                print(data.decode('utf-8'))





def test_mytest_2_Interval_1_Min():

        API_URL = "https://www.alphavantage.co/query"
        symbols = ['TCS']

        for symbol in symbols:
                data = { "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval" : "1min",
                "datatype": "json",
                "apikey": "H3RF2EQFQIC7O1R8" }
                response = requests.get(API_URL, data)
                data = response.json()


                print('URL is: ',response.url)
                print('**************************************************************************')
                print('Headers are: ')
                print(response.request.headers)
                print('**************************************************************************')
                print('Content is: ',response.content)
                print('**************************************************************************')
                print('Response code is: ',response.status_code)
                print('**************************************************************************')
                print('Response is: ')
                print(data)
                print('**************************************************************************')
                print('Symbol is: ',symbol)
                print('**************************************************************************')
                print('IBM_TIME_SERIES_1_Mins_DAILY:')
                a = (data['Time Series (60min)'])
                keys = (a.keys())
                for key in keys:

                 print(a[key]['1. open'] + " " + a[key]['2. high'] + " " + a[key]['3. low'] + " " + a[key][
                                '4. close'] + " " + a[key]['5. volume'])

                print('**************************************************************************')
                print('Print the Request with Entire Results:')
                data = dump.dump_all(response)
                #sys.stdout = open("results.html", "w")
                print(data.decode('utf-8'))




def test_mytest_3_Invalid_URI():

        API_URL = "https://www.alphavantage.co/querY"
        symbols = ['IBM']

        for symbol in symbols:
                data = { "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval" : "60min",
                "datatype": "json",
                "apikey": "H3RF2EQFQIC7O1R8" }
                response = requests.get(API_URL, data)
                data = response.json()


                print('URL is: ',response.url)
                print('**************************************************************************')
                print('Headers are: ')
                print(response.request.headers)
                print('**************************************************************************')
                print('Content is: ',response.content)
                print('**************************************************************************')
                print('Response code is: ',response.status_code)
                print('**************************************************************************')
                print('Response is: ')
                print(data)
                print('**************************************************************************')
                print('Symbol is: ',symbol)
                print('**************************************************************************')
                print('IBM_TIME_SERIES_60_Mins_DAILY:')
                a = (data['Time Series (60min)'])
                keys = (a.keys())
                for key in keys:

                 print(a[key]['1. open'] + " " + a[key]['2. high'] + " " + a[key]['3. low'] + " " + a[key][
                                '4. close'] + " " + a[key]['5. volume'])

                print('**************************************************************************')
                print('Print the Request with Entire Results:')
                data = dump.dump_all(response)
                #sys.stdout = open("results.html", "w")
                print(data.decode('utf-8'))


def test_mytest_4_Other_Function():

        API_URL = "https://www.alphavantage.co/query"
        symbols = ['IBM']

        for symbol in symbols:
                data = { "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval" : "60min",
                "datatype": "pandas",
                "apikey": "H3RF2EQFQIC7O1R8" }
                response = requests.get(API_URL, data)
                data = response.json()


                print('URL is: ',response.url)
                print('**************************************************************************')
                print('Headers are: ')
                print(response.request.headers)
                print('**************************************************************************')
                print('Content is: ',response.content)
                print('**************************************************************************')
                print('Response code is: ',response.status_code)
                print('**************************************************************************')
                print('Response is: ')
                print(data)
                print('**************************************************************************')
                print('Symbol is: ',symbol)
                print('**************************************************************************')
                print('IBM_TIME_SERIES_60_Mins_DAILY:')
                a = (data['Time Series (60min)'])
                keys = (a.keys())
                for key in keys:

                 print(a[key]['1. open'] + " " + a[key]['2. high'] + " " + a[key]['3. low'] + " " + a[key][
                                '4. close'] + " " + a[key]['5. volume'])

                print('**************************************************************************')
                print('Print the Request with Entire Results:')
                data = dump.dump_all(response)
                #sys.stdout = open("results.html", "w")
                print(data.decode('utf-8'))




def test_mytest_5_Without_API_Key():

        API_URL = "https://www.alphavantage.co/querY"
        symbols = ['IBM']

        for symbol in symbols:
                data = { "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval" : "60min",
                "datatype": "json" }
                response = requests.get(API_URL, data)
                data = response.json()


                print('URL is: ',response.url)
                print('**************************************************************************')
                print('Headers are: ')
                print(response.request.headers)
                print('**************************************************************************')
                print('Content is: ',response.content)
                print('**************************************************************************')
                print('Response code is: ',response.status_code)
                print('**************************************************************************')
                print('Response is: ')
                print(data)
                print('**************************************************************************')
                print('Symbol is: ',symbol)
                print('**************************************************************************')
                print('IBM_TIME_SERIES_60_Mins_DAILY:')
                a = (data['Time Series (60min)'])
                keys = (a.keys())
                for key in keys:

                 print(a[key]['1. open'] + " " + a[key]['2. high'] + " " + a[key]['3. low'] + " " + a[key][
                                '4. close'] + " " + a[key]['5. volume'])

                print('**************************************************************************')
                print('Print the Request with Entire Results:')
                data = dump.dump_all(response)
                #sys.stdout = open("results.html", "w")
                print(data.decode('utf-8'))