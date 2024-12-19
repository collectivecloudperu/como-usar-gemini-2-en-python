from google import genai

cliente = genai.Client(api_key="")

respuesta = cliente.models.generate_content(
    model='gemini-2.0-flash-exp', contents='Donde esta la Torre Eifel?'
)

print(respuesta.text)