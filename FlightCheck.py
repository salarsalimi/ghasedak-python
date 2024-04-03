#### This is a simple script to check new flights and Send SMS with Ghasedak Web API to notify User

import requests
import json

url = "https://flight.atighgasht.com/api/Flights"
headers = {
    "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"24\", \"Chromium\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJidXMiOiI0ZiIsInRybiI6IjE3Iiwic3JjIjoiMiJ9.vvpr9fgASvk7B7I4KQKCz-SaCmoErab_p3csIvULG1w",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36",
    "Content-Type": "application/json-patch+json",
    "Accept": "application/json, text/plain, */*",
    "X-Playerid": "5c755ab9-16f3-4d80-a5b4-abbc4c213009",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Origin": "https://mrbilit.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://mrbilit.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}

data = {
    "AdultCount": 1,
    "ChildCount": 0,
    "InfantCount": 0,
    "CabinClass": "All",
    "Routes": [{"OriginCode": "MHD", "DestinationCode": "THR", "DepartureDate": "2024-01-01"}],
    "Baggage": True
}

response = requests.post(url, headers=headers, json=data)

count = 0
prices_val = []
id_old = []
id_new = []
if response.status_code == 200:
    json_response = response.json()
    for items in json_response['Flights']:
        if items['Prices']:
            id_new.append(items['Id'])
            count = count + 1
            print(items['Prices'][0]['PassengerFares'][0]['TotalFare'])
            prices_val.append(items['Prices'][0]['PassengerFares'][0]['TotalFare'])

else:
    print("Request failed with status code:", response.status_code)

print(prices_val)

# Open the file in read mode
with open('flights.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        id_old.append(line.strip())  # Strip removes the newline character from the end of each line



# Open the file in write mode
with open('flights.txt', 'w') as file:
    # Write content to the file
    for i in id_new:
        file.write(i)
        file.write("\n")

# Notify the user that writing is completed
print("Content has been written to the file.")


ff = 0
for ids in id_new:
    for oids in id_old:
        if ( oids == ids ):
            ff = 1
    if ( ff == 0 ):
        url = "https://api.ghasedak.me/v2/sms/send/simple"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36",
            "apikey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "message": "بلیط هواپیما",
            "receptor": "09121111111",
            "linenumber": "300002525"
        }

        response = requests.post(url, headers=headers, data=payload)
        print(response.text)
        break
