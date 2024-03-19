import random
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

vida = 200
chances = 4
tempo = 60

fibonacci_max = 100
sorteador = fibonacci(random.randint(5, 10))
while sorteador > fibonacci_max:
    sorteador = fibonacci(random.randint(5, 10))
print("---SORTEADOR---")
print("─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄")
print("█░░░█░░░░░░░░░░▄▄░██░█")
print("█░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█")
print("█░░░▀░░░▄▄▄▄▄░░██░▀▀░█")
print("─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀")
print("Vamos ver se você consegue advinhar o número certo?")
time.sleep(2)
print("\nINSTRUÇÕES: Você tem 4 tentativas, caso erre todas é Gamer Over\nVale lembrar que você inicia com 200 de vida, cada vez que errar subtraímos o valor inserido com o número sorteado, caso sua vida acabe é Game Over.")
time.sleep(4)
print("\nAgora que leu as instruções, vamos ao jogo!")
print("\nSorteando um número par de 0 á 100...")
print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("█░██░██░██░██░██░██░██░██░██░░░░░░░░░░█")
print("█░██░██░██░██░██░██░██░██░██░░░░░░░░░░█")
print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
time.sleep(2)
print("\nNúmero sorteado, Desejo Sorte para você!")

time.sleep(2)
print(" ")

while chances > 0 and vida > 0 and tempo > 0:
    print("Você tem {:.0f} segundos!".format(tempo))

    antes = time.time()

    print("VIDAS RESTANTES:", vida)
    print("CHANCES RESTANTES:", chances)
    print(" ")

    num = int(input("Digite um número: "))
    tempo -= (time.time() - antes)

    if tempo <= 0:
        print("OH NÃO, SEU TEMPO ACABOU!")

        break

    if num == sorteador:
        print("")
        chances = 0
        vida = 0
        print("⠀⣴⠉⡙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⣚⡯⠴⢬⣱⡀⠀")
        print("⢰⡇⣷⡌⢲⣄⡑⢢⡀⠀⠀⠀⠀⠀⢠⠾⢋⠔⣨⣴⣿⣷⡌⠇⡇⠀")
        print("⠀⢸⢹⣿⣿⣄⢻⣿⣷⣝⠷⢤⣤⣤⡶⢋⣴⣑⠟⠿⠿⠿⣿⣿⡀⡇")
        print("⠀⢸⢸⣿⡄⢁⣸⣿⣋⣥⣶⣶⣶⣶⣶⣶⣿⣿⣶⣟⡁⠚⣿⣿⡇⡇⠀")
        print("⢀⣠⡤⠤⠾⡘⠋⢀⣘⠋⠉⠉⠉⠉⢭⣭⣭⣭⣍⠉⢩⣭⠉⠉⠂⠙⠛⠃⣇⡀")
        print("⠏⠀⠀⢿⣿⣷⡀⠀⢿⡄⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣆⠀⢿⣇⠀⠀⠀⠀⠀⠀⠈⢱")
        print("⣦⠀⠀⠈⢿⣿⣧⠀⠘⣿⠀⠀⠀⡀⠀⠀⠘⣿⣿⣿⣿⡆⠀⢻⡆⠀⠀⠀⠀⠀⠀⢸")
        print("⢻⡄⠀⠀⠘⠛⠉⠂⠀⠙⠁⠀⣼⣧⠀⠀⠀⠈⠀⠀⠈⠙⠀⠘⠓⠀⠀⠀⠀⠀⢀⡟")
        print("⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣏⠀")
        print("⠀⠀⠛⢶⢰⣶⢢⣤⣤⣄⠲⣶⠖⠀⣙⣀⠀⠀⠀⠤⢤⣀⣀⡀⣀⣠⣾⠟⡌⠀")
        print("⠀⠘⢄⠃⣿⣿⣿⣿⠗⠀⠾⢿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⠸⠟⣡⣤⡳⢦")
        print("⠀⠀⠀⢻⡆⣙⡿⢷⣾⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⡿⠟⢡⣴⣾⣿⣿⣿⣦")
        print("⠀⠀⠀⡼⢁⡟⣫⣶⣍⡙⠛⠛⠛⠛⠛⣽⡖⣉⣠⣶⣶⣌⠛⢿⣿⣿⣿⣿")
        print("⠀⠀⢀⠔⢡⢎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿⣿⣿")
        print("⠀⢠⠖⢁⣴⡿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿")

        print("---PARABÉNS VOCÊ ACERTOU!---")

    elif num != sorteador:
        vida = max(0, vida - abs(sorteador - num))
        chances -= 1
        print("──────▄▀▄─────▄▀▄")
        print("─────▄█░░▀▀▀▀▀░░█▄")
        print("─▄▄──█░░░░░░░░░░░█──▄▄")
        print("█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")
        print("---OPS...PARECE QUE VOCÊ ERROU!---")

if vida <= 0 or chances <= 0:

    print("\n---GAME OVER---!")

