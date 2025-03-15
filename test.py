import google.generativeai as genai

genai.configure(api_key="AIzaSyCOQ7lBaZb5iV_Ycvil9xqQC26-Vb_KHmg")
models = genai.list_models()

for model in models:
    print(model.name)
