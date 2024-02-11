from urllib import request

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from ModalClass.modal import FileUpload, UploadFileResponse
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
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)

    return UploadFileResponse(status_code=200, message="File uploaded successfully")

@app.get("/view/{file_name}/")
async def view_file(request: Request, file_name: str):
    file_upload = FileUpload()
    file_upload.read_file(f"uploads/{file_name}")

    return templates.TemplateResponse("template.html", {"request": request, "file_content": file_upload.get_content()})
