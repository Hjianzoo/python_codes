import requests
url = 'http://smartdevice.ai.tuling123.com/speech/chat'
headers = {'Host':"smartdevice.ai.tuling123.com",\
'Connection':'keep-alive',\
'Content-Length':'26899',\
'Cache-Control':'no-cache',\
'Content-Type':'multipart/form-data; boundary',\
'Accepy':'*/*',\
'Accept-Encoding':'gzip,deflate',\
'Accept-Language':'zh-CN',\
'Content-Disposition':'form-data; name="parameters"'\
}
d = {"ak": "8268ff3bce3e45c7b10a6d49a0fddcd5","uid": "9C5DE14C6503BCF56821D7A41DA23B4D",\
'asr':1,'tts':1,'token':"2af62825b9cd49568cc55a6256a86239","flag": 3}
r = requests.post(url, headers = headers,data=d)
print r.text