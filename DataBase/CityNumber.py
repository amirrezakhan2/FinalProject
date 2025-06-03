import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.Userinfo import Hash_Data
from models.City import CityNode
from Data_structure.strucure import Array
from models.Plate import PlateNode
City_Array = Array(9)
with open('FinalProject/TestFile/citycode.txt','r') as Code:
    for line in Code:
        Code_City,City_Name = line.rstrip().split(' | ')
        new_City = CityNode(Code_City,City_Name)
        City_Array.insert(new_City)

with open('FinalProject/TestFile/cars.txt','r') as ca:
     for line in ca:
          CarID,c,d,PlateNumber,d,National =line.rstrip().split(' | ')
          # print(Hash_Data.search(int(National)))

          for i in range(len(City_Array)):
               if City_Array[i].Citycode == PlateNumber.split('-')[1]:
                    result = PlateNumber.split('-')[0]
                    a = result[0:2]
                    b = result [3:6]
                    result = a + str(ord(result[3])) + b 
                    new_node = PlateNode(City_Array[i].CityName,National,PlateNumber,int(result),CarID)
                    City_Array[i].PBST.insert(new_node)
                    Hash_Data.search(int(National)).Linklist_Plate.insert(new_node)



