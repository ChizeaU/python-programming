import requests
import json

url = "https://free-nba.p.rapidapi.com/stats"

querystring = {"page":"0","per_page":"25"}

headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "e25fd7c49cmsh006d58ed34a264ep111c9djsn3df28e302cea"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

#Saves the data set to a file
with open("nbaStats.json", "w") as nba_file:
    nba_file.write(json.dumps(response.text))




