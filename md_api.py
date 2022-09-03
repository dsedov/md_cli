
import yaml,requests, json, io
from PIL import Image

class MDPromptConfig:
    def __init__(self):
        self.prompt = "magestic castle painting by mark rothko"
        self.w = 512
        self.h = 512
        self.steps = 50
        self.scale = 8
        self.strength = 0
    
    def json(self):
        return self.__dict__

class MDApi:
    def __init__(self, settingsFile):
        self.config = yaml.safe_load(open("config.yaml"))

    def txt2img(self, promptConfig):
        r = requests.post(self.config["md"]["server_address"] + "/txt2img/", data=promptConfig.json())
       
        filename = r.headers["filename"]
        image_bytes = io.BytesIO(r.content)
        img = Image.open(image_bytes)
        return (filename, img)
    
    def img2img(self, promptConfig, imagePath):
        files = {'image': open(imagePath,'rb')}
        
        r = requests.post(self.config["md"]["server_address"] + "/img2img/", files=files, data=promptConfig.json())
        
        filename = r.headers["filename"]
        image_bytes = io.BytesIO(r.content)
        img = Image.open(image_bytes)
        return (filename, img)

    def pil2img(self, promptConfig, pilImage):
        byte_io = io.BytesIO()
        pilImage.save(byte_io, 'png')
        byte_io.seek(0)
        files = {'image': ('pil_image.png', byte_io, 'image/png')}
        r = requests.post(self.config["md"]["server_address"] + "/img2img/", files=files, data=promptConfig.json())
        
        filename = r.headers["filename"]
        image_bytes = io.BytesIO(r.content)
        img = Image.open(image_bytes)
        return (filename, img)

