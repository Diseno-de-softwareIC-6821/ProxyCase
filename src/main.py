import pathlib
import sys
from time import sleep


from Classes import fileManager as fm
from Classes import Proxy

"""
Diagram link: 
https://app.diagrams.net/#G1URfbuWhEchDjLqOndiq2CUmI-8b-JjaN
"""


def main() -> None:
    fileManager = fm.FileManager()
    proxy = Proxy.Proxy(fileManager)
    id: int = proxy.insert("{name: Esteban, phone: [1,2,3]}")
    sleep(5)
    id: int = proxy.update(2, "{name: Daniel, lastname: Sambucci}")
    id: int = proxy.delete(3)
    sleep(5)
    id: int = proxy.insert("{name: Daniel, lastname: Cornejo}")
    sleep(5)


if __name__ == "__main__":
    main()
