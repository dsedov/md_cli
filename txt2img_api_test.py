import yaml,requests
from PIL import Image

config = yaml.safe_load(open("config.yaml"))
values = {
    'q' : 'Magnificent castle by Mark Rothko',
    'steps' : 70,
    'w' : 512,
    'h' : 512,
    'strength' : 0.8
}

r = requests.post(config["md"]["server_address"] + "/txt2img/", data=values)
filename = r.headers["filename"]
print(r.headers)
f = open(filename, "wb")
f.write(r.content)
f.close()