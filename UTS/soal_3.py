jumlah_barang = int(input('masukan jumlah barang:'))
total = 0

for x in range(jumlah_barang):
    harga = int(input (f'harga barang ke-{x+1}='))
    total += harga

print(f'total belanjaan : Rp.{total:,}')