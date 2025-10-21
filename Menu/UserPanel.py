import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataBase.FineHistory import Hash_Data
# from DataBase.FineHistory import City_Array 
from models.Plate import PlateNode,MakePlate
from Menu.ManagerPanel import CarBST 
from DataBase.PlateHistory import City_Array
# from DataBase.CarData import CarBST
def inorder(root, Type):
    result = ''
    if root is not None:
        result += inorder(root.left, Type)

        if hasattr(root, Type):
            result += f"{getattr(root, Type)} | "

        result += inorder(root.right, Type)
    return result

# def SavePlate():
#     with open('FinalProject/TestFile/Plate.txt', 'w') as file:
#         for i in range(len(City_Array)):
#             plate = inorder(root=City_Array[i].PBST.root,Type='plate')
#             for j in plate.split(' | '):
#                 if j and j != 'None':
#                     j = j.split('-')[0]
#                     key = j[0:2] + str(ord(j[2])) + j[3:]
#                     file.write(f'{City_Array[i].PBST.search(key).plate} | {City_Array[i].PBST.search(key).StartDate} | {City_Array[i].PBST.search(key).serial} | {City_Array[i].PBST.search(key).National}\n')

def MakePlate_User(City,NationalCode):
    for i in range(len(City_Array)):

        if Hash_Data.search(NationalCode).BlockDay == 0:
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

                return True,Plate
        else:
            return False,print('You can not make a new plate')
    else:
      return False,print('you are ban form systeam')

def SeePlate(Natinal):
    PlateInfo = Hash_Data.search(Natinal).Linklist_Plate 
    temp = PlateInfo.head 
    if temp == None:
        return print('you do not have any plate')
    while temp :
        print(temp.data)
        temp = temp.next

from DataBase.CarData import CarBST
def SeeCar(National):
    count = 0
    Carinfo = Hash_Data.search(National).Linklist_Plate
    temp = Carinfo.head
    if temp == None :
        return print('you dont Have any Car')
    else:
        while temp:
            if temp.data.serial == None:
                pass
            else:
                count += 1
                print(CarBST.search(temp.data.serial))
            temp = temp.next
        if count == 0:
                return print('you dont Have any Car')

    

def SeeFine(NationalCode):
    InFo = Hash_Data.search(NationalCode)
    if len(InFo.Finehistory) != 0:
        return print(InFo.Finehistory)
    else:
        return print('you dont have any fine')

def SeeFinePLate(National):
    info = Hash_Data.search(National)
    PlateLL = info.Linklist_Plate
    temp = PlateLL.head 
    PlateEnter = input('Enter the plate you want see the fine:\n')
    while temp :
       if PlateEnter == temp.data.plate:
            Plate = PlateEnter.split('-')[0]
            key = Plate[0:2] + str(ord(Plate[2])) + Plate[3:]
            for i in range(len(City_Array)):
               code = PlateEnter.split('-')[1]
               if City_Array[i].Citycode == code:
                return print(City_Array[i].PBST.search(int(key)).Finehistory)
       temp = temp.next
    else:
        return print('you dont have this plate')
    
def User_Seenegative(National):
    if Hash_Data.search(National):
        User = Hash_Data.search(National)
        if User.negative > 0:
            print(f'You have {User.negative} negative points')

        else:
            print('You have no negative points')

def History(Nationalcode):
    Plate_Enter = input('Enter the plate you want see History:\n')
    temp = Hash_Data.search(Nationalcode).Linklist_Plate.head
    while temp:
        if temp.data.plate == Plate_Enter:
            for i in range(len(temp.data.CarHistory)):
                print(f'Car info:{CarBST.search(temp.data.CarHistory[i].CarID)} | Start Date:{temp.data.CarHistory[i].StartDate} | End Date:{temp.data.CarHistory[i].EndDate}')

            break

        temp = temp.next 
    else:
        return print('the plate is not yours ')