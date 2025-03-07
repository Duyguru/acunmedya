#object oriented programing
#nesneler class ile oluşturulur
class A():
    pass #fonksiyonu boş bırakabilmeyi sağlar

class Car():
    model="Toyota"
    
    def __init__(self,model):
        self.__model=model
        print("yeni car uretildi")

    def start(self):#self -> class ın kendisi yazmazsak hata verir

        print(f"{self.__model} araba başlatılıyor")

    def increase_speed(self,amount):
        print(f"hız su kadar arttiriliyor: {amount}")

       #getter
    def get_model(self):
     return self.__model

       #setter
    def set_model(self,model):
      if len(model)<3:
        print("marka ismi 3 haneden küçük olamaz.")
        return
      self.__model=model

car=Car("Audi") #instance
#car.model="Audi"  Encapsulation yazma işlemi (set etmek)  önlemek için __ ekledik modele
#print(car.model)  Get etmek -okuma isşemi
car.start()   
car.increase_speed(50)

car1=Car("Honda") # ilgili classın yapıcı methodunu çağırır (constructor)
#car1.model="Honda"    
car1.start()

