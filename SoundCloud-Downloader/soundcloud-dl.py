import json, requests

url = 'https://api.soundcloud.com/resolve.json'

your_client_id = '[PUT YOUR client_id HERE]'

params = dict(
    url='https://soundcloud.com/msmrsounds/ms-mr-hurricane-chvrches-remix',
    client_id=your_client_id,
)

# resolve
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

# get api url
track_url = data.get('location')

track_resp = requests.get(url=url, params=params)
track_data = json.loads(resp.text)

# get stream_url

track_title = track_data.get('title')

stream_url = track_data.get('stream_url')

print track_title
print stream_url

stream_params = dict(
    client_id=your_client_id,
)

stream_resp = requests.get(url=url, params=params)

# pass in title + '.mp3' for filename
with open(track_title + '.mp3', 'wb') as handle:
    response = requests.get(url=stream_url, params=stream_params, stream=True)

    if not response.ok:
        # Something went wrong
        print 'Error downloading mp3'

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)