import requests

## INFORMATION ##
# EMULATOR ACTIVE FOR 1HOURS, YOU NEED SOCKS PROXIES,  CUSTOMIZE(IMEI, ANDROIDID, ETC) #
# TOPOLOGY: SET PROXY > SIGNUP LINE > FETCH TOKEN > CLEAR DATA LINE > CHANGE PROXY > CHANGE INFO (IMEI, ANDROIDID, ETC) > RESIGNUP AGAIN

apiKey = "apikey_here"
params = {"apikey": apiKey}
data = requests.get("https://api.chstore.me/v1/getemu",params=params).json()["result"]
print("Remote URL: "+data["remoteUrl"])
print("FetchToken URL: "+data["fetchtoken"])
