from Data_structure.strucure import Linklist
class User:
    def __init__(self,National,Name,Lname,Date,Password):
        self.National = int(National)
        self.Name = Name 
        self.Lname = Lname
        self.Date = Date 
        self.Password = Password
        self.Linklist_Plate = Linklist()
    def __repr__(self):
        return f'{self.National} | {self.Name} | {self.Lname} | {self.Date} | {self.Password} | {self.Linklist_Plate}'