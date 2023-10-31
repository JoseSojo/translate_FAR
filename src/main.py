from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import goslate

def Trans(text, last):
    gs = goslate.Goslate()
    translate = gs.translate(text, last)

    return translate

app = FastAPI()

origins = ['http://localhost', 'http://localhost:5173']
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


class RequesTranslate(BaseModel):
    text_buffer: str

@app.get('/')
def index():
    return {'response':'Hola Mundo'}

@app.get('/translate/{from_payload}/{to_payload}/{text_buffer}')
async def translate_text_buffer(from_payload: str, to_payload: str, text_buffer:str):
    try:
        traduction = Trans()    

        return {'from':from_payload, 'to':to_payload, 'last_text':text_buffer, 'translate_result':traduction}
    except Exception:
        return { 'error temporal' }

