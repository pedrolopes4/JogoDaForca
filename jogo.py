# jogo da força
# declara a palavra
palavra = ("pistache")
palavracen = ("_") * len(palavra)
palavratraço = ("-" * len(palavra))
for i in range(len(palavra)):
    print("_", end="-")

# menu do jogo

print("tente adivinhar a palavra!")
chances = int(input("quantas chances você quer ter?"))
print("você tem ", (chances), "chances!")

# sistema do jogo
erro = 0 # Contador de erros.

# Declarando quebras.
quebra0 = True
quebra1 = True
quebra2 = True
quebra3 = True
quebra4 = True
quebra5 = True
quebra6 = True
quebra7 = True

while erro <= (chances): # enquanto não chega na quantidade de erros, repetir o código.

    letra = str(input("Tente adivinhar uma letra!")) # obtém a letra que o usuário quer adivinhar.
    
    while quebra0 == True:
        while quebra0 == True: # reconhecimento de letra.
            if letra != palavra[0]:
                print("Você escolheu uma letra incorreta!") 
                quebra1 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra0 = False

        while quebra1 == True:
            if letra != palavra[1]: 
                print("Você escolheu uma letra incorreta!")
                quebra1 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra1 = False

        while quebra2 == True:
            if letra != palavra[2]: 
                print("Você escolheu uma letra incorreta!")
                quebra2 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra2 = False

        while quebra3 == True:
            if letra != palavra[3]: 
                print("Você escolheu uma letra incorreta!")
                quebra3 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra3 = False

        while quebra4 == True:
            if letra != palavra[4]: 
                print("Você escolheu uma letra incorreta!")
                quebra4 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra4 = False
        
        while quebra5 == True:
            if letra != palavra[5]: 
                print("Você escolheu uma letra incorreta!")
                quebra5 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra5 = False

        while quebra6 == True:
            if letra != palavra[6]: 
                print("Você escolheu uma letra incorreta!")
                quebra6 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra6 = False

        while quebra7 == True:
            if letra != palavra[7]: 
                print("Você escolheu uma letra incorreta!")
                quebra7 = False
            else:
                print("Você escolheu uma letra correta!")
                quebra = False
                quebra7 = False

        break # encerra o escaneamento/reconhecimento.

    # troca a letra escolhida pela letra da palavra

    if letra == palavra[0]:
        palavra.replace(letra, palavracen[0])

    elif letra == palavra[1]:
        palavra.replace(letra, palavracen[1])
        
    elif letra == palavra[2]:
        palavra.replace(letra, palavracen[2])

    elif letra == palavra[3]:
        palavra.replace(letra, palavracen[3])

    elif letra == palavra[4]:
        palavra.replace(letra, palavracen[4])

    elif letra == palavra[5]:
        palavra.replace(letra, palavracen[5])

    elif letra == palavra[6]:
        palavra.replace(letra, palavracen[6])

    elif letra == palavra[7]:
        palavra.replace(letra, palavracen[7])

    print(palavracen, ".")
    erro = erro + 1 # adiciona 1 no contador de erros, para quando chegar na quantidade de chances, encerrar o código.

print("acabou suas chances!")