from PIL import Image
from md_api import MDApi, MDPromptConfig


api = MDApi("config.yaml")
prompt = MDPromptConfig()
prompt.strength = 0.5
img = api.img2img(prompt,'test_image.png')

img[1].show()