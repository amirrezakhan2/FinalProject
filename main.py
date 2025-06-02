from Menu.Signup import UserPanel
from Menu.MakeUserPlate import MakePlate_User

print(f'{1}...........SignUp or Login...........')
while True:
    User_chioce = input('What do you want to do?:\n ')
    if User_chioce == '1':
        status,Data = UserPanel()
        if status == True:
            print(f'{1}............Make Plate...............')
            User_work = input('What do you want to do?:\n ')
            if User_work == "1" :
                User_City = input('whcih city are you')
                plate = MakePlate_User(User_City,Data.National)
                if plate :
                    print(plate)
                else:
                    print('City name dose not exist')


                




