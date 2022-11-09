import os
import uvicorn
import configparser

from fastapi import FastAPI, status
from pathlib import Path

description = """
A REST API for R2RA. Receives files from VistA.
------------------------------
Below is a list of endpoints that can be accessed via the API, each endpoint.
"""

app = FastAPI(
    title="Applications R2ARA API", description=description, version="0.0.1", debug=True
)

# what extensions are allowed to send
ALLOWED_EXTENSIONS = set(
    ['txt', 'csv', 'xlsx', 'odt', 'rtf', 'dat', 'doc', 'docx', 'kid', 'pdf'])

workingDir = os.getcwd()

configFileName = 'r2araconfig.ini'

cfg = configparser.ConfigParser()
cfg.read(os.path.join(workingDir, configFileName))
UploadFolder = Path(cfg['DEFAULT']['Upload_Folder'])

env_port = os.environ["PORT"]

if env_port is not None:
    print(f"PRINT: env_port {env_port}")
    Port = int(env_port)

else:
    # print(f"PRINT: env_port NOT FOUND")
    Port = int(cfg['DEFAULT']['Port'].strip("'"))


@app.get("/api/v1/")
async def root():
    print(f"PRINT: Called /root")
    return {"message": "Hello World ROOT"}


@app.get("/api/v1/home", status_code=status.HTTP_200_OK)
async def home():
    print(f"PRINT: Called /home")
    return {"message": "Hello World HOME"}


@app.get("/api/v1/users/me")
async def read_user_me():
    print(f"PRINT: Called /users/me")
    return {"user_id": "the current user"}


@app.get("/api/v1/users/{user_id}")
async def read_user(user_id: str):
    print(f"PRINT: Called /users/{user_id}")
    return {"user_id": user_id}


if __name__ == "__main__":
    # HTTPS
    # uvicorn.run("main:app", host='127.0.0.1', port=Port, log_level="info",
    #             reload=True, ssl_keyfile="./key.pem", ssl_certfile="./cert.pem")
    # HTTP
    # config = uvicorn.run("main:app", host='127.0.0.1', port=Port,
    #             log_level="info", reload=True)
    # uvicorn.run("main:app", host='127.0.0.1', port=8080,
    #             log_level="info", reload=True)
    # config = uvicorn.Config("main:app", host='127.0.0.1',
    #                         port=5000, log_level="info")
    config = uvicorn.Config("main:app", host='0.0.0.0', port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
