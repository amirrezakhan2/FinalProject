class Fine:
    def __init__(self,DriverId,DateFine,Finelevel,Description,trackingnumber,Plate):
        self.DateFine = DateFine
        self.Finelevel = Finelevel
        self.Description = Description
        self.trackingnumber = trackingnumber
        self.DriverId = DriverId
        self.key = int(trackingnumber)
        self.Plate = Plate
    def __repr__(self):
        return f'{self.DateFine} | {self.Finelevel} | {self.Description}  | {self.Plate}  | {self.DriverId}'


    