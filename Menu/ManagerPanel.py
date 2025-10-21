import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
from DataBase.CarData import color_array
from DataBase.CarHistory import CarBST
from models.Car import CarNode
from DataBase.PlateHistory import City_Array
from DataBase.FineHistory import Hash_Data
from models.HistoryPlate import PlateHistory
from Menu.Signup import SignUp
from models.FineNode import Fine
import random
from DataBase.FineHistory import HashFine
from Menu.Signup import SaveUser
from Data_structure.strucure import Linklist

def SaveCarData():
    information = inorder(root=CarBST.root, Type='serial')
    with open('FinalProject/TestFile/cars.txt', 'w') as file:
        for i in information.split(' | '):
            if i and i != 'None':
                CarData = CarBST.search(int(i))
                file.write(f"{CarData.serial} | {CarData.name} | {CarData.Date} | {CarData.plate} | {CarData.color} | {CarData.National}\n")
def SaveHitory():
    information = inorder(root=CarBST.root, Type='serial')
    with open('FinalProject/TestFile/ownership_history.txt', 'w') as file:
        for i in information.split(' | '):
            if i and i != 'None':
                CarData = CarBST.search(int(i))
                for i in range(len(CarData.HistorySellBuy)):
                    file.write(f'{CarData.HistorySellBuy[i].CarID} | {CarData.HistorySellBuy[i].National} | {CarData.HistorySellBuy[i].StartDate} | {CarData.HistorySellBuy[i].EndDate} | {CarData.HistorySellBuy[i].Plate}\n')
def SaveDriver():
    with open('FinalProject/TestFile/drivers.txt', 'w') as file:
        for i in range(len(Hash_Data)):
            if Hash_Data[i] != None and Hash_Data[i].license:
                file.write(f'{Hash_Data[i].National} | {Hash_Data[i].license} | {Hash_Data[i].Datelicense}\n')
def SaveFine():
    with open('FinalProject/TestFile/penalties.txt', 'w') as file:
        for i in range(len(HashFine)):
            if HashFine[i] != None:
                file.write(f'{HashFine[i].trackingnumber} | {HashFine[i].DriverId} | {HashFine[i].Plate} | {HashFine[i].DateFine} | {HashFine[i].Finelevel} | {HashFine[i].Description }\n')

def SaveNegative():
    with open('FinalProject/TestFile/phase4.txt', 'w') as file:
        for i in range(len(Hash_Data)):
            if Hash_Data[i] != None and Hash_Data[i].license:
                file.write(f'{Hash_Data[i].National} | {Hash_Data[i].license} | {Hash_Data[i].negative}\n')
# def SavePlate():
#     with open('FinalProject/TestFile/Plate.txt', 'w') as file:
#         for i in range(len(City_Array)):
#             plate = inorder(root=City_Array[i].PBST.root,Type='plate')
#             for j in plate.split(' | '):
#                 if j and j != 'None':
#                     key = j[0:2] + str(ord(j[2])) + j[3:]
#                     file.write(f'{City_Array[i].PBST(key).plate} | {City_Array[i].PBST(key).StartDate} | {City_Array[i].PBST(key).serial}')




def color_Search(color):
    for i in range(len(color_array)):
        if color_array[i] == color:
            return True
    return False

def Date_plate(key,code,Serial):
    import datetime
    for i in range(len(City_Array)):
        if City_Array[i].Citycode == code:
             find_plate = City_Array[i].PBST.search(int(key))
             find_plate.StartDate = str(datetime.datetime.now().date())
             find_plate.serial = Serial
             find_plate.Status = True
             return find_plate.National
    else:
      return False

def Check_serial(serial):
    if len(serial) == 5:
        if serial.isdigit():
            return True
        else:
            return False
    else:
        return False

def Car_registration():

    Status_color = False
    Carname = input('Enter the car name:\n')
    Carcolor = input(f'Enter the car color:{color_array}\n ')
    Status_color = color_Search(Carcolor)
    if Status_color == True:
        year_make = input('Enter the Year of manufacture\n')
        Serial_car = input('Enter the car serial:\n')
        if CarBST.search(Serial_car):
            return False,print('the car serial is already exist')
        else:
            Carplate = input('Enter the car plate:\n')
            key,Citycde = Carplate.split('-')
            key = key[0:2] + str(ord(key[2])) + key[3:]
            National = Date_plate(key,Citycde,Serial_car)
            if National:
                new_Car = CarNode(Serial_car,Carname,year_make,Carplate,Carcolor,National)
                CarBST.insert(new_Car)
                SaveCarData()
                return True,print('Car add successful')
            else:
              return False,print('Plate is not exist')
    else:
            return False,print('color dose not exist')

