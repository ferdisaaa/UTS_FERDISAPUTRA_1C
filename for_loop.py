for i in range(0,10,2):
    print(i)
for i in range(1,10,2):
    print(f'perulangan ke -{i}')
# pake variabel
jumlah = 10
for i in range(jumlah):
    print(f'perulangan ke{i}')

# Perulangan unntuk mengecek bilangan ganjil/genap
for i in range(0,15):
    if i % 2 == 0:
        print(f'{i} -bilangan genap')
    else:
        print(f'{i} -bilangan ganjil')

fruits = ['mangga', 'apel','semangka','duren']

for i,buah in enumerate(fruits):
    print(f'buah ke -{i}: {buah}')


biodata = {
    'nama': 'agus',
    'nim' : '24090075',
    'umur': '25',
}

for a,b in biodata.items():
    print(f'{a}: {b}')