print("Program Mengubah Huruf Besar Menjadi Huruf Kecil dan Sebaliknya")

kata_awal = input("Masukkan Kata = ")

kata_baru = ""

for kar in kata_awal :
    if kar.isupper() :
        karbaru = kar.lower()
    elif kar.islower() :
        karbaru = kar.upper()
    else :
        karbaru = kar
    kata_baru = kata_baru + karbaru
print("Kalimat Sekarang Menjadi = ", kata_baru)
