import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data_structure.strucure import Linklist,DynamicArray
class User:
    def __init__(self,National,Name,Lname,Date,Password):
        self.National = int(National)
        self.key = int(National)
        self.Name = Name 
        self.Lname = Lname
        self.Date = Date 
        self.Password = Password
        self.Linklist_Plate = Linklist()
        self.StatusDriver = False
        self.license = None
        self.Datelicense = None
        self.BlockDay = 0
        self.negative = 0
        self.Finehistory = DynamicArray()


        
    def __repr__(self):
        return f'{self.National} | {self.Name} | {self.Lname} | {self.Date} | {self.Password} | {self.Linklist_Plate}'