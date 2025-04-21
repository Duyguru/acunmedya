def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayi degildir."
    
    for i in range(2,sayi):
        if sayi%i==0:
         return f"{sayi} bir asal sayi degildir."
    return f"{sayi} bir asal sayidir." 
sayi=int(input("sayi giriniz: "))
print(asal_mi(sayi))

        
        