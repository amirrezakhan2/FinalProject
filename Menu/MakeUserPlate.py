import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.Userinfo import Hash_Data
from models.Plate import PlateNode,MakePlate
from DataBase.CityNumber import City_Array,Hash_Data
def MakePlate_User(City,NationalCode):
    for i in range(len(City_Array)):
        if City_Array[i].CityName == City:
            Code = City_Array[i].Citycode
            Creater = MakePlate()
            key,Plate = Creater.plateMaker()
            while City_Array[i].PBST.search(int(key)):
                key,Plate = Creater.plateMaker()
            Plate += '-' + Code
            new_Plate = PlateNode(City_Array[i].CityName,NationalCode,Plate,key)
            City_Array[i].PBST.insert(new_Plate)
            Hash_Data.search(NationalCode).Linklist_Plate.insert(new_Plate)
            return Plate
    else:
      return False











