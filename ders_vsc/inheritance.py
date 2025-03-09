
class Vehicle():
    def __init__(self,model):
        self.model=model
    def start(self):
         print("araç başlatılıyor.")

class Car(Vehicle):
  def start(self): #method overriding-->Polymorphism
      print(f"{self.model} araba başlatiliyor.")

class Truck(Vehicle):
    def load(self):
        print("yük yükleniyor.")

truck=Truck("Scania")
truck.start()
truck.load()

car=Car("Hyundai")
car.start()
