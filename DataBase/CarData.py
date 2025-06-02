import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Car import CarNode
from Data_structure.strucure import BST
CarBST = BST()
with open('FinalProject/TestFile/cars.txt','r') as ca:
     for line in ca:

          CarID,Name,Date,PlateNumber,Color,Natinal =line.rstrip().split(' | ')
          new_NodeCar = CarNode(CarID,Name,Date,PlateNumber,Color,Natinal)
          CarBST.insert(new_NodeCar)


