# jogo da força
# declara a palavra
palavra = ("pistache")
palavracen = list("_" * len(palavra))
palavratraço = str("-" * len(palavra))
for i in range(len(palavra)):
    print("_", end="-")

# menu do jogo

print("tente adivinhar a palavra!")
chances = int(input("quantas chances você quer ter?"))
print("você tem ", (chances), "chance(s)!")

# sistema do jogo
erro = 0 # Contador de erros.

while erro < chances:
    letra = input("Tente adivinhar uma letra!").lower() # Recebe a letra e transforma ela em minúscula para reconhecimento.
    if letra in palavra:
        print("A palavra possui essa letra!")
        for idx, char in enumerate(palavra): # Percorre a palavra inteira procurando indíce(1,2,3 etc...) da palavra e char daquele indíce.
            if char == letra: # Se char = letra
                palavracen[idx] = letra # Troca a letra pela char daquela posição.
    else:
        print("A palavra não possui essa letra!")
        erro += 1

    print("".join(palavracen))
    adivinhacao = input("Você já consegue adivinhar a palavra?").lower()
    if adivinhacao == "sim":
        tentativaA = input("Tente adivinhar a palavra!").lower()
        if tentativaA == palavra:
            print("Você acertou a palavra!")
            print("Você ganhou o jogo!")
            chances = 10000
            break
        else:
            print("Você errou a palavra!")
    else:
        print("Ok")

print("acabou suas chances!")