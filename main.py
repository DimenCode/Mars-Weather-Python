import datetime
import requests
import json

#I found the link using the inspector tool on this website : https://mars.nasa.gov/msl/weather/
data = requests.get("https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json")
data = data.text


data_dict_2 = json.loads(data)
data_dict_2 = data_dict_2['soles']
data_dict = data_dict_2[0]

#terrestrial date of the latest data avaiable
list = str(data_dict['terrestrial_date']).split("-")
data_date = datetime.date(int(list[0]), int(list[1]), int(list[2]))

#current date got from the computer which is running the script
current_date = datetime.date.today()
days_between = str(current_date - data_date).split(",")


#Date converted to a more readable format
list = str(current_date).split("-")
printed_current_date = current_date.strftime("%A") + " the " + list[2] + " of " + current_date.strftime("%B") + " " + list[0] + " (" + list[2] + "/" +list[1] + "/" + list[0] + ")"
list = str(data_date).split("-")
printed_data_date = data_date.strftime("%A") + " the " + list[2] + " of " + data_date.strftime("%B") + " " + list[0] + " (" + list[2] + "/" +list[1] + "/" + list[0] + ")"


#print part
print("""
___  ___                    _    _            _   _               
|  \/  |                   | |  | |          | | | |              
| .  . | __ _ _ __ ___     | |  | | ___  __ _| |_| |__   ___ _ __ 
| |\/| |/ _` | '__/ __|    | |/\| |/ _ \/ _` | __| '_ \ / _ \ '__|
| |  | | (_| | |  \__ \    \  /\  /  __/ (_| | |_| | | |  __/ |   
\_|  |_/\__,_|_|  |___/     \/  \/ \___|\__,_|\__|_| |_|\___|_| 
""")


print("Current date      : " + printed_current_date)
print("---------------------------------------------------------------")
print("date of the data  : " + printed_data_date)
print("---------------------------------------------------------------")
print("data is from " + days_between[0] + " ago")
print("---------------------------------------------------------------")
print("Sol number " + data_dict['sol'] + " :")
print("")
print("-Day cycle                                   -Temperatures ")
print("  Sun rised at : " + data_dict["sunrise"] + "                          Min : " + data_dict['min_temp'] + " °C")
print("  Sun sat at   : " + data_dict["sunset"] + "                          Max : " + data_dict['max_temp'] + " °C")
print("")
print("Local UV irradiance index : " + data_dict['local_uv_irradiance_index'])
print("Atmosphere Opacity : " + data_dict['atmo_opacity'])
print("Pressure : " + data_dict['pressure'] + " Pa")
print("---------------------------------------------------------------")
print("Season :" + data_dict['season'])
print("Id : " + data_dict['id'])

# while loop so the window don't shut itself after less than a second, there is probably a better way don't judge me please :')
dontjudgemeplease = True
while dontjudgemeplease == True :
    dontjudgemeplease = True

# entirely made (except the parts stolen from internet guys from 3 years ago lol) by DimenCode
# https://github.com/DimenCode/Mars-Weather-Python