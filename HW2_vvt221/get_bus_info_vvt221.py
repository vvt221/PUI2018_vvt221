from __future__ import print_function
import json
import urllib.request
import sys
import os

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python  get_bus_info_vvt221.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()
    
api_key = sys.argv[1]
bus_no = sys.argv[2]
file_name= sys.argv[3]

fout = open(file_name, "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
mta_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+api_key+"&VehicleMonitoringDetailLevel=calls&LineRef="+ bus_no

response = urllib.request.urlopen(mta_url).read()

mta_data = json.loads(response.decode('utf-8'))

mta_vehicle_details = mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

num_active_buses = len(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

NextStopInfoListDictionary=[]
Next_Stop_Info_Dictionary={}

mta_vehicle_details = mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

no_active_buses = len(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])


print("Latitude,Longitude,Stop Name,Stop Status")
for vehicle in range(no_active_buses):

    onward_calls = len(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][vehicle]['MonitoredVehicleJourney']['OnwardCalls'])
    latitude = str(mta_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    longitude = str(mta_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    
    
    if bool(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][vehicle]['MonitoredVehicleJourney']['OnwardCalls']):
        stop_name = str(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][vehicle]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        
    
        stop_status = str(mta_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][vehicle]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
        fout.write(latitude+","+longitude+","+stop_name+","+stop_status+"\n")
        print(latitude+","+longitude+","+stop_name+","+stop_status)
        
    else:
        fout.write(latitude+","+longitude+",N/A,N/A\n")
        print(latitude+","+longitude+",N/A,N/A")
        
    
