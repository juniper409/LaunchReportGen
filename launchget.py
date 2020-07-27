import urllib.parse
import requests
import json

title_line = '-' * 10

print("Welcome to Launch Report Generator!")
print("Press ESC or type 'exit' to exit the program.")
print()
print("Here are the next 10 launches:")

main_api = 'https://launchlibrary.net/1.4/launch/next/11'

next = '10'
url = main_api + urllib.parse.urlencode({'next': next})

json_data = requests.get(url).json()

index = 0
number = 0

while True:

    launch_name = json_data['launches'][index]['name']
    # launch_date = json_data['launches'][index]['net']
    # launch_from = json_data['launches'][index]['location']['pads'][0]['name']

    index += 1

    if index == 11:
        break

    print(int(index), launch_name)
print()
select = int(input("Enter Launch Number (1-10): "))

# Accounts for 0 in the index lists. Allows user to select 1 and get index 0. Takes input and subtracts 1 from it.
select = select - 1

index = select

launch_name = json_data['launches'][index]['name']
launch_date = json_data['launches'][index]['net']
launch_from = json_data['launches'][index]['location']['pads'][0]['name']
launch_vehicle = json_data['launches'][index]['rocket']['name']
launch_payload = json_data['launches'][index]['missions'][0]['name']
launch_description = json_data['launches'][index]['missions'][0]['description']

if select == 1:
    index = 1
elif select == 2:
    index = 2
elif select == 3:
    index = 3
elif select == 4:
    index = 4
elif select == 5:
    index = 5
else:
    print("Invalid Input. Please enter a numerical selection 1-5")


print(title_line)
print(launch_name)
print(title_line)
print('Launch Date & Time: ', launch_date)
print('From:               ', launch_from)
print('Vehicle:            ', launch_vehicle)
print('Payload:            ', launch_payload)
print('Description:        ', launch_description)