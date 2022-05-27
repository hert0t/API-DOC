import requests

class BEAPI():
    def __init__(self, apikey):
        self.host = "https://api.chstore.me/v1"
        self.http = requests.session()
        self.apikey = apikey

    def alphaCoders(self, search, page=1):
        params = {"search": search, "page": page, "apikey": self.apikey}
        resp = self.http.get(self.host+"/alphacoders",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def authKey2Primary(self, authKey):
        params = {"authkey": authKey, "apikey": self.apikey}
        resp = self.http.get(self.host+"/authkey2primary",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def brainlySearch(self, search):
        params = {"search": search, "apikey": self.apikey}
        resp = self.http.get(self.host+"/brainly",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def gifSearch(self, search):
        params = {"search": search, "apikey": self.apikey}
        resp = self.http.get(self.host+"/gifsearch",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def googleImg(self, search):
        params = {"search": search, "apikey": self.apikey}
        resp = self.http.get(self.host+"/googleimg",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def googleSearch(self, search, page=1):
        params = {"search": search, "page": page, "apikey": self.apikey}
        resp = self.http.get(self.host+"/googlesearch",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def googleTranslate(self, lang, text):
        params = {"lang": lang, "text": text, "apikey": self.apikey}
        resp = self.http.get(self.host+"/googletrans",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def gogoleImgReverse(self, url):
        params = {"url": url, "apikey": self.apikey}
        resp = self.http.get(self.host+"/imgreverse",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def jooxSearch(self, search):
        params = {"search": search, "apikey": self.apikey}
        resp = self.http.get(self.host+"/joox",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def jooxId(self, idx):
        params = {"id": idx, "apikey": self.apikey}
        resp = self.http.get(self.host+"/joox",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def kamusIndonesia(self, search):
        params = {"search": search, "apikey": self.apikey}
        resp = self.http.get(self.host+"/kbbi",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def lineAppver(self):
        params = {"apikey": self.apikey}
        resp = self.http.get(self.host+"/lineappver",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def lineGetQr(self, appName, cert=None, country="JP"):
        #['HK', 'IN', 'ID', 'JP', 'KR', 'SA', 'SG', 'TH', 'US', 'MY']
        params = {"appname": appName, "country": country, "apikey": self.apikey}
        if cert: params["cert"] = cert
        resp = self.http.get(self.host+"/lineqr",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def lineGetQrPincode(self, session):
        params = {"apikey": self.apikey}
        resp = self.http.get(self.host+"/lineqr/pincode/"+session,params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def lineGetQrAuth(self, session):
        params = {"apikey": self.apikey}
        resp = self.http.get(self.host+"/lineqr/auth/"+session,params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def oneCakRandom(self):
        params = {"apikey": self.apikey}
        resp = self.http.get(self.host+"/onecak",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def simiSimi(self, lang, text):
        #['af', 'al*', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'cx*', 'ch*', 'hr', 'cs', 'da', 'nl', 'en', 'et', 'ph*', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'he', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'kn', 'kk', 'kh*', 'ko', 'ku', 'lv', 'lt', 'mk', 'ms', 'ml', 'mr', 'mn', 'my', 'ne', 'nb', 'as', 'br', 'gn', 'jv', 'or', 'rw', 'zh*', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'rs*', 'si', 'sk', 'sl', 'es', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vn*', 'cy']
        params = {"lang": lang, "text": text, "apikey": self.apikey}
        resp = self.http.get(self.host+"/simisimi",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def smulePost(self, url):
        params = {"url": url, "apikey": self.apikey}
        resp = self.http.get(self.host+"/smule/post",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def smuleUser(self, user):
        params = {"user": user, "apikey": self.apikey}
        resp = self.http.get(self.host+"/smule/user",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp
    
    def smulePerformance(self, user):
        params = {"user": user, "apikey": self.apikey}
        resp = self.http.get(self.host+"/smule/performance",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def tiktokPostV2(self, url):
        params = {"url": url, "apikey": self.apikey}
        resp = self.http.get(self.host+"/musicallydown",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

