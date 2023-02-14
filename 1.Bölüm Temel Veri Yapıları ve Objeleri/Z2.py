"Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun"
"Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)"

boy = float(input("Boyunuzu Giriniz : "))
kilo = int(input("Kilonuzu Giriniz : "))

bke = kilo / (boy**2)

print("Beden Kitle Endeksiniz : ", bke)

