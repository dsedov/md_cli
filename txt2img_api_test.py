from md_api import MDApi, MDPromptConfig
api = MDApi("config.yaml")
prompt = MDPromptConfig()
prompt.seed = 2184854795
prompt.safety = False
prompt.scale = 8.0
prompt.prompt = [
    { "text" : "portrait of Morgan Freeman, painting by Jeremy Mann", "weight" : 0.5 },
    { "text" : "portrait of Elon Musk, painting by Valentin Serov", "weight" : 0.5 }]
img = api.txt2img(prompt)

img[1].show()