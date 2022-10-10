
from interfaces.i_bd_manager import IBdManager as IBD
from Classes.DataBase import DataBase
from datetime import datetime
from Classes.fileManager import FileManager


class Proxy(IBD):
    dataBase = None

    def __init__(self, fileman: FileManager) -> None:
        super().__init__()
        self.dataBase = DataBase()
        self.fm = fileman

    def insert(self, json: str) -> int:

        self.fm.saveTxt(str(datetime.now()) +
                        " Insert Into TABLA (json) values "+json, 1)
        id: int = self.dataBase.insert(json)  # 2 = insert into database
        self.fm.saveTxt(str(datetime.now())+" id:" +
                        str(id) + " sucess", 2)  # 3 = record.txt
        return id

    def update(self, u_id: int, json: str) -> int:

        self.fm.saveTxt(str(datetime.now()) +
                        " Updating Into TABLA (json) values "+json, 1)

        id: int = self.dataBase.update(u_id, json)

        self.fm.saveTxt(str(datetime.now())+" id:" +
                        str(id) + " sucess", 2)  # 3 = record.txt
        return id

    def delete(self, u_id: int) -> int:

        self.fm.saveTxt(str(datetime.now()) +
                        " Deleting json where id="+str(u_id), 1)
        id: int = self.dataBase.delete(u_id)

        self.fm.saveTxt(str(datetime.now())+" id:" +
                        str(id) + " success", 2)  # 3 = record.txt
        return id
