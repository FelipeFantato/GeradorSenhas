#Felipe Fantato

import random


#site = input("digite o nome do site: ")
#login = input("digite seu o nome de login: ")
tamanho = input("qual seria o tamanho da senha?")

def geradorSenha(tamanho):
    
    i = 0
    novaSenha = ""
    
    while(int(tamanho) > i):
        print(i)
        listaMinuscula = 'abcdefghijklmnopqrstuvwxyz'
        listaMaiuscula = listaMinuscula.upper()
        listaNumeros = "0123456789"
        listaCaractere = "!@#$%^&*'~`"
        lista = listaMinuscula + listaMaiuscula + listaNumeros + listaCaractere
        listaMisturada = ''.join(random.sample(lista,len(lista)))
        #print(listaMisturada)
        caractere = random.choices(listaMisturada)
        novaSenha = novaSenha + ''.join(caractere)
        
        i = i+1   
        
    return novaSenha

print(geradorSenha(tamanho))