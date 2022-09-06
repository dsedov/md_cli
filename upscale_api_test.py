from PIL import Image, ImageDraw, ImageFilter
from md_api import MDApi, MDPromptConfig
import uuid
api = MDApi("config.yaml")

source_image = 'test_image.png'
upscale_prompt = 'serene landscape, painting by Albert Marquet, trending on artstation'
upscale_prompt = 'dark abandoned streets of night los angeles , painting by Jean_Delville, trending on artstation'
upscale_prompt = 'dark abandoned streets of night los angeles, painting by Joe Fenton, trending on artstation'
upscale_prompt = 'dark abandoned streets of night los angeles, painting by Juan Gris, trending on artstation'
upscale_prompt = 'dark abandoned geometric, isometric echo, from drone, painting by Marianne von Werefkin, trending on artstation, science fiction'
upscale_prompt = 'dark abandoned streets of night los angeles, painting by Margaret Macdonald Mackintosh, trending on artstation, science fiction'
upscale_prompt = 'destroyed brick wall, painting by Margaret Maximilien Luce, trending on artstation, science fiction'
upscale_prompt = 'castle ruins with overgrown vines, painting by Odilon Redon, trending on artstation, science fiction'

# Kate_Greenaway
# Katsuhiro_Otomo
# Kay_Nielsen
# Kim_Jung_Gi
# Margaret_Macdonald_Mackintosh
# Marianne_von_Werefkin
# Maximilien_Luce
scale_factor = 2 
tile_size_w = 512
tile_size_h = 512
tile_mask_errode = 64
tile_mask_blur = 16
tile_step = 512-128-32

prompt = MDPromptConfig()
prompt.steps = 40
prompt.safety = False
prompt.prompt = upscale_prompt
prompt.strength = 0.8
#prompt.seed = 112
prompt.w = tile_size_w
prompt.h = tile_size_h

pilImage = Image.open('00004_S1305043296.png')

pilMask = Image.new(mode='RGB', size= (tile_size_w,tile_size_h), color=(255,255,255))
draw_handle = ImageDraw.Draw(pilMask)
draw_handle.rectangle([(tile_mask_errode,tile_mask_errode),(tile_size_w - tile_mask_errode,tile_size_h - tile_mask_errode)], fill = (0,0,0))
pilMask = pilMask.filter(ImageFilter.GaussianBlur(tile_mask_blur))


def upscale(image, mask, settings, scale_factor, tile_size_w, tile_size_h, tile_step ):
    image = image.resize(( int(image.size[0] * scale_factor),int(image.size[1] * scale_factor)), resample=Image.Resampling.LANCZOS)
    maskL = mask.convert('L')
    for y in range(0, image.size[1] // tile_step + 2):
        for x in range(0, image.size[0] // tile_step + 2):
            print(f"tile {x}:{y}")
            sendImage = image.crop((x * tile_step - tile_size_w//2, y * tile_step - tile_size_h//2, x * tile_step + tile_size_w//2, y * tile_step + tile_size_h//2))
            img = api.pil2img(settings,sendImage, mask)
            img_comp = Image.composite(sendImage, img[1], maskL)
            Image.Image.paste(image, img_comp, (x * tile_step - tile_size_w//2, y * tile_step - tile_size_h//2))
            
    return image

for i in range(3):
    print(f"stage {i}")
    pilImage = upscale(pilImage, pilMask, prompt, scale_factor, tile_size_w, tile_size_h, tile_step) 
    pilImage.save(f"temp/{str(uuid.uuid4())}.png")    
    pilImage.show()
    prompt.strength -= 0.05