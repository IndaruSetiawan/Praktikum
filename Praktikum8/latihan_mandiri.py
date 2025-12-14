print("Silakan masukan 2 bilangan dan 1 operator")

try:
    bilangan1 = int(input("Masukan bilangan pertama :"))
    operator = input("Masukan operator :")
    bilangan2 = int(input("Masukan bilangan kedua :"))
    result = eval(f"{bilangan1} {operator} {bilangan2}")
    print(f"Hasilnya : {bilangan1} {operator} {bilangan2} = {result}")
    
except ValueError:
    print("Input yang anda masukan bukan angka!")
    
except ZeroDivisionError:
    print("Input salah! Angka tidak boleh nol.")
    
except Exception as e:
    print(f"Terjadi eror yang tidak diketahui: {e}")
    