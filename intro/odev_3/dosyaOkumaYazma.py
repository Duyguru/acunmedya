dosya = open("metinDosyasi.txt", "w") # "w" modu - Mevcut içeriği siler
metin=input("txt. dosyasına dönüştürmek istediğiniz metni giriniz:")
dosya.write(metin)
dosya.close()

dosya=open("metinDosyasi.txt","r")
oku=dosya.read()
print(oku)
dosya.close()

dosya1 = open("metinDosyasi1.txt", "a") # "a" modu - İçeriğin sonuna ekler
for i in range (5):
       
        metin1=input("txt. dosyasına dönüştürmek istediğiniz metni giriniz:")
        dosya1.write(metin1+'\n')
dosya1.close()
                     
dosya1=open("metinDosyasi1.txt","r")
oku1=dosya1.read()
print(oku1)
dosya1.close()