#Jogo de Adivinhação
import random   

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")          
print("*********************************")

numero_secreto = random.randrange(1, 101)
numero_de_tentativas = 0
nivel = int(input("Escolha o nível de dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): "))
pontos = 1000


if nivel == 1:
    numero_de_tentativas = 10
elif nivel == 2:
    numero_de_tentativas = 5
elif nivel == 3:
    numero_de_tentativas = 3

print("Pontos: {}".format(pontos))
print("Você tem {} tentativas.".format(numero_de_tentativas))
print("*********************************")

while True and numero_de_tentativas > 0:

    chute = int(input("Digite um número entre 1 e 100: "))
    numero_de_tentativas -= 1

    print("Tentativas restante: {}".format(numero_de_tentativas ))

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue
    elif chute == numero_secreto:
        print ("Parabéns! Você acertou o número secreto! {}.".format(numero_secreto))
        if nivel == 1:
            pontos += 100
        elif nivel == 2:
            pontos += 400
        elif nivel == 3:
            pontos += 700

        print("Pontos: {}".format(pontos))
        continuar = input("Deseja continuar jogando? (s/n): ")
        if continuar.lower() == 's':
            numero_secreto = random.randrange(1, 101)
            if nivel == 1:
                numero_de_tentativas = 10
            elif nivel == 2:
                numero_de_tentativas = 5
            elif nivel == 3:
                numero_de_tentativas = 3
            print("Novo número secreto gerado! Você tem {} tentativas.".format(numero_de_tentativas))
            print("*********************************")
            continue
            
        else:
            print("Obrigado por jogar! Seus pontos finais: {}".format(pontos))
        break
    elif numero_de_tentativas == 0:
        print("Suas tentativas acabaram! O número secreto era {}.".format(numero_secreto))
        pontos -= 400
        print("Pontos: {}".format(pontos))
        continuar = input("Deseja continuar jogando? (s/n): ")
        mudar_nivel = input("Deseja mudar o nível de dificuldade? (s/n): ")
        if mudar_nivel.lower() == 's':
            nivel = int(input("Escolha o nível de dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): "))
        if continuar.lower() == 's':
            numero_secreto = random.randrange(1, 101)
            if nivel == 1:
                numero_de_tentativas = 10
            elif nivel == 2:
                numero_de_tentativas = 5
            elif nivel == 3:
                numero_de_tentativas = 3
            print("Novo número secreto gerado! Você tem {} tentativas.".format(numero_de_tentativas))
            print("*********************************")
            continue
        print("Pontos: {}".format(pontos))
        break
    else:
        if chute < numero_secreto:
            print("O número secreto é maior que o seu chute.")
        else:
            print("O número secreto é menor que o seu chute.")
    


