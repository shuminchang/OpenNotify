# Use data from OpenNotify to calculate ISS velocity
from math import radians, cos, sin, asin, sqrt
import requests
import time

# haversine formula
def distance(lat1, lng1, lat2, lng2):
    """
    Calculate the great circle distance (in miles) between two points
    on the earth (specified in decimal degrees)
    """

    # convert decimal degrees to radians
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlng = lng2 - lng1
    dlat = lat2 - lat1

    # haversine formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
    c = 2 * asin(sqrt(a))
    return 6371 * c

# Get the information of position1
position1 = requests.get("http://api.open-notify.org/iss-now.json")
# Get the starting time
start = time.time() 
data1 = position1.json()
iss_position1 = data1['iss_position']
latitude1 = iss_position1['latitude']
longitude1 = iss_position1['longitude']
lat1 = float(latitude1)
lng1 = float(longitude1)
time1_raw = data1['timestamp']
time1 = int(time1_raw)

# Set a timer. Because the time between two script is less than 1 sec.
# And the minimum of timestamp is 1 sec.
# How to calculate the time between two scrpit?
time.sleep(1)

# Get the information of position2
position2 = requests.get("http://api.open-notify.org/iss-now.json")
# Get the ending time
end = time.time()
data2 = position2.json()
iss_position2 = data2['iss_position']
latitude2 = iss_position2['latitude']
longitude2 = iss_position2['longitude']
lat2 = float(latitude2)
lng2 = float(longitude2)
time2_raw = data2['timestamp']

# Calculating the traveling time between two positions
total = end - start

# distance between two point(km)
dis = distance(lat1, lng1, lat2, lng2)

tt = 60 / total

v = (dis / total)*tt*60
print(dis)
print(tt)
print(v)

# Can only get ~17000 km/h? What went wrong?