def inorder(root, Type):
    result = ''
    if root is not None:
        result += inorder(root.left, Type)

        if hasattr(root, Type):
            result += f"{getattr(root, Type)} | "

        result += inorder(root.right, Type)
    return result

def SeeALLCar():
    print(CarBST)

def SeeALLUser():
    for i in range(len(Hash_Data)):
        if Hash_Data[i] != None:
            print(Hash_Data[i])
def SeeALLCityPlate():
    City = input('Enter the City  you want:\n').capitalize()

    for i in range(len(City_Array)):
        if City_Array[i].CityName == City:
            print(City_Array[i].PBST)

def SeeALLCarCity():
    City = input('Enter the City  you want:\n').capitalize()
    for i in range(len(City_Array)):
        if City_Array[i].CityName == City:
            serial = inorder(City_Array[i].PBST.root,'serial').rstrip(' |')

            for i in serial.split(' | '):

                if i!= None and i != 'None'and i != '':
                    print(CarBST.search(i))

def DateSearch():
    user_input = input('Enter the year . Leave empty to show all: ').split()

    if len(user_input) == 2:
        Start = int(user_input[0])
        End = int(user_input[1])
        FindCarbyDate(CarBST.root, Start, End)
    elif len(user_input) == 1:
        Start = int(user_input[0])
        FindCarbyDate(CarBST.root, Start)
    elif len(user_input) == 0:
            print(CarBST)
    else:
        print("Invalid input.")
        
def FindCarbyDate(root,Start,End=None):
    if root is not None:
        FindCarbyDate(root.left,Start,End)
        Date = int(root.Date)
        if End is not None:
            if Start<= Date <= End:
                print(f'{root.serial} | {root.Date} | {root.color} | {root.plate}') 
        else:
            if Date == Start:
                print(f'{root.serial} | {root.Date} | {root.color} | {root.plate}') 

        FindCarbyDate(root.right,Start,End)


def SeeALLOwnerCity():
    City = input('Enter the city you want:\n').capitalize()

    for i in range(len(City_Array)):
        if City_Array[i].CityName == City:
            national_list = inorder(City_Array[i].PBST.root, 'National').rstrip(' |')

            if not national_list:
                print("No owners found in this city.")
                return

            for national_code in national_list.split(' | '):
                user = Hash_Data.search(int(national_code))

                temp = user.Linklist_Plate.head
                found_active = False
                while temp:
                    if temp.data.Status == True and temp.data.plate.split('-')[1]==City_Array[i].Citycode:
                        if not found_active:
                            print(f'{user.National} | {user.Name} | {user.Lname} | {user.Date}')
                            found_active = True
                    temp = temp.next
            return

    print(f"City '{City}' not found.")

def ChangeUsername():
    old_Username = input('Enter the Username code:\n')
    new_Username = input('Enter the new Username:\n')
    result = Hash_Data.change_key(old_Username, new_Username)
    SaveUser()
    if result:
        return new_Username 
    else:
        return None



def SeeCarHistory():
    CarID = input('Enter the CarId you want to see History\n')
    car = CarBST.search(CarID)
    if car:
            for i in range(len(car.HistorySellBuy)):
                print('National Code:', car.HistorySellBuy[i].National)
                print('Start Date:', car.HistorySellBuy[i].StartDate)
                print('End Date:', car.HistorySellBuy[i].EndDate)
                print('Plate:', car.HistorySellBuy[i].Plate)

    else:
        print("Car not found.")

def RegisteredDriver():
    for i in range(len(Hash_Data)):
        if Hash_Data[i] != None and Hash_Data[i].StatusDriver == True:
            print(f'license:{Hash_Data[i].license} | Nationalcode"{Hash_Data[i].National} | Datelicense:{Hash_Data[i].Datelicense}')

def DeleteCar():
        CarID = int(input('Enter the CarID:\n'))
        car = CarBST.search(CarID)
        if not car:
            print("Car not found.")
            return
                
        Plate = car.plate
        print(f"Plate: {Plate}")
        codecity = Plate.split('-')[1]
        Plate = Plate.split('-')[0]
        key_plate = Plate[0:2] + str(ord(Plate[2])) + Plate[3:]
                
        for i in range(len(City_Array)):
            if City_Array[i].Citycode == codecity:
                changeinfo = City_Array[i].PBST.search(int(key_plate))
                if not changeinfo:
                    print("Plate not found in city records.")
                    return
                
                print(f"Change Info: {changeinfo}")
                changeinfo.Status = False
                changeinfo.serial = None
                
        CarBST.Delete(CarID)
        SaveCarData()
        print("Car deleted successfully.")
            



