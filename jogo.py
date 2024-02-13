import os

import random

import time

import sys
sys.stdout.reconfigure(encoding="utf-8")


class Jogo_da_velha():

    def __init__(self):

        self.placar_jogador = 0

        self.placar_computador = 0

        self.empates = 0



    def limpar_tela(self):

        os.system('cls' if os.name == 'nt' else 'clear')



    def iniciar_jogo(self):

        while True:

            self.limpar_tela()

            print("Escolha 1 para X ou 2 para O (ou digite 'sair' para sair):")

            escolha = input()

            if escolha.lower() == 'sair':

                print("Obrigado por jogar!")

                break

            elif escolha in ['1', '2']:

                jogador_inicial = random.choice(["jogador", "computador"])

                print(f"O jogador inicial é: {jogador_inicial}")

                self.realizar_jogo(int(escolha), jogador_inicial)

            else:

                print("Opção inválida. Por favor, escolha 1 para X ou 2 para O.")



    def realizar_jogo(self, escolha, jogador_inicial):

        jogo = Partida(escolha, jogador_inicial)

        jogo.mostrar_tabela()

        jogo.turnos()



        self.placar_jogador += jogo.placar_jogador

        self.placar_computador += jogo.placar_computador

        self.empates += jogo.empates



        print(f"\nPlacar total: Jogador {self.placar_jogador} - {self.placar_computador} Computador ({self.empates} Empates)")

        input("Pressione Enter para continuar...")



class Partida():

    def __init__(self, escolha, jogador_inicial):

        self.tabela = [' ' for _ in range(9)]

        self.jogador = "X" if escolha == 1 else "O"

        self.computador = "O" if escolha == 1 else "X"

        self.turno_atual = jogador_inicial

        self.placar_jogador = 0

        self.placar_computador = 0

        self.empates = 0



    def mostrar_tabela(self):

        print(f"{self.tabela[0]} | {self.tabela[1]} | {self.tabela[2]}")

        print(f"{self.tabela[3]} | {self.tabela[4]} | {self.tabela[5]}")

        print(f"{self.tabela[6]} | {self.tabela[7]} | {self.tabela[8]}")



    def turnos(self):

        while not self.checar_ganhador() and ' ' in self.tabela:

            if self.turno_atual == "jogador":

                self.turno_jogador()

                self.turno_atual = "computador"

            else:

                self.turno_computador()

                self.turno_atual = "jogador"

            self.mostrar_tabela()

            if self.turno_atual == "computador":

                time.sleep(2)

                jogo.limpar_tela()



        if self.checar_ganhador():

            if self.checar_ganhador() == self.jogador:

                print(f"O jogador '{self.checar_ganhador()}' venceu!")

                self.placar_jogador += 1

            else:

                print("O computador venceu!")

                self.placar_computador += 1

        else:

            print("Empate!")

            self.empates += 1



    def turno_jogador(self):

        print("Sua vez (Digite o número de 1 a 9):")

        movimento = int(input()) - 1

        if self.tabela[movimento] == ' ':

            self.tabela[movimento] = self.jogador

        else:

            print("Posição ocupada. Tente novamente.")

            self.turno_jogador()



    def turno_computador(self):

        movimento = random.choice([i for i, v in enumerate(self.tabela) if v == ' '])

        self.tabela[movimento] = self.computador



    def checar_ganhador(self):

        for i in range(3):

            if self.tabela[i] == self.tabela[i+3] == self.tabela[i+6] != ' ':

                return self.tabela[i]

            if self.tabela[i*3] == self.tabela[i*3+1] == self.tabela[i*3+2] != ' ':

                return self.tabela[i*3]

        if self.tabela[0] == self.tabela[4] == self.tabela[8] != ' ':

            return self.tabela[0]

        if self.tabela[2] == self.tabela[4] == self.tabela[6] != ' ':

            return self.tabela[2]

        return None





jogo = Jogo_da_velha()

jogo.iniciar_jogo()