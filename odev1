isim="Duygu"
metin="{name}".format(name=isim)
print(metin)
metin2=f"{5+6}"
print(metin2)

""""
append()	Tek bir eleman ekler	lst.append([4,5])	[1, 2, 3, [4, 5]]
extend()	Listedeki elemanları tek tek ekler	lst.extend([4,5])	[1, 2, 3, 4, 5]

"""
class Human:
      #yapıcı blok
    def __init__(self,name):
        self.name= name

    
        print("bir human instance i üretildi")
    def walk(self): #self yazılmazsa (parametresiz) hata vermekte , bazı dillerdeki this
        print(f"{self.name} is walking")

    def talk(self,sentence):
        print(f"{self.name}: {sentence}") #sadece name çalışmaz class içinde bulamaz,  self.name kullandık
    def __str__(self):
        return f"str fonksiyonundan dönen değer: {self.name}"

human1= Human("Defne")
human1.talk("merhaba")
print(human1)
human2 = Human("Elif")
human2.walk()