from interfaces.i_bd_manager import IBdManager as IBD
from datetime import datetime
import random


class DataBase(IBD):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, json: str) -> int:
        createTS = datetime.now()
        print(createTS, "Insert into", json)
        # Return a random number between 0 and 100
        return random.randint(0, 10)

    def update(self, u_id: int, json: str) -> int:
        createTS = datetime.now()
        print(createTS, "Updating data", json)
        return u_id

    def delete(self, u_id: int) -> int:
        createTS = datetime.now()
        print(createTS, "Deleting data")
        return u_id
