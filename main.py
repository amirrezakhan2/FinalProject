from Menu.Signup import SignUp
from Menu.Login import login
from Menu.MakeUserPlate import MakePlate_User
from Menu.UserSeeCar import SeeCar
from Menu.UserSeePlate import SeePlate

while True:
            print(f'{1}...........SignUp...........')
            print(f'{2}............Login...........')
            User_chioce = input('What do you want to do?:\n ')
            if not User_chioce:
                raise  ValueError('Input cannot be empty.')
            if User_chioce == '1':
                status,Data = SignUp()
            elif User_chioce == '2':
                    status,Data = login()
                    print(f'welcome Back {Data.Name} ')
 
            if status == True:        
                    while True:
                        print(f'{1}............Make Plate...............')
                        print(f'{2}.............see All Car ............')
                        print(f'{3}...............see Plate...............')
                        User_work = input(f'What do you want to do? {Data.Name}:\n ')
                        if not User_work:
                            print('Error: Input cannot be empty.')
                            continue
                        if User_work == "1" :
                            User_City = input('which city are you:\n')
                            plate = MakePlate_User(User_City,Data.National)
                            if plate :
                                print(plate)
                            else:
                                print('City name dose not exist')
                        elif User_work =="2":
                            SeeCar(Data.National)
                        elif User_work == "3":
                             SeePlate(Data.National)
                        else:
                            print('Invalid option. Please choose 1 or 2.')
            else:
                print('Invalid option.')


                






                




