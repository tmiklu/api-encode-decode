import requests
import json
import base64

url = 'https://rj5pfi3lci.execute-api.eu-west-1.amazonaws.com/prod/'

with open("image.png", "rb") as files:
    encoded_string = base64.b64encode(files.read())

def decode():
    res = requests.post(
            url, 
            data=encoded_string,
            headers={
                'Content-Type': 'application/octet-stream',
                'Content-Encoding': 'identity'}
            )

    if res.status_code == 200:
        get_http_header = res.json()
        get_body = get_http_header['body']
        return get_body
    else:
        print(res.status_code)

print(decode())
