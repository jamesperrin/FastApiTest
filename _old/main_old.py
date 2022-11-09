import os
import uvicorn
import configparser

from fastapi import FastAPI
from pathlib import Path

app = FastAPI()

# what extensions are allowed to send
ALLOWED_EXTENSIONS = set(
    ['txt', 'csv', 'xlsx', 'odt', 'rtf', 'dat', 'doc', 'docx', 'kid', 'pdf'])

workingDir = os.getcwd()

configFileName = 'r2araconfig.ini'

cfg = configparser.ConfigParser()
cfg.read(os.path.join(workingDir, configFileName))
UploadFolder = Path(cfg['DEFAULT']['Upload_Folder'])
secret_key = cfg['DEFAULT']['secret_key']
# Address = str(cfg['DEFAULT']['Address'])
Port = int(cfg['DEFAULT']['Port'].strip("'"))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

if __name__ == "__main__":
    print(f"PROCESS: uvicorn.run('main:app', host='127.0.0.1', port={Port})")
    # uvicorn.run("main:app", host='127.0.0.1', port=8080,  log_level="info", reload=True)
    #HTTPS
    # uvicorn.run("main:app", host='127.0.0.1', port=Port, log_level="info", reload=True, ssl_keyfile="./key.pem", ssl_certfile="./cert.pem")
    #HTTP
    uvicorn.run("main:app", host='127.0.0.1', port=Port,
                log_level="info", reload=True)
