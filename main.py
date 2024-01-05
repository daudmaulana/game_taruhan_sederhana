import module
import os

while True:
    os.system('cls')
    print('ROLL THE DICE')
    print('PROGRAM PEMBUATAN GAME')
    print('-'*24)
    print('1. Tambah saldo')
    print('2. Cek saldo')
    print('3. Main')

    pilih = input('Masukkan pilihan : ')

    if pilih == '1':
        print(module.tambah_saldo())
    elif pilih == '2':
        print(module.cek_saldo())
    elif pilih == '3':
        module.main()
        
    done = input('Lagi? (y/n) : ')
    if done == 'n':
        break

print('Akhir dari program')