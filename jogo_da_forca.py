from random import choice


with open("palavras.txt") as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split("\n")

palavra = choice(lista_de_palavras).upper()

acertos = erros = 0
letras_acertadas = ''
letras_erradas = ''


forca = """
____
    |
    |
    -"""

vazio = """
"""

cabeca = """
    O
"""

tronco = """
    O
    |
"""

braco_esquerdo = """
    O
   /|
"""

braco_direito = """
    O
   /|\\
"""

perna_esquerda = """
    O
   /|\\
   /
"""

perna_direita = """
    O
   /|\\
   / \\
"""

corpo_forca = [
    vazio,
    cabeca,
    tronco,
    braco_esquerdo,
    braco_direito,
    perna_esquerda,
    perna_direita,

]


while acertos != len(palavra) and erros != 7:
    print(len(palavra))
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += letra + " "
        else:
            mensagem += '_ '

    print(forca + corpo_forca[erros])
    print(mensagem)

    letra = input("Digite uma letra: ").upper()

    if letra in letras_acertadas+letras_erradas:
        print("Você já digitou essa letra")
        continue

    if letra in palavra:
        letras_acertadas += letra
        acertos += palavra.count(letra)
        print("Você acertou")
    else:
        erros += 1
        letras_erradas += letra
        print("Você errou a letra")

    print("Letras digitadas:",letras_acertadas+letras_erradas)