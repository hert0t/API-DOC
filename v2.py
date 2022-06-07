import requests

class BEAPI():
    def __init__(self, apikey):
        self.host = "https://api.chstore.me/v2"
        self.http = requests.session()
        self.apikey = apikey

    def lineRegister(self, phone, country="ID"):
        #['HK', 'IN', 'ID', 'JP', 'KR', 'SA', 'SG', 'TH', 'US', 'MY']
        params = {"phone": phone, "country": country, "apikey": self.apikey}
        resp = self.http.get(self.host+"/lineregist",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def lineRegisterPincode(self, session, pinCode):
        params = {"pincode": pinCode, "apikey": self.apikey}
        resp = self.http.get(self.host+"/lineregist/pincode/"+session,params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp
