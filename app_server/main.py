from urllib import request
from utility.file_read import FileRead
import os
import sys
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from utility.modal import FileUpload, UploadFileResponse
from fastapi.middleware.cors import CORSMiddleware  # Add this line

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    print(request)
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/create/")
def create_element(request: Request):
    print(request)
    return templates.TemplateResponse("create.html", {"request": request})


@app.post("/upload/")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()

    file_name = file.filename
    
    file_path = f"uploads/{file_name}"

    absolute_path = os.path.abspath(file_path)
    print(f"ABS PATH {absolute_path}")
    with open(file_path, "wb") as f:
        f.write(contents)

    fl_obj = FileRead(file, absolute_path)
    data = fl_obj.render_read_file()
    print(data)

    return {"status_code": 200, "message":"File read successfully", "data":data, "file_type":fl_obj.file_type(), "file_name":file_name}

@app.get("/view/{file_name}/")
async def view_file(request: Request, file_name: str):
    file_upload = FileUpload()
    file_upload.read_file(f"uploads/{file_name}")

    return templates.TemplateResponse("template.html", {"request": request, "file_content": file_upload.get_content()})
