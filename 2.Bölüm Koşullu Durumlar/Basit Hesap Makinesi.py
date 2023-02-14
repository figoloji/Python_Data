print("""
************************
Hesap Makinesi Programı

İşlemler:

1- Toplama
2- Çıkartma
3- Çarpma
4- Bölme

************************
""")

islem = int(input("İşlemi Giriniz : "))
a = int(input("1.Sayı : "))
b = int(input("2.Sayı : "))

if islem == 1:
    print("{} ile {} sayısının toplamı {}'dır.".format(a,b, a+b))

elif islem == 2:
    print("{} ile {} sayısının çıkartması {}'dır.".format(a,b, a-b))

elif islem == 3:
    print("{} ile {} sayısının çarpımı {}'dır.".format(a,b, a*b))

elif islem == 4:
    print("{} ile {} sayısının bölümü {}'dır.".format(a,b, a/b))

else :
    print("Geçersiz İşlem Numarası...")