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

def get_moon_phase(latitude, longitude, date):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    observer.date = date
    
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

# Prompt the user to enter a date
    print("\n---- Getting Date ----")
    date_input = input("Enter a date (in the format MM DD YYYY): ")
    date_parts = date_input.split()
    date = "-".join([date_parts[2], date_parts[0], date_parts[1]])  # Rearrange date parts to YYYY-MM-DD

    print("\n---- Moon Phase ----")
# Get the moon phase for the provided coordinates and date
    moon_phase = get_moon_phase(latitude, longitude, date)
    print("Moon Phase on", date + ":", moon_phase)
else:
    print("Unable to retrieve coordinates for the address.")