def chnageowner():
    keychange = input('Enter the key you want to change owner:1-CarID 2-Plate\n')
    if keychange == '1':
        changeowner_by_id()
    elif keychange == '2':
        changeowner_by_plate()
        
def changeowner_by_plate():
    Plate = input('Enter the Plate you want to change owner:\n')
    key, Citycode = Plate.split('-')
    key = key[0:2] + str(ord(key[2])) + key[3:]
    for i in range(len(City_Array)):
        if City_Array[i].Citycode == Citycode:
            find_plate = City_Array[i].PBST.search(int(key))
            
            if find_plate.serial is not None:

                car = CarBST.search(find_plate.serial)
                new_plate = input('Enter the new plate:\n')
                new_key, new_Citycode = new_plate.split('-')
                new_key = new_key[0:2] + str(ord(new_key[2])) + new_key[3:]
                for j in range(len(City_Array)):
                    if City_Array[j].Citycode == new_Citycode:
                        find_new_plate = City_Array[j].PBST.search(int(new_key))
                        if find_new_plate.serial is None:
                            new_Hitory = PlateHistory(car.serial, find_plate.National, find_plate.StartDate, str(datetime.datetime.now().date()), find_plate.plate)
                            car.HistorySellBuy.insert(new_Hitory)
                            find_plate.CarHistory.insert(new_Hitory)
                            find_new_plate.serial = car.serial
                            find_new_plate.Status = True
                            find_new_plate.StartDate = str(datetime.datetime.now().date()),
                            car.plate = new_plate
                            car.National = find_new_plate.National
                            find_plate.serial = None
                            SaveCarData()
                            SaveHitory()
                            return print('Owner changed successfully')
                        else:
                            return print('This plate is already registered to another car.')


def changeowner_by_id():

        CarID = input('Enter the CarID you want to change owner:\n')
        car = CarBST.search(CarID)
        if not car:
            print("Car not found.")
            return


        new_plate = input('Enter the new plate:\n')
        key, Citycode = new_plate.split('-')
        key = key[0:2] + str(ord(key[2])) + key[3:]


        for j in range(len(City_Array)):
            if City_Array[j].Citycode == Citycode:
                find_plate = City_Array[j].PBST.search(int(key))
                if not find_plate:
                    print("New plate not found in city records")
                    return


                if find_plate.serial is None:

                    plate = car.plate
                    old_key, old_codecity = plate.split('-')
                    old_key = old_key[0:2] + str(ord(old_key[2])) + old_key[3:]

                    for i in range(len(City_Array)):
                        if City_Array[i].Citycode == old_codecity:
                            old_plate = City_Array[i].PBST.search(int(old_key))
                            if old_plate:
                                old_plate.Status = False
                                old_plate.serial = None
                             


                    new_Hitory = PlateHistory(car.serial, old_plate.National, old_plate.StartDate, str(datetime.datetime.now().date()), old_plate.plate)
                    car.HistorySellBuy.insert(new_Hitory)
                    old_plate.CarHistory.insert(new_Hitory)


                    find_plate.serial = car.serial
                    find_plate.Status = True
                    find_plate.StartDate = str(datetime.datetime.now().date())
                    car.plate = new_plate
                    car.National = find_plate.National
                    SaveCarData()
                    SaveHitory()
                    print('Owner changed successfully')
                    return
                else:
                    print('This plate is already registered to another car')


def removelicense():
    Natinal = input('Enter the National Code driver:\n')
    if Natinal:
        driver = Hash_Data.search(Natinal)
        driver.StatusDriver = False
        driver.license = None
        driver.BlockDay = 0
        driver.negiative = 0
        driver.Finehistory.restartArray
        print('Driver remove successfully ')
        SaveDriver()
    else:
        print('driver dose  not exist')

def SeeownerCarHistory():
    CarID = input('Enter the CarId you want to see History\n')
    car = CarBST.search(CarID)
    if car:
            for i in range(len(car.HistorySellBuy)):
                print('National Code:', car.HistorySellBuy[i].National)
                print('owner name:',Hash_Data.search(car.HistorySellBuy[i].National).Name)
                print('Start Date:', car.HistorySellBuy[i].StartDate)
                print('End Date:', car.HistorySellBuy[i].EndDate)
                print('Plate:', car.HistorySellBuy[i].Plate)

    else:
        print("Car not found.")

