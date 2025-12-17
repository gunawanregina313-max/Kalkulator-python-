def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Error: Pembagian tidak bisa dibagi nol"
    return a / b

print("---! Kalkulator Sederhana !---")

while True:
    print("\nPilih Operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Anda keluar dari kalkulator.")
        break

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            hasil = penjumlahan(angka1, angka2)
            print(f"Hasil penjumlahan = {hasil}")
        elif pilihan == '2':
            hasil = pengurangan(angka1, angka2)
            print(f"Hasil pengurangan = {hasil}")
        elif pilihan == '3':
            hasil = perkalian(angka1, angka2)
            print(f"Hasil perkalian = {hasil}")
        elif pilihan == '4':
            hasil = pembagian(angka1, angka2)
            print(f"Hasil pembagian = {hasil}")
    else:
        print("Anda tidak memasukkan pilihan.")
