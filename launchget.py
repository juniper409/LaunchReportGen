import urllib.parse
import requests
import json


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
    #launch_date = json_data['launches'][index]['net']
    #launch_from = json_data['launches'][index]['location']['pads'][0]['name']


    index += 1

    if index == 11:
        break

    print(int(index), launch_name)
print()
select = input("Enter Launch Number (1-10): ")

index = select

launch_name = json_data['launches'][index]['name']
launch_date = json_data['launches'][index]['net']
launch_from = json_data['launches'][index]['location']['pads']