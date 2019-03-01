
class FileReader:
    def __init__(self,  file = ""):
        self.file = file
        return

    def read(self):
        try:
            with open(self.file,"r") as f:
                result = f.read()
                return result
        except IOError:
            return ""

reader = FileReader("coursera_week3_cars.csv")
print(reader.read())
