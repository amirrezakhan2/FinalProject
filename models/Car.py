import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data_structure.strucure import BaseNode

class CarNode(BaseNode):
    def __init__(self,serial,name,date,plate,color,NationalCode):
        super().__init__(int(serial))
        self.name = name 
        self.Date = date 
        self.serial = int(serial)
        self.plate = plate 
        self.color = color 
        self.National = NationalCode

    def __repr__(self):
        return f"{self.serial} | {self.name} | {self.plate} | {self.National} | {self.color} | {self.Date}"