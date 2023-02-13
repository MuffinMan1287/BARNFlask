import requests

url = "https://nba-player-props-odds.p.rapidapi.com/get-player-odds-for-event"

querystring = {"eventId":"22200","bookieId":"1:4:5:6:7:8:9:10","marketId":"1:2:3:4:5:6","decimal":"true","best":"true"}

headers = {
	"X-RapidAPI-Key": "0608f45064msh40e1e6383c4be53p176cf6jsn49eacc437480",
	"X-RapidAPI-Host": "nba-player-props-odds.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)