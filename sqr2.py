import requests

## INFORMATION ##
# FAST GET, UNIQUE IP CHANGED EVERY MINUTE, LONG TIMEOUT (60-120S) #

apiKey = "apikey_here"
appName = "IOSIPAD\t10.5.2\tiPhone 8\t11.2.5"

## LOGIN WITHOUT CERT ##
params = {"apikey": apiKey, "appname": appName}
login = requests.get("https://api.chstore.me/v1/lineqr2",params=params).json()["result"]
print("Login ip: "+login["ip"])
print("Qrcode: "+login["qrcode"])
print("Qrlink: "+login["qrlink"])
pincode = requests.get("https://api.chstore.me/v1/lineqr2/pincode/"+login["session"],params=params).json()["result"]
print("Pincode: "+pincode["pincode"])
auth = requests.get("https://api.chstore.me/v1/lineqr2/auth/"+login["session"],params=params).json()["result"]
print("AccessToken: "+auth["accessToken"])
print("Cert: "+auth["certificate"])



## LOGIN WITH CERT ##
cert = "your_cert"
params = {"apikey": apiKey, "appname": appName, "cert": cert}
login = requests.get("https://api.chstore.me/v1/lineqr2",params=params).json()["result"]
print("Login ip: "+login["ip"])
print("Qrcode: "+login["qrcode"])
print("Qrlink: "+login["qrlink"])
auth = requests.get("https://api.chstore.me/v1/lineqr2/auth/"+login["session"],params=params).json()["result"]
print("AccessToken: "+auth["accessToken"])
print("Cert: "+auth["certificate"])

