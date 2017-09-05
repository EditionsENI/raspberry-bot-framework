########### Python 2.7 #############
import httplib, urllib, base64
import json
import operator
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '8b30f0bb8182478891fe95fc2d01dbd6',
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = open('s.jpg','rb').read()

conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)

response = conn.getresponse()
data = response.read()
result = json.loads(data)
scores = result[0]["scores"]

sorted_x = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)

if(sorted_x[0][0] == 'happiness'):
    print ('happy!')
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, 0, 255, 0)
    uh.show()

if(sorted_x[0][0] == 'neutral'):
    print ('neutral!')
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, 255, 255, 255)
    uh.show()

if(sorted_x[0][0] == 'sadness'):
    print ('sad!')
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, 0, 0, 255)
    uh.show()

print (sorted_x)
conn.close()
input()