import json
from email.mime import application

import requests

lat = input("Enter the latitude of your location: ")
lon = input("Enter the longitude of your location: ")
lat = float(lat)
lon = float(lon)
coord_lat = [lat + 0.02, lat - 0.02]
coord_lon = [lon + 0.02, lon - 0.02]
api_url = 'http://api.agromonitoring.com/agro/1.0/polygons?appid=0421e7f92d2b3cffdd65a4ba8cf004bd'
header = {'Content-Type': 'application/json'}
params = {
   "name": "Polygon Sample",
   "geo_json": {
      "type": "FeatureCollection",
      "features": [{
         "type":"Feature",
         "properties": {},
         "geometry": {
            "type":"Polygon",
            "coordinates":
               [
                  [
                     [coord_lat[0], coord_lon[0]],
                     [coord_lat[0], coord_lon[1]],
                     [coord_lat[1], coord_lon[1]],
                     [coord_lat[1], coord_lon[0]],
                     [coord_lat[0], coord_lon[0]]
                  ]
               ]
         }
      }
      ]
   }
}
# "0421e7f92d2b3cffdd65a4ba8cf004bd"
res = requests.post(api_url, data=json.dumps(params), headers=header)
# print(res.request.headers['application/json'])
# print(res.request.body)
print(res.json())
temp = res.json()
pol_id = str(temp["id"])
api_id = '0421e7f92d2b3cffdd65a4ba8cf004bd'
start_time = '1556658000'
end_time = '1564606800'
# 1556658000 1564606800
# 55.6417 37.6728
temp_link = 'http://api.agromonitoring.com/agro/1.0/weather/history?'
temp_api = temp_link + 'polyid=' + pol_id +'&appid=' + api_id + '&start=' + start_time + '&end=' + end_time
print(temp_api)
ans = requests.get(temp_api)
print(ans.json())