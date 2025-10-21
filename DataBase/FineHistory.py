import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.CityNumber import Hash_Data,City_Array
from models.FineNode import Fine
from Data_structure.strucure import Hash
HashFine = Hash()
with open('FinalProject/TestFile/penalties.txt','r') as History:
    for line in History:
        FineSerial,DriverID,PlateNumber,DateFine,Finelevel,Description = line.strip().split(' | ')
        new_Fine = Fine(DriverID,DateFine,Finelevel,Description,FineSerial,PlateNumber)
        HashFine.insert(FineSerial,new_Fine)
        for i in range(len(City_Array)):
            if City_Array[i].Citycode == PlateNumber.split('-')[1]:
                PlateNumber = PlateNumber.split('-')[0]
                PlateNumber = PlateNumber[0:2] + str(ord(PlateNumber[2])) + PlateNumber[3:]
                City_Array[i].PBST.search(PlateNumber).Finehistory.insert(new_Fine)
                break
        for j in range(len(Hash_Data)):
            if Hash_Data[j] != None and Hash_Data[j].license == DriverID:
                Hash_Data[j].Finehistory.insert(new_Fine)
        






        


