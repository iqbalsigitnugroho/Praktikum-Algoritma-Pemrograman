print("""
==============================================
                Iqsin Smartphone Store
            Daftar Handphone Yang Tersedia
               Jl. Pendidikan II No. 17
                  Tambun - Kab.Bekasi
==============================================
1. Realme                   : Rp. 6.000.000
2. Samsung                  : Rp. 4.000.000
3. Xiaomi                   : Rp. 3.000.000
4. Infinix                  : Rp. 1.500.000
==============================================""")
nama=input("Nama Pembeli                : ")
pesan=str(input("Nama Produk                 : "))
jumlahpesanan=int(input("Jumlah Unit                 : "))
if pesan == "Realme":
    harga=(6000000*jumlahpesanan)
elif pesan == "Samsung":
    harga=(4000000*jumlahpesanan)
elif pesan == "Xiaomi":
    harga=(3000000*jumlahpesanan)
elif pesan == "Infinix":
    harga=(1500000*jumlahpesanan)
else:
    pesan="-"
    harga="-"
    pilihan=input("Menu Tidak Tersedia, silahkan ulangi kembali Y/N")
ppn = 15000+harga
print("------------------------------------------------")
print("Harga Satuan                : Rp. {}".format (harga))
print("PPN                         : Rp.   15000")
print("Total                       : Rp. {}".format (ppn))
print("------------------------------------------------")
print("     Semua Smartphone Memiliki Garansi Resmi")
print("""        Jika Ada Masalah Silahkan Hubungi
                Telp. 0813-1895-9634
            Email : iqsinphone@gmail.com
===================TERIMA KASIH===================
""")