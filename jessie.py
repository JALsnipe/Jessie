import sys
import pyimgur
import string
import random
import json

from urllib2 import Request, urlopen

# http://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if len(sys.argv) != 2:
	print "Usage: python jesse.py [image to upload]"
	sys.exit()

# TODO: check if this is a valid image
# print sys.argv[1]

CLIENT_ID = "Your_applications_client_id"
PATH = sys.argv[1]

# TODO: error checking here
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title=PATH)
# print(uploaded_image.title)
# print(uploaded_image.link)
# print(uploaded_image.size)
# print(uploaded_image.type)

headers = {"Content-Type": "application/json"}
request = Request("http://upload.gfycat.com/transcode/" + id_generator() + "?fetchUrl=" + uploaded_image.link, headers=headers)
response_body = urlopen(request).read()
# print response_body
# print type(response_body)

json_req = json.loads(response_body)
# TODO: Need error checking here

print "http://gfycat.com/" + json_req['gfyname']