import json
# Load the JSON data from file
with open("dataset.json") as f:
    data = json.load(f)
for i in range(len(data['weather'])):
    current_temp =data['weather'][i]['temp']
    peak_temp = data['weather'][i]['highest_temp']
    place=data['weather'][i]['place']
    print(f"Place: {place}")
    print(f"Temperature: {current_temp}°C")
    print(f"Peak Temperature: {peak_temp}°C")
    print(" ")