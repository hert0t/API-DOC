## REQUIREDMENT ##
Apikey: https://api.chstore.me

## EXAMPLE ##
- ALPHACODERS
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.alphaCodersSearch("naruto", 1)
api.pretyPrint(res) #for prety print result
```

- AUTHKEY2PRIMARY
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.authKey2Primary('your line authkey')
api.pretyPrint(res) #for prety print result
```

- ALPHACODERS
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.alphaCodersSearch("naruto", 1)
api.pretyPrint(res) #for prety print result
```

- BRAINLY
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.brainlySearch('kenapa bumi bulat')
api.pretyPrint(res) #for prety print result
```

- GIFSEARCH
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.gifSearch("naruto")
api.pretyPrint(res) #for prety print result
```

- GOOGLESEARCH
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.googleSearch("naruto")
api.pretyPrint(res) #for prety print result
```

- GOOGLEIMG
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.googleImg("naruto")
api.pretyPrint(res) #for prety print result
```

- GOOGLE TRANSLATE
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.googleTranslate('anjing', 'en')
api.pretyPrint(res) #for prety print result
```

- IMGREVERSE
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.googleImgReverse("url_img")
api.pretyPrint(res) #for prety print result
```

- JOOXSEARCH
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
#WITH SEARCH QUERY
res = api.jooxSearch("bring me the horizon")
#WITH SONG ID
res = api.jooxId("1W09eg2vDIJLQgrWOj_4FQ==")
api.pretyPrint(res) #for prety print result
```

- KAMUS INDONESIA
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.kamusIndonesia("makan")
api.pretyPrint(res) #for prety print result
```

- LINEAPPVER LAST
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.lineAppver()
api.pretyPrint(res) #for prety print result
```

- LINE QR ROTATE
```PY
from BEAPI import BEAPI
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

- 1CAKRANDOM
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.oneCakRandom()
api.pretyPrint(res) #for prety print result
```

- SIMISIMI
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
#['af', 'al*', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'cx*', 'ch*', 'hr', 'cs', 'da', 'nl', 'en', 'et', 'ph*', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'he', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'kn', 'kk', 'kh*', 'ko', 'ku', 'lv', 'lt', 'mk', 'ms', 'ml', 'mr', 'mn', 'my', 'ne', 'nb', 'as', 'br', 'gn', 'jv', 'or', 'rw', 'zh*', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'rs*', 'si', 'sk', 'sl', 'es', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vn*', 'cy']
res = api.simiSimi('anjing', 'id')
api.pretyPrint(res) #for prety print result
```

- SMULE
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
#res = api.smulePerformance("JoseffMcKenneth")
#res = api.smuleUser("JoseffMcKenneth")
res = api.smulePost("https://www.smule.com/p/2352981025_3553994501")
api.pretyPrint(res) #for prety print result
```

- TIKTOK
```PY
from BEAPI import BEAPI
api = BEAPI("apikey_here")
res = api.tiktokPostV2("https://www.tiktok.com/@msglowbdl/video/6933152608211307778")
api.pretyPrint(res) #for prety print result
```

