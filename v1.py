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

    def lineAppnameRandom(self, osname):
        #["android","ios","chromeos","desktopmac","desktopwin","iosipad"]
        params = {"osname": osname, "apikey": self.apikey}
        resp = self.http.get(self.host+"/lineappname_random",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def linePrimary2Secondary(self, appName, authToken):
        params = {"appname": appName, "authtoken": authToken, "apikey": self.apikey}
        resp = self.http.get(self.host+"/lineprimary2secondary",params=params).json()
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

    def nineGagFresh(self, category):
        #['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe']
        params = {"apikey": self.apikey, "category": category}
        resp = self.http.get(self.host+"/9gag-fresh",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def nineGagHot(self, category):
        #['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe']
        params = {"apikey": self.apikey, "category": category}
        resp = self.http.get(self.host+"/9gag-hot",params=params).json()
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

    def tiktokPost(self, url):
        params = {"url": url, "apikey": self.apikey}
        resp = self.http.get(self.host+"/tiktok",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp
    
    def tiktokPostV2(self, url):
        params = {"url": url, "apikey": self.apikey}
        resp = self.http.get(self.host+"/musicallydown",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp

    def trackingResi(self, resi, courier):
        #['pos', 'wahana', 'jnt', 'sap', 'sicepat', 'jet', 'dse', 'first', 'ninja', 'lion', 'idl', 'rex', 'ide', 'sentral']
        params = {"resi": resi, "courier": courier, "apikey": self.apikey}
        resp = self.http.get(self.host+"/track-resi",params=params).json()
        if resp["status"] != 200: raise Exception (resp["reason"])
        return resp
