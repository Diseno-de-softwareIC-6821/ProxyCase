"""Module used to simulate an interface for other classes to implement"""
from abc import ABC, abstractmethod

class IBdManager(ABC):
    """Class that simulates an interface"""

    @abstractmethod
    def insert(self, json: str) -> int:
        """Abstract method that will be implemented by class children"""

    @abstractmethod
    def update(self, u_id: int, json: str) -> int:
        """Abstract method that will be implemented by class children"""

    def delete(self, u_id: int) -> int:
        """Abstract method that will be implemented by class children"""
