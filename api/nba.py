import http.client

conn = http.client.HTTPSConnection("nba-player-props-odds.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "0608f45064msh40e1e6383c4be53p176cf6jsn49eacc437480",
    'X-RapidAPI-Host': "nba-player-props-odds.p.rapidapi.com"
    }

conn.request("GET", "/get-player-odds-for-event?eventId=22200&bookieId=1%3A4%3A5%3A6%3A7%3A8%3A9%3A10&marketId=1%3A2%3A3%3A4%3A5%3A6&decimal=true&best=true", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))