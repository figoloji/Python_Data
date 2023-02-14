"Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."

a = int(input("1. Sayıyı Giriniz : "))
b = int(input("2. Sayıyı Giriniz : "))

a,b = b,a

print("Girilen Sayılar: \n1.Sayı {} \n2.Sayı {}".format(a,b))