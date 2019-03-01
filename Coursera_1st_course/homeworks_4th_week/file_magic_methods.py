import tempfile
import os

class File:
    def __init__(self, file_name):
        self.file_name = file_name
        self.count_lines = 0

    def __getitem__(self, text):
        return text

    def write(self, text):
        with open(self.file_name, "w+") as f:
            f.write(text)
        return f

    def __add__(self, obj):
        new_file = os.path.join(tempfile.gettempdir(), "new_file.txt")
        with open(self.file_name, "r") as f:
            self_data = f.read()
        with open(obj.file_name, "r") as f:
            obj_data = f.read()
        with open(new_file, "w") as f:
            f.write(f"{self_data}{obj_data}")
        return File(new_file)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file_name, "r") as f:
            lines_list = f.readlines()
            if self.count_lines == len(lines_list):
                self.count_lines = 0
                raise StopIteration
            result = lines_list[self.count_lines].strip()
            self.count_lines += 1
        return result


    def __str__(self):
        return f"{self.file_name}"
