import http.client

conn = http.client.HTTPSConnection("sportspage-feeds.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "sportspage-feeds.p.rapidapi.com"
    }

conn.request("GET", "/teams?league=%3CREQUIRED%3E", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))