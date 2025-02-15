from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

@app.get("/hello-world")
def get_hello_world():
    return {"message": "Hello World!"}