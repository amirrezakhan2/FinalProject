from Data_structure.strucure import BST,Array
import random
class CityNode:
    def __init__(self,Number,name):
        self.CityName = name
        self.Citycode = Number
        self.PBST = BST()
    def __repr__(self):
        return f'{self.CityName} | {self.Citycode}'


