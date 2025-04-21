def sum(*args):
 result=0
 for number in args:
  result += number
 return result

print(sum(5,6))
print(sum(8,9,23))

topla = lambda a,b:a+b
print(topla(7,9))


"""
*args:sinirsiz sayida parametreli fonksiyon olusturmak icin parametrelerin onune * koyularak kullanilir
sonucumuz tuple olarak doner.

**kwargs: tek yildizdan en onemli farki fonksiyonu cagirirken anahtar deger iliskisiyle cagirabilmek
sonucumuz dictionary olarak doner.

*args ve **kwargs, esnek fonksiyonlar yazmanı sağlar.

Yerleşik fonksiyonları (sum, print vb.) override etmemeye dikkat et!

Lambda fonksiyonlar basit işlemler için idealdir.
"""

def fonksiyon(*args,**kwargs):
  for i in args:
    print(i)

  for k,v in kwargs.items():
    print('anahtar: ',k,'degerimiz: ',v)

fonksiyon(1,2,3,'args', deger = 'kwargs')     