from PIL import Image
from md_api import MDApi, MDPromptConfig


api = MDApi("config.yaml")
prompt = MDPromptConfig()

img = api.txt2img(prompt)

img[1].show()