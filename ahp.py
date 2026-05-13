# ==========================================
# PROGRAM AHP (Analytical Hierarchy Process)
# Sistem Penunjang Keputusan Pemilihan Siswa Terbaik
# ==========================================

# Nama kriteria
kriteria = ["Akademik", "Disiplin", "Keaktifan"]

# Matriks perbandingan berpasangan
matriks = [
    [1,   3,   5],
    [1/3, 1,   2],
    [1/5, 1/2, 1]
]

# Data alternatif
alternatif = {
    "Andi": [85, 90, 80],
    "Budi": [90, 85, 75],
    "Citra": [88, 92, 85]
}

# Fungsi menampilkan matriks
def tampil_matriks(data, judul):
    print("\n" + "=" * 50)
    print(judul)
    print("=" * 50)
    for baris in data:
        for nilai in baris:
            print(f"{nilai:10.3f}", end=" ")
        print()

# Langkah 1: Tampilkan matriks awal
tampil_matriks(matriks, "1. Matriks Perbandingan Kriteria")

# Langkah 2: Jumlah setiap kolom
jumlah_kolom = []
for j in range(len(matriks[0])):
    total = 0
    for i in range(len(matriks)):
        total += matriks[i][j]
    jumlah_kolom.append(total)

print("\n2. Jumlah Tiap Kolom")
for i in range(len(kriteria)):
    print(f"{kriteria[i]} : {jumlah_kolom[i]:.3f}")

# Langkah 3: Normalisasi matriks
normalisasi = []
for i in range(len(matriks)):
    baris = []
    for j in range(len(matriks[i])):
        baris.append(matriks[i][j] / jumlah_kolom[j])
    normalisasi.append(baris)

tampil_matriks(normalisasi, "3. Matriks Normalisasi")

# Langkah 4: Hitung bobot prioritas
bobot = []
for baris in normalisasi:
    rata = sum(baris) / len(baris)
    bobot.append(rata)

print("\n4. Bobot Prioritas")
for i in range(len(kriteria)):
    print(f"{kriteria[i]:10} = {bobot[i]:.3f}")

# Langkah 5: Hitung skor alternatif
print("\n" + "=" * 50)
print("5. Perhitungan Nilai Alternatif")
print("=" * 50)

hasil = {}
for nama, nilai in alternatif.items():
    skor = 0
    print(f"\nNama Siswa : {nama}")
    print("-" * 40)
    for i in range(len(kriteria)):
        nilai_bobot = nilai[i] * bobot[i]
        skor += nilai_bobot
        print(f"{kriteria[i]:10}: {nilai[i]} x {bobot[i]:.3f} = {nilai_bobot:.2f}")
    hasil[nama] = skor
    print(f"Total Skor : {skor:.2f}")

# Langkah 6: Ranking
ranking = sorted(hasil.items(), key=lambda x: x[1], reverse=True)

print("\n" + "=" * 50)
print("6. Hasil Ranking")
print("=" * 50)

for i, (nama, skor) in enumerate(ranking, start=1):
    print(f"{i}. {nama:10} = {skor:.2f}")

print("\nKesimpulan:")
print(f"Siswa terbaik adalah {ranking[0][0]} dengan nilai {ranking[0][1]:.2f}")