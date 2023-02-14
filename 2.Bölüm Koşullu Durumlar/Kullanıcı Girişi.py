print("""
*****************
Kullanıcı Girişi
*****************
""")

sys_user = "sinans"
sys_password = "123456"

kullanici_adi = input("Kullanıcı Adı : ")
parola = input("Parola : ")

if ( kullanici_adi == sys_user and parola != sys_password):
    print("Parola Hatalı...")

elif ( kullanici_adi != sys_user and parola == sys_password):
    print("Kullanıcı Adı Hatalı...")

elif ( kullanici_adi != sys_user and parola != sys_password):
    print("Kullanıcı Adı ve Parola Hatalı...")

else:
    print("Sisteme Giriş Başarılı")