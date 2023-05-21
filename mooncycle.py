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

def get_moon_phase(latitude, longitude):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)

    moon = ephem.Moon()
    moon.compute(observer)

    phase = moon.phase / 100  # Convert phase value to fraction

    if 0 <= phase < 0.03 or phase >= 0.97:
        moon_phase = 'New Moon'
    elif 0.03 <= phase < 0.5:
        moon_phase = 'First Quarter Waxing Crescent'
    elif 0.5 <= phase < 0.53:
        moon_phase = 'First Quarter Half Moon'
    elif 0.53 <= phase < 0.97:
        moon_phase = 'First Quarter Waxing Gibbous'
    else:
        moon_phase = 'Full Moon'

    return moon_phase


# Prompt the user to enter an address
print("\n---- Getting Latitude and Longitude ----")
address = input("Enter an address: ")

# Retrieve the latitude and longitude for the address
coordinates = get_coordinates(address)
if coordinates:
    latitude, longitude = coordinates
    print("\n---- Coordinates ----")
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    # Get the moon phase for the provided coordinates
    moon_phase = get_moon_phase(latitude, longitude)
    print("\n---- Moon Phase ----")
    print("Moon Phase:", moon_phase)
    print("\n")
else:
    print("Unable to retrieve coordinates for the address.")
