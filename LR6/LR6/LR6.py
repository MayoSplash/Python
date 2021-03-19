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


A = Address('Россия','Краснодарский край','Краснодар','Ямальская','5','64')
print(A._Address__Flat)

