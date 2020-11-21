import random
import numpy as np


class Board:

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board_updated_after_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.choices = ['x', '0']
        self.counterPC = 0
        self.counterJuc = 0

    def cine_incepe(self):
        """

        :return:Metoda a clasei ce alege cine v-a incepe si cu ce se va juca.
        De asemena se va returna si un contor ce va defini cine face miscarea urmatoare
        """
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board_updated_after_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.choices = ['x', '0']
        self.jucator = random.choice(range(0, 100))
        self.calculator = random.choice(range(0, 100))
        self.urmatoarea_miscare = 0
        if self.jucator > self.calculator:
            print("Jucatorul incepe")
            self.jucator = input("Alege x sau 0 pentru a incepe")
            while self.jucator not in self.choices:
                self.jucator = input("Alege te rog x sau 0. Acestea sunt variantele")
            if self.jucator == 'x':
                self.calculator = '0'
            else:
                self.calculator = 'x'
            return self.jucator, self.calculator, self.urmatoarea_miscare
        else:
            self.urmatoarea_miscare = 1
            print("Calculatorul incepe")
            self.calculator = random.choice(self.choices)
            if self.calculator == 'x':
                self.jucator = '0'
            else:
                self.jucator = 'x'
            return self.jucator, self.calculator, self.urmatoarea_miscare


    def vrei_sa_mai_joci(self):
            print("Vrei sa mai joci? D/N. Scorul este {} PC - {} Jucator ".format(self.counterPC, self.counterJuc))
            self.alegere = input("").upper()
            if self.alegere == 'D':
                self.cine_incepe()
                self.metoda_de_miscare()
                self.vrei_sa_mai_joci()
            return 0

    def metoda_castigator(self, tabla):
        """"
        Check in linie
        Check in diag principala
        Check in diagonala secundara
        CHekc in coloana
        """
        self.tabla = tabla
        self.tabla_coloana = np.transpose(self.tabla.reshape(3,3))
        for i in self.tabla.reshape(3, 3):
            if i[0] == i[1] == i[2] and i[0] == self.calc:
                print("ai invins {}".format(self.calc))
                self.counterPC += 1
                return True
            elif i[0] == i[1] == i[2] and i[0] == self.juc:
                print("ai invins {}".format(self.juc))
                self.counterJuc += 1
                return True

        for i in self.tabla_coloana:
            if i[0] == i[1] == i[2] and i[0] == self.calc:
                print("ai invins {}".format(self.calc))
                self.counterPC += 1
                return True
            elif i[0] == i[1] == i[2] and i[0] == self.juc:
                print("ai invins {}".format(self.juc))
                self.counterJuc += 1
                return True

        if tabla.reshape(3, 3)[0][0] == tabla.reshape(3, 3)[1][1] == tabla.reshape(3, 3)[2][2]\
                and tabla.reshape(3, 3)[0][0] == self.calc:
            print("ai invins {}".format(self.calc))
            self.counterPC += 1
            return True
        elif tabla.reshape(3, 3)[0][0] == tabla.reshape(3, 3)[1][1] == tabla.reshape(3, 3)[2][2]\
                and tabla.reshape(3, 3)[0][0] == self.juc:
            print("ai invins {}".format(self.juc))
            self.counterJuc += 1
            return True

        if tabla.reshape(3, 3)[0][2] == tabla.reshape(3, 3)[1][1] == tabla.reshape(3, 3)[2][0] and tabla.reshape(3, 3)[0][2] == self.calc:
            print("ai invins {}".format(self.calc))
            self.counterPC += 1
            return True
        elif tabla.reshape(3, 3)[0][2] == tabla.reshape(3, 3)[1][1] == tabla.reshape(3, 3)[2][0] and tabla.reshape(3, 3)[0][2] == self.juc:
            print("ai invins {}".format(self.juc))
            self.counterJuc += 1
            return True


    def metoda_de_miscare(self):

        self.juc, self.calc, self.urm_misc = self.cine_incepe()
        if self.urm_misc == 0:
            while self.board_updated_after_move:
                print("Jucatorul trebuie sa aleaga o pozitie libera din urmatoarele {}".format(self.board_updated_after_move))
                try:
                    self.alegere_jucator = int(input("Alege {} in pozitiile libere".format(self.juc)))
                    while self.alegere_jucator not in self.board_updated_after_move:
                        self.alegere_jucator = int(input("Alege {} in pozitiile libere".format(self.juc)))
                    else:
                        self.board[self.alegere_jucator - 1] = self.juc
                        for index, value in enumerate(self.board_updated_after_move):
                            if self.alegere_jucator == value:
                                del self.board_updated_after_move[index]
                        self.board_compus = np.array(self.board)
                        if self.metoda_castigator(self.board_compus):
                            break
                        print("""'Tabela arata dupa miscarea jucatorului 
                              {} """.format(self.board_compus.reshape(3, 3)))
                        if self.board_updated_after_move:
                            self.alegere_calc = random.choice(self.board_updated_after_move)
                            self.board[self.alegere_calc - 1] = self.calc
                            self.board_compus = np.array(self.board)
                            for index, value in enumerate(self.board_updated_after_move):
                                if self.alegere_calc == value:
                                    del self.board_updated_after_move[index]
                            print(self.board_updated_after_move)
                            print("""'Tabela arata dupa miscarea calculatorului 
                                                  {} """.format(self.board_compus.reshape(3, 3)))
                            if self.metoda_castigator(self.board_compus):
                                break
                except Exception:
                    print("ai Ales ceva gresit")

            return self.board_compus.reshape(3, 3)

        else:
            while self.board_updated_after_move:
                try:
                    self.alegere_calc = random.choice(self.board_updated_after_move)
                    for index, value in enumerate(self.board_updated_after_move):
                        if self.alegere_calc == value:
                            del self.board_updated_after_move[index]
                    self.board[self.alegere_calc - 1] = self.calc
                    self.board_compus = np.array(self.board)
                    print("""'Tabela arata dupa miscarea calculatorului  {} """.format(self.board_compus.reshape(3, 3)))
                    if self.metoda_castigator(self.board_compus):
                        break
                    if self.board_updated_after_move:
                        print("Jucatorul trebuie sa aleaga o pozitie libera din urmatoarele {}".format(
                                self.board_updated_after_move))
                        self.alegere_jucator = int(input("Alege {} in pozitiile libere".format(self.juc)))
                        while self.alegere_jucator not in self.board_updated_after_move:
                            self.alegere_jucator = int(input("Alege {} in pozitiile libere".format(self.juc)))
                        else:
                            self.board[self.alegere_jucator - 1] = self.juc
                            for index, value in enumerate(self.board_updated_after_move):
                                if self.alegere_jucator == value:
                                    del self.board_updated_after_move[index]
                            self.board_compus = np.array(self.board)
                            print("""'Tabela arata dupa miscarea jucatorului 
                                                         {} """.format(self.board_compus.reshape(3, 3)))
                            if self.metoda_castigator(self.board_compus):
                                break
                except Exception:
                    print("Ai ales ceva anormal, logic, ai pierdut. Joc terminat")
                    self.counterPC += 1
                    break
            return self.board_compus.reshape(3, 3)


obj1 = Board()
obj1.metoda_de_miscare()
obj1.vrei_sa_mai_joci()