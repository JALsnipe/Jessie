import sys
import pyimgur
import string
import random
import json
import urllib2
import requests

# http://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if len(sys.argv) != 2:
	print "Usage: python jesse.py [.gif to upload]"
	sys.exit()

# Check if this is a valid gif image
if(not sys.argv[1].endswith('.gif')):
	print "Please use a valid .gif image."
	sys.exit()


# TODO: handle errors from Imgur API
# print sys.argv[1]

CLIENT_ID = "Your_applications_client_id"
PATH = sys.argv[1]

im = pyimgur.Imgur(CLIENT_ID)

try:
	uploaded_image = im.upload_image(PATH, title=PATH)
except ValueError, e:
	print e
	sys.exit()
except requests.exceptions.HTTPError:
	# print "Error: check your CLIENT_ID"
	sys.exit()
except IOError:
	print "No such file: " + sys.argv[1]
	sys.exit()
# print(uploaded_image.title)
# print(uploaded_image.link)
# print(uploaded_image.size)
# print(uploaded_image.type)

headers = {"Content-Type": "application/json"}

try:
	request = urllib2.Request("http://upload.gfycat.com/transcode/" + id_generator() + "?fetchUrl=" + uploaded_image.link, headers=headers)
	response_body = urllib2.urlopen(request).read()
	json_req = json.loads(response_body)

	# print response_body
	print "http://gfycat.com/" + json_req['gfyname']

except NameError:
	print "Error: no response"
	sys.exit()

except KeyError:
	# Hit the API too many times.  Only one upload every 30 seconds is allowed.
	print "Error: " + json_req['error']
	sys.exit()