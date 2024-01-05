import random

def tambah_saldo():
    saldo = input('Masukkan jumlah saldo ($) : ')
    try:
        with open('data.txt','r') as file:
            jumlah_saldo = int(file.read())
            hasil = jumlah_saldo + int(saldo)
            with open('data.txt','w') as file:
                file.write(str(hasil))
            
    except:
        with open('data.txt','w') as file:
            file.write(saldo)
    return f'\nSaldo sejumlah ${saldo} berhasil ditambahkan!.'

def cek_saldo():
    try:
        with open('data.txt','r') as file:
            read = file.read()
            return f'\nSaldo : ${read}'
    except:
        return '\nSaldo : $0'
    
def main():
    bet = int(input('Masukkan jumlah bet : '))
    try:
        with open('data.txt','r') as file:
            saldo = int(file.read())
            if bet > saldo:
                print('\nMaaf saldo kamu kurang')
            else:
                card = random.randint(1,10)
                card2 = random.randint(1,10)
                
                print(f'\nCard : {card}')
                choice = input('Will the next card be higher or lower? Enter "h" for higher or "l" for lower: ')
                if choice == 'h' and card2 < card or choice == 'l' and card2 > card:
                    with open('data.txt','w') as file :
                        result = saldo - bet
                        file.write(str(result))
                    print('\nLOSE!!! Too bad')
                    print(f'You lose ${bet}')
                else:
                    with open('data.txt','w') as file :
                        result = saldo + bet
                        file.write(str(result))
                    print('\nWIN!!! Congratulations')
                    print(f'You win ${bet}')
    except:
        print('\nMaaf saldo kamu kurang')