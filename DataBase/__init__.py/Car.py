class CarNode:
    def __init__(self,serial,name,date,plate,color,NationalCode):
        self.name = name 
        self.date = date 
        self.serial = int(serial)
        self.plate = plate 
        self.color = color 
        self.National = NationalCode
        self.left = None 
        self.right = None 
        self.Parent = None
        self.key = int(serial)
    def __repr__(self):
        return f"{self.serial} | {self.name} | {self.plate} | {self.National}"