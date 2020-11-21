import random


class Spanzuratoarea:

    def __init__(self, word):
        self.choice = 7
        self.word = word
        self.copie = ''
        self.incercari_gresite = 0
        self.progresul_cautarii = list('_') * len(self.word)
        self.lista_de_litere = []

    def first_and_last_letter(self):
        self.first_last_letter =''
        self.first_and_last_first = list(self.word)
        self.lista_speciala = self.progresul_cautarii
        self.lista_speciala[0] = self.first_and_last_first[0].lower()
        self.lista_speciala[-1] = self.first_and_last_first[-1]

    def tabela_joc(self, cond):
        if cond== 6:
            print(" ---------- \n |     6  | \n | \n | \n | \n | \n | _____________ ")
        elif cond == 5:
            print(" ---------- \n |   5    | \n |        O  \n | \n | \n | \n | _____________ ")
        elif cond == 4:
            print(" ---------- \n |   4    | \n |        O  \n |       /  \n | \n | \n | _____________ ")
        elif cond == 3:
            print(" ---------- \n |   3    | \n |        O  \n |       / \   \n | \n | \n | _____________ ")
        elif cond == 2:
            print(" ---------- \n |   2    | \n |        O  \n |       / \   \n |        | \n | \n | _____________ ")
        elif cond == 1:
            print(
                " ---------- \n |   1    | \n |        O  \n |       / \   \n |        | \n |       / \n | _____________ ")
        elif cond == 0:
            print(
                " ---------- \n |        | Sfarsit de joc  \n |        O  \n |       / \   \n |        | \n |       / \ \n | _____________ ")
        elif cond == 7:
            print(" ---------- \n \n | \n | \n | \n | \n | _____________ ")

    def find_index(self, letter):
        """

        :param letter: index that takes where the letter is
        :return: a list of indexes
        """
        return [i for i, char in enumerate(self.word.lower()) if letter == char]

    def input_from_keyboard(self):
        user_input = input("Alege o litera pentru a juca")
        return user_input

    def first_and_last_multiple(self):
        """

        :param letter: prima si ultima litera pusa in 2 lista, parcurs lista cuv si inlocuit in lista de parcurgere
        :return:
        """
        lista_de_indexi_inital = self.find_index(self.lista_speciala[0])
        lista_de_indexi_final = self.find_index(self.lista_speciala[-1])
        for index in lista_de_indexi_inital:
            self.progresul_cautarii[index] = self.lista_speciala[0]

        for index in lista_de_indexi_final:
            self.progresul_cautarii[index] = self.lista_speciala[-1]

        for val in self.lista_speciala:
            self.first_last_letter += val
        print(' '.join(self.first_last_letter))
        return self.progresul_cautarii

    def is_invalid(self, input_):
        """

        :param input_: caracterul introdus de la tastatura
        :return: daca este corect sau nu
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def play_hangman(self):
        self.progresul_cautarii = self.first_and_last_multiple()
        while self.copie != self.word.lower() and self.choice > 0:
            self.copie = ''
            litera = self.input_from_keyboard()
            while self.is_invalid(litera) is True and litera in self.lista_de_litere:
                print("litera gresita")
                litera = self.input_from_keyboard()

            self.lista_de_litere.append(litera)
            lista_de_indexi = self.find_index(litera)
            if lista_de_indexi:
                for index in lista_de_indexi:
                    self.progresul_cautarii[index] = litera
            else:
                self.choice -= 1
            self.tabela_joc(self.choice)

            for i in self.progresul_cautarii:
                self.copie += i
            print(' '.join(self.copie))

        if self.choice > 0 :
            print("Felicitari INVINGATORULE!")
        else:
            print("Ghinion :( . Cuvantul era {}".format(self.word).lower())


def get_cuvinte_in_lista():
    file = open(file='word.txt')
    lines = list(file.readlines())
    poc = []
    for line in lines:
        ana = str(line).replace("\n", '')
        poc.append(ana)
    return poc


word = random.choice(get_cuvinte_in_lista())

obj1 = Spanzuratoarea(word.lower())
obj1.first_and_last_letter()
obj1.play_hangman()
