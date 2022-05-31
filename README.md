## REQUIREMENT ##
Apikey: https://api.chstore.me

## EXAMPLE ##
- ALPHACODERS
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.alphaCodersSearch("naruto", 1)
print(res) #for prety print result
```

- AUTHKEY2PRIMARY
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.authKey2Primary('your line authkey')
print(res) #for prety print result
```

- ALPHACODERS
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.alphaCodersSearch("naruto", 1)
print(res) #for prety print result
```

- BRAINLY
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.brainlySearch('kenapa bumi bulat')
print(res) #for prety print result
```

- GIFSEARCH
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.gifSearch("naruto")
print(res) #for prety print result
```

- GOOGLESEARCH
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.googleSearch("naruto")
print(res) #for prety print result
```

- GOOGLEIMG
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.googleImg("naruto")
print(res) #for prety print result
```

- GOOGLE TRANSLATE
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.googleTranslate('anjing', 'en')
print(res) #for prety print result
```

- IMGREVERSE
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.googleImgReverse("url_img")
print(res) #for prety print result
```

- JOOXSEARCH
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
#WITH SEARCH QUERY
res = api.jooxSearch("bring me the horizon")
#WITH SONG ID
res = api.jooxId("1W09eg2vDIJLQgrWOj_4FQ==")
print(res) #for prety print result
```

- KAMUS INDONESIA
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.kamusIndonesia("makan")
print(res) #for prety print result
```

- LINEAPPVER LAST
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.lineAppver()
print(res) #for prety print result
```

- LINEAPPNAME RANDOM
```PY
from v1 import BEAPI
api = BEAPI()
#["android","ios","chromeos","desktopmac","desktopwin","iosipad"]
res = api.lineAppNameRandom("chromeos")
print(res) #for prety print result
```

- LINE QR ROTATE
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
qr = api.lineGetQr("IOSIPAD\t10.5.2\tiPhone 8\t11.2.5")
print("Link QR: "+qr["result"]["qrlink"])
print("QR Image: "+qr["result"]["qrcode"])
print("IP: "+qr["result"]["ip"])
pincode = api.lineGetQrPincode(qr["result"]["session"])
print("Pincode: "+pincode["result"]["pincode"])
auth = api.lineGetQrAuth(qr["result"]["session"])
print("AccessToken: "+auth["result"]["accessToken"])
print("Cert: "+auth["result"]["certificate"])

## LOGIN WITH CERT ##

api = BEAPI("apikey_here")
qr = api.lineGetQr("IOSIPAD\t10.5.2\tiPhone 8\t11.2.5","your_cert")
print("Link QR: "+qr["result"]["qrlink"])
print("QR Image: "+qr["result"]["qrcode"])
print("IP: "+qr["result"]["ip"])
auth = api.lineGetQrAuth(qr["result"]["session"])
print("AccessToken: "+auth["result"]["accessToken"])
print("Cert: "+auth["result"]["certificate"])
```

- LINEPRIMARYCONVERT
```PY
from v1 import BEAPI
api = BEAPI()
res = api.linePrimary2Secondary("IOSIPAD\t10.5.2\tiPhone 8\t11.2.5","your_authtoken")
print(res) #for prety print result
```

- 9GAG
```PY
from v1 import BEAPI
api = BEAPI()
##['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe']
res = api.nineGagFresh('funny')
print(res) #for prety print result
#OR
res = api.nineGagHot('funny')
print(res) #for prety print result
```

- 1CAKRANDOM
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
res = api.oneCakRandom()
print(res) #for prety print result
```

- SIMISIMI
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
#['af', 'al*', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'cx*', 'ch*', 'hr', 'cs', 'da', 'nl', 'en', 'et', 'ph*', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'he', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'kn', 'kk', 'kh*', 'ko', 'ku', 'lv', 'lt', 'mk', 'ms', 'ml', 'mr', 'mn', 'my', 'ne', 'nb', 'as', 'br', 'gn', 'jv', 'or', 'rw', 'zh*', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'rs*', 'si', 'sk', 'sl', 'es', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vn*', 'cy']
res = api.simiSimi('anjing', 'id')
print(res) #for prety print result
```

- SMULE
```PY
from v1 import BEAPI
api = BEAPI("apikey_here")
#res = api.smulePerformance("JoseffMcKenneth")
#res = api.smuleUser("JoseffMcKenneth")
res = api.smulePost("https://www.smule.com/p/2352981025_3553994501")
print(res) #for prety print result
```

- TRACKRESI
```PY
from v1 import BEAPI
api = BEAPI()
#['pos', 'wahana', 'jnt', 'sap', 'sicepat', 'jet', 'dse', 'first', 'ninja', 'lion', 'idl', 'rex', 'ide', 'sentral']
res = api.trackingResi('your_resi', 'your_courier')
print(res) #for prety print result
```

- TIKTOK
```PY
from v1 import BEAPI
api = BEAPI()
res = api.tiktokPost("https://www.tiktok.com/@msglowbdl/video/6933152608211307778")
print(res) #for prety print result
res = api.tiktokPostV2("https://www.tiktok.com/@msglowbdl/video/6933152608211307778")
print(res) #for prety print result
```

