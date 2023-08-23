lista_do_jogo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


print("Nesse programa iremos sortear indices da lista e trocaremos por 0")
print("Abaixo estara a lista como está normalmente, os números sorteados e")
print("a lista com os indices trocados. (Caso caia nas casas A você voltara do começo)")
print(lista_do_jogo)
print("")


n = 0
while n != 5:
    from random import randint
    random = randint(0, 39)
    print(random)
    lista_do_jogo.pop(random)
    lista_do_jogo.insert(random, 'A')
    n += 1
print("")
print("Você está na casa de número 1, chegue o mais longe possivel")
print("para vencer!")
print("||", lista_do_jogo, "||")
print("")

k = 0
position = 1
while k != 5:
    from random import randint
    dado = randint(1, 6)
    position += dado
    k += 1
    print("Rodada {}".format(k))
    print("você está na {} casa e tirou {} nos dados".format(position, dado))
    print ("")
    if lista_do_jogo[position] == 0:
        print("|| Você deu azar, volte até o começo ||")
        position -= position
    if lista_do_jogo[position] == 40:
        print("|| Você Ganhou o jogo, Parabéns ||")
        break

if k == 5 and lista_do_jogo[position] == 0:
    print("")
    print("|| Putz, que azar hein! Você parou de onde saiu! ||")

lista_do_jogo.pop(position)
lista_do_jogo.insert(position, "|P|")
print ("")
print("")
print("Abaixo está sua posição final")
print(lista_do_jogo)
