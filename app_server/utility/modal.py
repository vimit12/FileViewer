from pydantic import BaseModel


class FileUpload:
    def __init__(self):
        self._filename = None
        self._content = None

    def read_file(self, filename):
        with open(filename, 'r') as file:
            self._content = file.read()

    def get_content(self):
        return self._content

    def get_filename(self):
        return self._filename

class UploadFileResponse():
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
