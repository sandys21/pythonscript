import http.client

conn = http.client.HTTPSConnection("datausa.io")


conn.request("GET", "/api/data?drilldowns=Nation&measures=Population")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))