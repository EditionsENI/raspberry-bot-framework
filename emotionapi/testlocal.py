########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '8b30f0bb8182478891fe95fc2d01dbd6',
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = open('02.jpg','rb').read()

conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)

response = conn.getresponse()
data = response.read()
print(data)

conn.close()