import json
# Load the JSON data from file
with open("dummy.json") as f:
    data = json.load(f)

current_temp =data['main'][0]['temp']
peak_temp = data['main'][0]['highest_temp']

print(f"Temperature: {current_temp}°C")
print(f"Peak Temperature: {peak_temp}°C")
