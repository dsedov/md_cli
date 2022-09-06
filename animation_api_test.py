from PIL import Image, ImageDraw, ImageFilter
from md_api import MDApi, MDPromptConfig
import cv2
import numpy as np
api = MDApi("config.yaml")
prompt = MDPromptConfig()
prompt.steps = 50
prompt.safety = False
prompt.strength = 0.5
prompt.seed = 112
prompt.w = 512
prompt.h = 512
pilImage = Image.open('test_image.png')
pilImage = pilImage.resize((prompt.w,prompt.h), resample=Image.Resampling.LANCZOS)


videodims = (prompt.w, prompt.h)
fourcc = cv2.VideoWriter_fourcc(*'avc1')    
video = cv2.VideoWriter("flowing_24fps_1.mp4",fourcc, 24,videodims)

i = 0 
for a in np.arange(0, 200, 1):
    print(f"Frame: {a}")
    pilMask = Image.new(mode='RGB', size= (prompt.w,prompt.h), color=(255,255,255))
    draw_handle = ImageDraw.Draw(pilMask)
    draw_handle.rectangle([(0,0),(prompt.w,prompt.h-(prompt.h-a))], fill = (0,0,0))
    pilMask = pilMask.filter(ImageFilter.GaussianBlur(32))
    img = api.pil2img(prompt,pilImage, pilMask)
    img[1].save(f"temp/{i}.png")
    imtemp = img[1].copy()
    video.write(cv2.cvtColor(np.array(imtemp), cv2.COLOR_RGB2BGR))
    i += 1
video.release()
