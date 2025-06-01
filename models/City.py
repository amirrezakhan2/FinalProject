from Data_structure.strucure import BST
class CityNode:
    def __init__(self,Number,Name):
        self.CityName = Name
        self.Citycode = Number
        self.PBST = BST()
    def __repr__(self):
        return f'{self.CityName} | {self.Citycode}'


