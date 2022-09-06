from PIL import Image, ImageDraw, ImageFilter
from md_api import MDApi, MDPromptConfig
api = MDApi("config.yaml")
prompt = MDPromptConfig()
prompt.steps = 60
prompt.strength = 0.9
prompt.seed = 112
prompt.w = 706
prompt.h = 768
pilImage = Image.open('test_image.png')
pilImage = pilImage.resize((706,768), resample=Image.Resampling.LANCZOS)

pilMask = Image.new(mode='RGB', size= (706,768), color=(255,255,255))
draw_handle = ImageDraw.Draw(pilMask)
draw_handle.rectangle([(0,0),(706,768-500)], fill = (0,0,0))
pilMask = pilMask.filter(ImageFilter.GaussianBlur(32))

img = api.pil2img(prompt,pilImage, pilMask)
img[1].show()