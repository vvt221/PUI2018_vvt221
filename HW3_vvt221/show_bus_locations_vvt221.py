

from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  show_bus_locations_vvt221.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE>")
    sys.exit()
    
api_key=str(sys.argv[1])
bus_no=str(sys.argv[2])


mta_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+api_key+"&VehicleMonitoringDetailLevel=calls&LineRef="+ bus_no

response = urllib.urlopen(mta_url).read()
mta_data = json.loads(response.decode('utf-8'))
mta_vehicle_details = mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

num_active_buses = len(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print("Bus Line : " + str(bus_no))
print("Number of Active Buses: "+ str(num_active_buses))
for vehicle in range(num_active_buses):
    print("Bus "+ str(vehicle) +" is at latitude "+ str(mta_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) +" and longitude "+ str(mta_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
