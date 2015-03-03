import json
json_block=""
with open("ordered_data.json", 'r') as f:
	for line in f:
		if (line[-1]==" "):
			line = line.strip("\n")
			json_block+=line
		else:
			json_block+=line.strip("\n")
data=json.loads(json_block)

f = open("seasons_labelled.json",'w')
for item in data:
	output = {}
	output["Date"] = item["Date"]
	output["Color"] = item["Color"]
	output["Subscribers"] = item["Subscribers"]
	output["Customers"] = item["Customers"]
	output["Total"] = item["Subscribers"] + item["Customers"]
	date=item["Date"]
	if ((date.startswith("3")) or (date.startswith("4")) or (date.startswith("5"))):
		output["season"] = "Spring"
	elif ((date.startswith("6")) or (date.startswith("7")) or (date.startswith("8"))):
		output["season"] = "Summer"
	elif ((date.startswith("9")) or (date.startswith("10")) or (date.startswith("11"))):
		output["season"] = "Fall"
	else:
		output["season"] = "Winter"
	text = json.dumps(output)
	f.write(text + ",\n")
f.close()