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
          for i in range(len(City_Array)):
               if City_Array[i].Citycode == PlateNumber.split('-')[1]:
                    result = PlateNumber.split('-')[0]
                    result = result[0:2] + str(ord(result[2])) + result [3:]
                    new_node = PlateNode(City_Array[i].CityName,National,PlateNumber,result,CarID)
                    if CarID:
                         new_node.Status = True
                    City_Array[i].PBST.insert(new_node)
                    Hash_Data.search(int(National)).Linklist_Plate.insert(new_node)
# with open('FinalProject/TestFile/Plate.txt','r') as file:
#      for line in file:
#           Plate,Start,CarID,National = line.split(' | ')
#           key,citycode = Plate.split('-')
#           key = key[0:2] + str(ord(key[2])) + key[3:]
#           for i in range(len(City_Array)):
#                if City_Array[i].Citycode == citycode:
#                     info = City_Array[i].PBST.search(key)
#                     if info:
#                          info.StartDate = Start
#                     else:
#                          new_node = PlateNode(City_Array[i].CityName,National,PlateNumber,key,CarID)
#                          City_Array[i].PBST.insert(new_node)
#                          Hash_Data.search(int(National)).Linklist_Plate.insert(new_node)

                         





