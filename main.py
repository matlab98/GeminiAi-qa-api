import textwrap
import os
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace("•", "  *")
    
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

load_dotenv()  # Carga las variables del archivo .env
gemini_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_key)

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
        
model = genai.GenerativeModel("gemini-1.5-flash")

# %%time
response = model.generate_content("me puedes ayudar generando flashcard acerca de react?")

print(to_markdown(response.text).data)

response.candidates
