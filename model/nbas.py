import requests

url = "https://nba-player-props-odds.p.rapidapi.com/api/v1/odds"

headers = {
    "X-RapidAPI-Host": "nba-player-props-odds.p.rapidapi.com",
    "X-RapidAPI-Key": "0608f45064msh40e1e6383c4be53p176cf6jsn49eacc437480",
    "Content-Type": "application/json"
}

data = {
    "player": "Marcus Smart"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    data = response.json()
    print("Prop odds for player:", data["player"])
    print("Points scored:", data["points"])
    print("Rebounds:", data["rebounds"])
    print("Assists:", data["assists"])
else:
    print("Failed to retrieve prop odds for player.")