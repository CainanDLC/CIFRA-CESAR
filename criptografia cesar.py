import random

caracteres = "abcdefghijklmnopqrstuvwxyz"
tamanho_caracteres = len(caracteres)

chave = random.randint(3,10)


def criptografar(mensagem):
    mensagem_criptografada = "" #Inicia a string para obter a mensagem criptografada
    for letra in mensagem: #percorre todas as letras da string enviada
        if letra in caracteres: #se a letra digitada na mensagem estiver presente na string "caracteres", vai para a condição abaixo
            posicao = caracteres.index(letra) #Pega a posicao da letra na string "caracteres"
            letra_nova = caracteres[(posicao + chave) % tamanho_caracteres]  #Soma o valor da posicao atual da letra com o valor da chave e limita o numero da soma ao tamanho da string caracteres
            mensagem_criptografada += letra_nova #adiciona a letra nova a mensagem criptografada
        else:
            mensagem_criptografada += letra #caso a letra digitada não esteja presente na string "caracteres", adiciona a letra sem criptografa-la a mensagem.

    return mensagem_criptografada

def descriptografar(mensagem):
    mensagem_final = ""
    for letra in mensagem:
        if letra in caracteres:
            posicao = caracteres.index(letra)
            letra_nova = caracteres[(posicao - chave) % tamanho_caracteres] #a única diferença dessa função é que ela diminui o valor da chave ao invés de somar
            mensagem_final += letra_nova

        else:
            mensagem_final += letra

    return mensagem_final

nome = input("Digite o nome que deseja criptografar: ")
mensagem_secreta = criptografar(nome)
mensagem_final = descriptografar(mensagem_secreta)

print("Mensagem Criptografada: ", mensagem_secreta)
print("Mensagem Descriptografada: ", mensagem_final)
print("A chave da criptografia era: ", chave)





