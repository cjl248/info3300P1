# output {date, #subscriber, #customer, #total, season (string), color (hex value)
import json

data = []
weather_data = []
final_output = []

json_block = ""
json_weather_block = ""

#with open("data/properties_trip_data.json", 'r') as f:
with open("data/properties_trip_data.json", 'r') as f:
	for line in f:
		if (line[-1]==" "):
			line = line.strip("\n")
			json_block+=line
		else:
			json_block+=line.strip("\n")
data=json.loads(json_block)

output = {}
previous_date = data[0]["Start Date"].encode('ascii','ignore')
cut = previous_date.find(" ")
previous_date = previous_date[0:cut]

#generate weather data first, then search it for each output
temp_dict={}
with open("data/properties_weather.json", 'r') as f:
	for line in f:
		if (line[-1]==" "):
			line = line.strip("\n")
			json_weather_block+=line
		else:
			json_weather_block+=line.strip("\n")
weather_data=json.loads(json_weather_block)
#make count for each day (new array?)
for w_item in weather_data:
	weather_date =w_item["Date"].encode('ascii','ignore')
	temp = w_item["Mean_Temperature_F"]
	temp_dict[weather_date] = temp
#print temp_dict

output["subscribers"]=0
output["customers"]=0
output["date"]=previous_date

#output["total"]=1

#eventually replace with color that combines season and temp
#output["temp"] = temp_dict[previous_date]

if (previous_date[:-6] == "3" or "4" or "5"):
	output["season"] = "Spring"
#summer = 6/1-8/31
elif (previous_date[:-6] == "6" or "7" or "8"):
	output["season"] = "Summer"
#autumn = 9/1-11/30
elif (previous_date[:-6] == "9" or "10" or "11"):
	output["season"] = "Fall"
#winter = 12/1 - 2/28
else:
	output["season"] = "Winter"

for item in data:
	#just get initial date
	date = item["Start Date"].encode('ascii','ignore')
	cut = date.find(" ")
	date = date[0:cut]
	#output["date"]=date
	s_type = item["Subscription Type"]
	#repeate date: update #, update subscribers, update season
	if (output["date"] == previous_date):
		#output["total"]+=1
		if (s_type=="Subscriber"):
			if ("subscribers" in output.keys()):
				output["subscribers"]+=1
			else:
				output["subscribers"]=1
		else:
			if ("customers" in output.keys()):
				output["customers"]+=1
			else:
				output["customers"]=1
		#print output
	else:
		final_output.append(output)
		output = {}
		#initalize
		output["date"]=date
		#output["total"]=0
		output["customers"]=0
		output["subscribers"]=0
		#eventually create placeholder
		#output["temp"] = temp_dict[date]
		#only calculate season for new outputs (also do it for the first one)
		#spring = 3/1-5/31
		if ((date.startswith("3")) or (date.startswith("4")) or (date.startswith("5"))):
			output["season"] = "Spring"
			#print "SEASON"
		#summer = 6/1-8/31
		elif ((date.startswith("6")) or (date.startswith("7")) or (date.startswith("8"))):
			output["season"] = "Summer"
		#autumn = 9/1-11/30
		elif ((date.startswith("9")) or (date.startswith("10")) or (date.startswith("11"))):
			output["season"] = "Fall"
		#winter = 12/1 - 2/28
		else:
			output["season"] = "Winter"
		#print date
		#output["total"]+=1
		if (s_type=="Subscriber"):
			output["subscribers"]+=1
		else:
			output["customers"]+=1
	previous_date = date
	#print output["date"]
final_output.append(output)
print len(final_output)

#json.dump(final_output,"final.json")


#loop thru final_output and create new output
end_result = []
f=open("final.json",'w')
for d in final_output:
	text = json.dumps(d)
	f.write(text + ",\n")
	#print d
	#calculate total here
	#d["temp"] = temp_dict[d["date"]]
	#temp = d["temp"]
	#look up date's temp in temp_dict

	#find max and min temp for each season
	temp_spring_max = 0
	temp_spring_min = 0
	temp_summer_max = 0
	temp_summer_min = 0
	temp_fall_max = 0
	temp_fall_min = 0
	temp_winter_max = 0
	temp_winter_min = 0
	if (d["season"] == "Spring"):
		if (temp > temp_spring_max):
			temp_spring_max = temp
		if (temp < temp_spring_min):
			temp_spring_min = temp
	if (d["season"] == "Summer"):
		if (temp > temp_summer_max):
			temp_summer_max = temp
		if (temp < temp_summer_min):
			temp_summer_min = temp
	if (d["season"] == "Fall"):
		if (temp > temp_fall_max):
			temp_fall_max = temp
		if (temp < temp_fall_min):
			temp_fall_min = temp
	if (d["season"] == "Winter"):
		if (temp > temp_winter_max):
			temp_winter_max = temp
		if (temp < temp_winter_min):
			temp_winter_min = temp

f.close()

print "temp_spring_max = " + str(temp_spring_max)
print "temp_spring_min = " + str(temp_spring_min)
print "temp_summer_max = " + str(temp_summer_max)
print "temp_summer_min = " + str(temp_summer_min)
print "temp_fall_max = " + str(temp_fall_max)
print "temp_fall_min = " + str(temp_fall_min)
print "temp_winter_max = " + str(temp_winter_max)
print "temp_winter_min = " + str(temp_winter_min)



