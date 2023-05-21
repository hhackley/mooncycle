import ephem
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent='my_app')
    location = geolocator.geocode(address)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

# Prompt the user to enter an address
print("---- Getting Latitude and Longitude ----")
address = input("Enter an address: ")

# Retrieve the latitude and longitude for the address
coordinates = get_coordinates(address)
if coordinates:
    latitude, longitude = coordinates
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Unable to retrieve coordinates for the address.")
    