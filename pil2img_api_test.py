from PIL import Image
from md_api import MDApi, MDPromptConfig


api = MDApi("config.yaml")
prompt = MDPromptConfig()
prompt.strength = 0.5
pilImage = Image.open('test_image.png')
img = api.pil2img(prompt,pilImage)

img[1].show()