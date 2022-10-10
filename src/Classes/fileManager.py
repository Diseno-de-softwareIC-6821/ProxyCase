import pathlib


class FileManager():
    def __init__(self):
        # Get the current path, solving problem saving files on same fileManager.py path
        self.path = str((pathlib.Path(__file__).parent.resolve()))
        self.path = self.path[:self.path.find("src")] + "files\\"

    def loadTxt(self, mode):
        txtData = ""
        try:
            if (mode == 1):
                txt = open(self.path + "logs.txt", "r")
            elif (mode == 2):
                txt = open(self.path + "record.txt", "r")
            txtData = txt.read()
            txt.close()
        except:
            print("Error: File not found")
        return txtData

    def saveTxt(self, data, mode):
        newTxt = data + "\n"
        try:
            if (mode == 1):
                txt = open(self.path + "logs.txt", "a")
            elif (mode == 2):
                txt = open(self.path + "record.txt", "a")
            txt.write(newTxt)
            txt.close()
        except:
            print("Error saving file")
