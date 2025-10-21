import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataBase.FineHistory import City_Array,Hash_Data
from models.HistoryPlate import PlateHistory
count = 0
with open('FinalProject/TestFile/ownership_history.txt','r') as History:
    for line in History:
        CarID,NationalCode,StartDate,EndDate,Plate = line.strip().split(' | ')
        new_History = PlateHistory(CarID,NationalCode,StartDate,EndDate,Plate)
        Backup_Plate = Plate

        for i in range(len(City_Array)):
            if City_Array[i].Citycode == Plate.split('-')[1]:
                result = Plate.split('-')[0]
                result = result[0:2] + str(ord(result[2])) + result[3:]
                City_Array[i].PBST.search(result).CarHistory.insert(new_History)
                break
