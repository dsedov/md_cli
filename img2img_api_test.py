import yaml, os, requests, json
from PIL import Image

config = yaml.safe_load(open("config.yaml"))
files = {'image': open('test_image.png','rb')}

values = {
    'q' : 'Magnificent castle by Mark Rothko',
    'steps' : 70,
    'w' : 512,
    'h' : 512,
    'strength' : 0.8
}

r = requests.post(config["md"]["server_address"] + "/img2img/", files=files, data=values)
filename = r.headers["filename"]
print(r.headers)
f = open(filename, "wb")
f.write(r.content)
f.close()