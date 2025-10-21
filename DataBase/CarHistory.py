import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.CarData import CarBST
from models.HistoryPlate import PlateHistory
with open('FinalProject/TestFile/ownership_history.txt','r') as History:
    for line in History:
        CarID,NationalCode,StartDate,EndDate,Plate = line.strip().split(' | ')
        new_History = PlateHistory(CarID,NationalCode,StartDate,EndDate,Plate)
        CarBST.search(CarID).HistorySellBuy.insert(new_History)
