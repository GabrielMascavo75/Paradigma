import random
from abc import ABC, abstractmethod

# Classe abstrata (base)
class Jogo(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass


# Classe Jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

# Classe principal do jogo
class JogoAdivinhacao(Jogo):
    def __init__(self, jogador: Jogador, dificuldade):
        self.jogador = jogador
        self.__tentativas = 0

        # Define dificuldade
        if dificuldade == 1:
            self.__limite = 15
            self.max_num = 50
        elif dificuldade == 2:
            self.__limite = 10
            self.max_num = 100
        else:
            self.__limite = 5
            self.max_num = 200

        self.numero_secreto = random.randint(1, self.max_num)

        # Ranking de níveis
        self.niveis_criatura = {
            1: "Deus",
            2: "Anjo",
            3: "Mago",
            4: "Guerreiro",
            5: "Arqueiro"
        }

    def iniciar(self):
        print(f"\nBem-vindo(a), {self.jogador.nome}!")
        print("Jogo de Adivinhação")
        print(f"Adivinhe um número entre 1 e {self.max_num}")
        print(f"Você tem {self.__limite} tentativas\n")

    def jogar(self):
        while self.__tentativas < self.__limite:
            try:
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("Digite apenas números!")
                continue

            self.__tentativas += 1

            if palpite == self.numero_secreto:
                print("\n Você acertou!")
                print("Tentativas usadas:", self.__tentativas)

                # Calcula pontuação
                pontos = (self.__limite - self.__tentativas + 1) * 10
                self.jogador.pontuacao += pontos

                print(f"Você ganhou {pontos} pontos!")

                nivel = self.niveis_criatura.get(self.__tentativas, "Novato")
                print(f"Seu nível: {nivel}")

                return

            elif palpite < self.numero_secreto:
                print("Tente um número MAIOR.")
            else:
                print("Tente um número MENOR.")

        print("\n Fim de jogo!")
        print("O número era:", self.numero_secreto)

        # Penalidade
        self.jogador.pontuacao -= self.__limite * 5
        print("Você perdeu pontos!")


# Lista global de ranking
ranking = []


def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    while True:
        try:
            op = int(input("Opção: "))
            if op in [1, 2, 3]:
                return op
            else:
                print("Escolha válida: 1, 2 ou 3")
        except ValueError:
            print("Digite um número válido!")


def mostrar_ranking():
    print("\n RANKING ")

    # Ordena por pontuação (maior para menor)
    ranking_ordenado = sorted(ranking, key=lambda j: j.pontuacao, reverse=True)

    for i, jogador in enumerate(ranking_ordenado, start=1):
        print(f"{i}º - {jogador.nome}: {jogador.pontuacao} pontos")


def executar_jogo():
    nome = input("Digite seu nome: ")
    jogador = Jogador(nome)

    dificuldade = escolher_dificuldade()

    jogo = JogoAdivinhacao(jogador, dificuldade)
    jogo.iniciar()
    jogo.jogar()

    # Adiciona ao ranking
    ranking.append(jogador)

    mostrar_ranking()


# Executa o jogo
executar_jogo()

'''Foi implementado um sistema de dificuldade que altera o número de tentativas e o intervalo do número secreto, tornando o jogo mais dinâmico.
Além disso, foi criado um ranking de jogadores que armazena as pontuações e exibe os melhores resultados em ordem decrescente.
O código também foi organizado e comentado para facilitar o entendimento.'''
