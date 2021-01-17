from alpha_vantage.timeseries import TimeSeries

API_Key = 'H3RF2EQFQIC7O1R8'




ts = TimeSeries(key=API_Key, output_format='pandas')
data = ts.get_daily('IBM')
print(data[0].T)