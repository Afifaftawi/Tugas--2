# Minta input dari pengguna
bilangan = int(input("Masukkan bilangan: "))

# Periksa apakah bilangan tersebut genap atau ganjil
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")
