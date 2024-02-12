import json
import pandas as pd


class FileRead:

    def __init__(self, file, abs_file_path):
        self._file_obj = file
        self._abs_path = abs_file_path

    def file_type(self):
        return self._file_obj.filename.split(".")[-1]
    

    def render_read_file(self):
        data = None
        if self.file_type() == 'json':
            data = self.__json_file_read()
        elif self.file_type() in ['xlsx', 'xls']:
            ...
        else:
            ...
        
        return data

    def __json_file_read(self):
        data = None
        with open(self._abs_path, 'r') as file:
            data = file.read()
        return data
