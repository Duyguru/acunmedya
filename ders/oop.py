#object oriented programing
#nesneler class ile oluşturulur
class A():
    pass #fonksiyonu boş bırakabilmeyi sağlar

class Car():
    model="Toyota"
    
    def __init__(self,model):
        self.model=model
        print("yeni car uretildi")

    def start(self):#self -> class ın kendisi yazmazsak hata verir

        print(f"{self.model} araba başlatılıyor")

    def increase_speed(self,amount):
        print(f"hız su kadar arttiriliyor: {amount}")

car=Car("Audi") #instance
#car.model="Audi"
car.start()   
car.increase_speed(50)

car1=Car("Honda") # ilgili classın yapıcı methodunu çağırır (constructor)
#car1.model="Honda"    
car1.start()