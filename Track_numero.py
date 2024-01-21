import phonenumbers 
from phonenumbers import geocoder #import necessário para pegar o geo code baseado no numero
import os
import platform
from time import sleep  

def limpar(): #função para limpar o terminal
    if platform.system() == 'Windows':
        os.system('cls') 



while True: #comando de repetição
    limpar()
    print('\033[32m-=-=-=-=-=-=-\033[m'.center(80))
    print('\033[1;32mRastreador de número\033[m'.center(80))
    print('\033[32m-=-=-=-=-=-=-\033[m'.center(80))

    print('\033[33m\nExemplo: +55 83 999996665\033[m')

    telefone = phonenumbers.parse(input('\033[1;32m\nDigite um numero aqui: \033[m').replace('-', ''))
    print('\033[1;32m{} está localizado em\033[m \033[1;33m{}\033[m'.format(telefone,geocoder.description_for_number(telefone,'en')))

    esc = input('\033[34m\nDeseja reiniciar o programa ? S/N: \033[m').lower()

    if(esc == 's'):
        print('\033[32mReiniciando\033[m')
        sleep(1)
        limpar()

    elif(esc == 'n'):
        print('\033[31mEncerrado\033[m')
        break
    else:
        print('\033[1;31m\nDigite apenas "s" ou "n"\033[m')
        break
