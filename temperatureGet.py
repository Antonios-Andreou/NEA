
import pprint
from ipGet import ipInfo
import http.client

latitude, longitude = ipInfo()


conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")

headers = {
    'X-IBM-Client-Id': "11c9e8f4fccd4446e952aa4e494384d8",
    'X-IBM-Client-Secret': "01337190c2b7d7b3e31ce6cceaba15e9",
    'accept': "application/json"
    }
#above is correct

conn.request("GET", f"/v0/forecasts/point/hourly?excludeParameterMetadata=TRUE&includeLocationName=FALSE&latitude={latitude}&longitude={longitude}", headers=headers)

res = conn.getresponse()
data = res.read()

weather_info = data.decode("utf-8")
#pprint.pprint(weather_info)

weather_info = eval(weather_info)

temperate = weather_info["features"][0]["properties"]["timeSeries"][2]["screenTemperature"]
print(temperate)
