print("|| Começa O jogo, Boa Sorte! ||")
chute = 0
contador = 0
vitorias = 0
derrotas = 0
while contador < 3:
    from random import randint
    random = randint(0, 20)
    chute = input("Chute um número de 0 a 20: ")
    if chute.isnumeric():
        chute = int(chute)
        contador += 1
        if chute > 20:
            print("")
            print("Tente Novamente! Lembrando, escolha um número de 0 a 20.")
            print("")
            contador = contador - 1
        else:
            if chute == random:
                print("")
                print("Parabéns, você chutou {} e acertou!".format(random))
                print("")
                vitorias += 1
            else:
                print("")
                print("Você errou! Mais sorte na proxima! O número era {}.".format(random))
                print("")
                derrotas += 1
    if derrotas == 3:
        print("Levanta a cabeça princesa, se não a coroa cai!")
    if vitorias == 1:
        print("Iti malia, parece que a sorte começou a sorrir pra você!")
    if vitorias == 2:
        print("Eita Giovana! Cê tá que tá, heim?")
    if vitorias == 3:
        print("A serenidade no olhar de quem ganhôooooo!!!")

print("")
print("|| O jogo acabou, volte sempre! ||")