import requests

## INFORMATION ##
# PRIVATE PROXY, ROTATE EVERY 1 MINUTE, JAPAN SERVER, FULL SPEED #

apiKey = "apikey_here"

params = {"apikey": apiKey}
proxies = requests.get("https://api.chstore.me/v1/rotateproxy",params=params).json()["result"]
print("Your proxies: "+str(proxies))
myIP = requests.get("https://api.ipify.org",proxies=proxies).text
print("Your ip: "+myIP)
