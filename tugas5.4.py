def perkalian(a, b):
    return sum(a for _ in range(abs(b))) if b >= 0 else -sum(a for _ in range(abs(b)))

def pemangkatan(base, exp):
    hasil = 1
    for _ in range(abs(exp)):
        hasil = perkalian(hasil, base)
    return hasil if exp >= 0 else 1 / hasil

def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("=== Program Perkalian, Pemangkatan, dan Bilangan Prima ===")
a = int(input("Masukkan bilangan pertama untuk perkalian: "))
b = int(input("Masukkan bilangan kedua untuk perkalian: "))
print(f"{a} * {b} = {perkalian(a, b)}")

base = int(input("Masukkan bilangan dasar untuk pemangkatan: "))
exp = int(input("Masukkan pangkat: "))
print(f"{base} ** {exp} = {pemangkatan(base, exp)}")

n = int(input("Masukkan bilangan untuk memeriksa apakah prima: "))
print(f"{n} {'adalah' if is_prima(n) else 'bukan'} bilangan prima.")