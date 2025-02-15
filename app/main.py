from fastapi.responses import RedirectResponse
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

@app.get("/hello-world")
def get_hello_world():
    return {"message": "Hello World!"}