import requests
import json
import base64

url = 'https://rj5pfi3lci.execute-api.eu-west-1.amazonaws.com/prod/'

with open("image.png", "rb") as files:
    encoded_string = base64.b64encode(files.read())

def send_data():
    res = requests.post(
            url, 
            data=encoded_string,
            headers={
                'Content-Type': 'text/plain;charset=UTF-8',
                'Content-Encoding': 'identity'}
            )

    if res.status_code == 200:
        get_http_header = res.json()
        get_body = get_http_header['body']
        return get_body
    else:
        print(res.status_code)

def decode_data():
    img_decode = base64.b64decode(decode_body)
    filename = 'some_image.png'
    with open(filename, 'wb') as f:
        f.write(img_decode)

decode_body = send_data()

#
##
### main function
##
#
decode_data()
