import requests

## INFORMATION ##
# VERY FAST GET, UNIQUE IP, FILTER IP BY REGION, BUT FAST TIMEOUT (30SEC) #

apiKey = "apikey_here"
appName = "IOSIPAD\t10.5.2\tiPhone 8\t11.2.5"
country = "JP"
#['HK', 'IN', 'ID', 'JP', 'KR', 'SA', 'SG', 'TH', 'US', 'MY']


## LOGIN WITHOUT CERT ##
params = {"apikey": apiKey, "appname": appName, "country": country}
login = requests.get("https://api.chstore.me/v1/lineqr1",params=params).json()["result"]
print("Login ip: "+login["ip"])
print("Qrcode: "+login["qrcode"])
print("Qrlink: "+login["qrlink"])
pincode = requests.get("https://api.chstore.me/v1/lineqr1/pincode/"+login["session"],params=params).json()["result"]
print("Pincode: "+pincode["pincode"])
auth = requests.get("https://api.chstore.me/v1/lineqr1/auth/"+login["session"],params=params).json()["result"]
print("AccessToken: "+auth["accessToken"])
print("Cert: "+auth["certificate"])



## LOGIN WITH CERT ##
cert = "cert_here"
params = {"apikey": apiKey, "appname": appName, "country": country, "cert": cert}
login = requests.get("https://api.chstore.me/v1/lineqr1",params=params).json()["result"]
print("Login ip: "+login["ip"])
print("Qrcode: "+login["qrcode"])
print("Qrlink: "+login["qrlink"])
auth = requests.get("https://api.chstore.me/v1/lineqr1/auth/"+login["session"],params=params).json()["result"]
print("AccessToken: "+auth["accessToken"])
print("Cert: "+auth["certificate"])

