
class Address:
    def __init__(self, Country, Region, City, Street, Build, Flat):
        self.__Country = Country
        self.__Region = Region
        self.__City = City
        self.__Street = Street
        self.__Build = Build
        self.__Flat = Flat
        print('Добавлена новая запись адреса: ' + Country + ', ' + Region + ', г.' + City + ', ул.' + Street + ', д.' + Build + ', кв.' + Flat)

    def ToString(self):
        return( self.Country + ', ' + self.Region + ', г.' + self.City + ', ул.' + self.Street + ', д.' + self.Build + ', кв.' + self.Flat)

    def GetCountry(self):
        return self.Country
    def SetCountry(self, value):
        self.Country = value

print('Напишите страну, регион, город, улицу, дом и номер квартиры, разделяя параметры символом "."')
B = input()
B = B.split('.')
try:
    if len(B) != 6:
        raise ValueError('Вы ввели неверное число аргументов, необходимо 6 аргументов')
    A = Address(B[0],B[1],B[2],B[3],B[4],B[5])
except ValueError as err:
    print(err.args)


