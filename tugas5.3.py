# Fungsi untuk menghitung IPS
def hitung_ips(jumlah_matkul, nilai_mk):
    total_sks = 0
    total_nilai = 0

    for i in range(jumlah_matkul):
        # Menentukan SKS berdasarkan nilai
        if nilai_mk[i] == 'A':
            sks = 4
        elif nilai_mk[i] == 'B':
            sks = 3
        elif nilai_mk[i] == 'C':
            sks = 2
        elif nilai_mk[i] == 'D':
            sks = 1
        else:
            print(f"Nilai '{nilai_mk[i]}' tidak valid. Gunakan A, B, C, atau D.")
            sks = 0  # Jika nilai tidak valid, set sks menjadi 0

        total_sks += sks
        total_nilai += sks  # Menghitung total nilai untuk IPS

    # Menghitung IPS
    ips = total_nilai / total_sks if total_sks > 0 else 0
    return ips

# Input jumlah mata kuliah
jumlah_mata_kuliah = int(input("Berapa jumlah mata kuliah? "))

# Input nilai untuk setiap mata kuliah
nilai_mata_kuliah = []
for i in range(jumlah_mata_kuliah):
    nilai = input(f"Nilai mata kuliah ke-{i + 1} (A/B/C/D): ").upper()
    nilai_mata_kuliah.append(nilai)

# Menghitung IPS
ips_hasil = hitung_ips(jumlah_mata_kuliah, nilai_mata_kuliah)

# Output hasil IPS
print(f"Nilai IPS anda semester ini {ips_hasil:.2f}")