import phonenumbers
from myphone import number
from phonenumbers import geocoder

#1. Determine country by country phone code
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,'en')

print(location)

#2. Telecommunications service provider identification
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
host = carrier.name_for_number(service_pro,'en')
print(host)

import opencage
from opencage.geocoder import OpenCageGeocode

#3 Output result from phone number (array)
#a. Get key_API
key_API = '39fdd131c37c448daf39738645c3f3a4'
geocoder = OpenCageGeocode(key_API)
query = str(location)

#b. print Result
result = geocoder.geocode(query)
#print(result)

#c. determine latitude and longitude
lat = result[9]['geometry']['lat']
lng = result[9]['geometry']['lng']
print(lat,lng)


#4. Export html map file
import folium

MyMap = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat,lng],popup = location).add_to(MyMap)
MyMap.save('C:\\Users\\Admin\\Desktop\\FILEQUANG\\New folder\\my_location.html')
