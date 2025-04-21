def hesap_makinesi(sayi1, sayi2, islem):
    if islem not in ['+', '-', '*', '/']: 
        return "Geçersiz işlem türü!"
    
    if islem == '/' and sayi2 == 0: 
        return "Bölme işlemi için ikinci sayı 0 olamaz!"

    match islem:
        case '+':
            return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
        case '-':
            return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
        case '*':
            return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
        case '/':
            return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"


sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
islem = input("Yapmak istediğiniz işlemi giriniz (+, -, *, /): ")


print(hesap_makinesi(sayi1, sayi2, islem))