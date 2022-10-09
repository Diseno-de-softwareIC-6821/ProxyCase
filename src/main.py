import pathlib
import sys

sys.path.append(str((pathlib.Path(__file__).parent.resolve())) + "\\Classes") 

import fileManager as fm

def main() -> None:
    fileManager = fm.FileManager()
    print(fileManager.loadTxt(1))

if __name__ == "__main__":
    main()
