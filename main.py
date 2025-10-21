from Menu.Signup import SignUp
from Menu.Login import login
from Menu.UserPanel import MakePlate_User
from Menu.UserPanel import SeeCar
from Menu.UserPanel import SeePlate
from Menu.ManagerPanel import Car_registration,SeeALLCar,SeeALLUser,SeeALLCityPlate,SeeALLCarCity,DateSearch,SeeALLOwnerCity,ChangeUsername,SeeCarHistory,RegisteredDriver,DeleteCar,chnageowner,removelicense,SeeownerCarHistory,BlockingDriver,Drivinglicense,MakeFine
from Menu.UserPanel import User_Seenegative
from Menu.UserPanel import SeeFine,SeeFinePLate
from Menu.UserPanel import History
from Menu.ManagerPanel import SeeFine

status = False

while True:
    print(f'{1}...........SignUp...........')
    print(f'{2}............Login...........')
    print(f'{3}............ManagerPanel......')
    
    User_chioce = input('What do you want to do?:\n ')
    
    if not User_chioce:
        print('Input cannot be empty.')
        continue
    if User_chioce == '0':
        break
    if User_chioce == '1':
        status, Data = SignUp()

    elif User_chioce == '2':
        status, Data = login()
        print(f'Welcome Back {Data.Name}')

    elif User_chioce == '3':
        Username = int(input('Enter the Username:\n'))
        Password = int(input('Enter the Password:\n'))

        if Username == 0000 and Password == 0000:
            while True:
                print('{1}..........Register Car.........')
                print('{2}..........See ALL Car.........')
                print('{3}..........See ALL User.........')
                print('{4}..........See ALL City Plate.........')
                print('{5}..........See ALL Car City.........')
                print('{6}..........See ALL Car Date.........')
                print('{7}..........See ALL Owner City.........')
                print('{8}..........Change Username.........')
                print('{9}..........See Car History.........')
                print('{10}.........See Registered Driver.........')
                print('{11}.........Delete Car.........')
                print('{12}.........change owner plate.........')
                print('{13}.........removelicence.........')
                print('{14}.........See owner car History.........')
                print('{15}.........BlackingDriver.........')
                print('{16}.........GiveDrvinglicense.........')
                print('{17}.........MakeFine.........')
                print('{18}.........SeeFine.........')
                print('{19}.........Back to main menu.........')

                Manger_chioce = input('What do you want sir:\n')

                if Manger_chioce == '1':
                    Car_registration()

                elif Manger_chioce == '2':
                    SeeALLCar()

                elif Manger_chioce == '3':
                    SeeALLUser()

                elif Manger_chioce == '4':
                    SeeALLCityPlate()

                elif Manger_chioce == '5':
                    SeeALLCarCity()

                elif Manger_chioce == '6':
                    DateSearch()

                elif Manger_chioce == '7':
                    SeeALLOwnerCity()

                elif Manger_chioce == '8':
                    new_user = ChangeUsername()
                    if new_user:
                        print('Username changed successfully')
                        Data.National = new_user  
                    else:
                        print('User not found')



                elif Manger_chioce == '9':
                    SeeCarHistory()

                elif Manger_chioce == '10':
                    RegisteredDriver()

                elif Manger_chioce == '11':
                    DeleteCar()

                elif Manger_chioce == '12':
                    chnageowner()
                elif Manger_chioce == '13':
                    removelicense()
                elif Manger_chioce == '14':
                    SeeownerCarHistory()
                elif Manger_chioce == '15':
                    BlockingDriver()
                elif Manger_chioce == '16':
                    Drivinglicense()
                elif Manger_chioce == '17':
                    MakeFine()
                elif Manger_chioce == '18':
                    SeeFine()
                elif Manger_chioce == '19':
                    break 

                else:
                    print('Invalid option.')

            continue  

        else:
            print('Password and Username do not match')
            continue

    if status == True:
        while True:
            print(f'{1}............Make Plate...............')
            print(f'{2}.............See All Car ............')
            print(f'{3}.............See Plate...............')
            print(f'{4}.............See Negative Point......')
            print(f'{5}.............See Fine................')
            print(f'{6}.............See Plate Fine..........')
            print(f'{7}.............See Plate History.......')
            print(f'{8}.............Exit to main menu.......')

            User_work = input(f'What do you want to do? {Data.Name}:\n ')
            
            if not User_work:
                print('Error: Input cannot be empty.')
                continue

            if User_work == "1":
                User_City = input('Which city are you in?\n').capitalize()
                
                Status, plate = MakePlate_User(User_City, Data.National)
                if not Status:
                    print('You cannot make a new plate.')
                else:
                    print(f'Your new plate is {plate}')

            elif User_work == "2":
                SeeCar(Data.National)

            elif User_work == "3":
                SeePlate(Data.National)

            elif User_work == "4":
                User_Seenegative(Data.National)

            elif User_work == "5":
                SeeFine(Data.National)

            elif User_work == "6":
                SeeFinePLate(Data.National)

            elif User_work == "7":
                History(Data.National)

            elif User_work == "8":
                break  

            else:
                print('Invalid option.')

    else:
        print('Invalid option.')





                




