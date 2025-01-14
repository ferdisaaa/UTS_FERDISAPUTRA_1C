# tahun = int(input('Masukan Tahun : '))

# satu = (tahun/400)
# dua = (tahun/4/100)



# kabisat = (satu==dua)

# if kabisat==True:
#     print (f'Tahun {tahun} merupakan TAHUN KABISAT')
    
tahun  = int(input('masukkan tahun:'))

rules1 = (tahun/400)
rules2 = (tahun/4/100)

kabisat = rules1==rules2

if kabisat == True:
    print(f'tahun{tahun} ini merupakan tahun kabisat')  