def BlockingDriver():
    key_for_search = input('Enter the key you want find the driver:1-Nationalcode,2-liecese\n')
    if key_for_search == '1':
        Nationalcode = input('Enter the Natioanlcode')
        Hash_Data.search(Nationalcode).StatusDriver = False
        return print('Driver blocked successfully')
    if key_for_search == '2':
        license = input('Enter the license')
        for i in range(len(Hash_Data)):
            if Hash_Data[i] != None and Hash_Data[i].license == license:
                Hash_Data[i].StatusDriver = False
                return print('Driver blocked successfully')

def Makelicense():
    status = False
    while status == False:
        number = str(random.randint(10000000, 99999999))
        for i in range(len(Hash_Data)):
            if Hash_Data[i] != None and Hash_Data[i].license == number:
                status = False
                break
            else:
                status = True
    return number


def calculate_age_years(birth_date_str):

    birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    today = datetime.datetime.today()
    age = today.year - birth_date.year
    return age

def Drivinglicense():

    Nationalcode = input('Enter the Natioanlcode:\n')
    info = Hash_Data.search(Nationalcode)
    if info:
            age = calculate_age_years(info.Date)
            if age < 18:
                return print('You are not old enough to get a driving license')
            else:
                info.Datelicense = str(datetime.datetime.now().date())
                info.StatusDriver = True
                info.license = Makelicense()
                SaveDriver()
                return print(f'Your driving license is {info.license}')
    else:
        SignUp()
        Drivinglicense()
        
def MakeFine():

    license = input('Enter the license of the driver:\n')
    Plate = input('Enter the plate of the car:\n')



    for i in range(len(Hash_Data)):
        if Hash_Data[i] is not None and Hash_Data[i].license == license:
            DateFine = str(datetime.datetime.now().date())
            Finelevel = input('Enter the fine level: 1-Low(-10) 2-Medium(-20) 3-High(-30)\n')
            if Finelevel == '1':
                Hash_Data[i].negative += 10
                Hash_Data[i].BlockDay += 1
                Finelevel = 'Low'
            elif Finelevel == '2':
                Hash_Data[i].negative += 20
                Hash_Data[i].BlockDay += 2
                Finelevel = 'Medium'
            elif Finelevel == '3':
                Hash_Data[i].negative += 30
                Hash_Data[i].BlockDay += 3
                Finelevel = 'High'
            else:
                print("Invalid fine level.")
                return
            SaveNegative()
            Description = input('Enter the fine description:\n')
            trackingnumber = track()

            if Hash_Data[i].negative >= 500:
                Hash_Data[i].StatusDriver = False
                print('You have been blocked due to excessive negative points.')

            new_Fine = Fine(license, DateFine, Finelevel, Description, trackingnumber, Plate)
            HashFine.insert(trackingnumber, new_Fine)
            Hash_Data[i].Finehistory.insert(new_Fine)
            break  

    if not new_Fine:
        print("Driver with this license not found.")
        return

    key, Citycode = Plate.split('-')
    key = key[0:2] + str(ord(key[2])) + key[3:]
    print(key)

    for i in range(len(City_Array)):
        if City_Array[i].Citycode == Citycode:
            plate_search_result = City_Array[i].PBST.search(int(key))
            if plate_search_result:
                plate_search_result.Finehistory.insert(new_Fine)
                SaveFine()
                break
            else:
                print(f"Plate '{Plate}' not found in city records.")
                return

    print(f'Fine created successfully with tracking number: {trackingnumber}')



                
def track():
    status = False
    while status == False:
            number = str(random.randint(100000, 999999))
            if HashFine.search(number):
                status = False
            else:
                status = True
    return number

def SeeFine():
    for i in range(len(HashFine)):
        if HashFine[i] != None:
            print(HashFine[i])
class NodeN:
    def __init__(self,Nagative,National):
        self.Nagative = Nagative
        self.National = National
def Seenagative():
    ll = Linklist()
    neg = int(input('enter the range:\n'))
    for i in range(len(Hash_Data)):
        if Hash_Data[i] != None and Hash_Data[i].license and Hash_Data[i].negative >= neg:
            new = NodeN(Hash_Data[i].negative,Hash_Data[i].National)
            ll.insert(new)
    temp = ll.head
Seenagative()