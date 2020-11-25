import datetime


class TodoList:
    def __init__(self):
        self.lista = ['task', 'data', 'persoana', 'categ_task']
        self.lista_task = []
        self.lista_to_do = []
        #  lista folosita la sortare in functie de anumiti param asc/desc
        self.lista_cu_sortare = []
        # lista folosita la sortareade filtrare punctul 3
        self.lista_filtrare_punctul3 = []
        self.taskuri = input('Introdu task-uri ( q pentru iesire )')
        self.lista_task.append(self.taskuri)
        # Adaug task  urile in lista de task uri si verific daca acestea sunt deja in lista de task uri
        while self.taskuri.upper() != 'Q':
            self.taskuri = input('Introdu task uri')
            if self.taskuri.upper() != 'Q':
                if self.taskuri not in self.lista_task:
                    self.lista_task.append(self.taskuri)
                else:
                    print("Task deja exsitent!")
            else:
                print("Ai iesit din adaugare task uri!")

        # introducere pe rand un task de la tastatura
        print("Introduceți cate o activitate/data/responsabil/categorie de taskuri.")
        self.task = input("Introduceti va rog de la tastatura un task")
        self.data = input("Introduceti va rog data si ora in formatul zz.ll.yyyy hh:mm")

        # Verficare data
        try:
            datetime.datetime.strptime(self.data, '%d.%m.%Y %H:%M')
        except ValueError:
            self.data = '02.10.2011 12:11'

        # Adaugarea de responsabil

        self.responsabil = input("Persoana responsabila este:")

        # adugarea unei categorie pentru acea activitate din lista de task uri.
        # facem si verificare aratand utilizatorului optiunile

        self.categorie_task = input("Introduceti va rog o categorie din urmatoare {}".format(self.lista_task))
        if self.categorie_task not in self.lista_task:
            self.categorie_task = input("Introduceti va rog o categorie din urmatoare nu"
                                        " din altele pe care nu le avem {}".format(self.lista_task))

        # Crearea listei de dictionare pentru fiecare iteratie in while
        self.to_do = {
                    'task': self.task, 'data': self.data,
                    'persoana': self.responsabil, 'categ_task': self.categorie_task
        }
        self.lista_to_do.append(self.to_do)
        # adaugarea acelor task uri de un numar infinit
        self.choice = input('Daca vrei sa adaugi din nou activitate/data/responsabil/categorie'
                            ' apasa orice altceva in afara de q ')

        while self.choice.upper() != 'Q':
            self.task = input("Introduceti va rog data de la tastatura un task")
            self.data = input("Introduceti va rog data si ora in formatul zz.ll.yyyy hh:mm")

            # Verficare data
            try:
                self.data = datetime.datetime.strptime(self.data, '%d.%m.%Y %H:%M')
            except ValueError:
                self.data = '03.10.2011 12:11'

            # Adaugarea de responsabil

            self.responsabil = input("Persoana responsabila este:")

            # adugarea unei categorie pentru acea activitate din lista de task uri.
            # facem si verificare aratand utilizatorului optiunile

            self.categorie_task = input("Introduceti va rog o categorie din urmatoare {}".format(self.lista_task))
            if self.categorie_task not in self.lista_task:
                self.categorie_task = input("Introduceti va rog o categorie din urmatoare nu"
                                            " din altele pe care nu le avem {}".format(self.lista_task))
            self.to_do = {
                'task': self.task, 'data': self.data,
                'persoana': self.responsabil, 'categ_task': self.categorie_task
            }
            self.lista_to_do.append(self.to_do)
            self.choice = input(
                'Daca vrei sa adaugi din nou activitate/data/responsabil/categorie apsa orice altceva in afara de q ')

    # sortare in funcitie de task/categ/etc
    def sortare(self, i='task', j=False):
        return sorted(self.lista_to_do, key=lambda x: x[i], reverse=j)

    def metoda1_sortare(self):
        print("""
                Criteriile disponibile de sortare sunt: 
                1. sortare ascendentă task
                2. sortare descendentă task
                3. sortare ascendentă data
                4. sortare descendentă data
                5. sortare ascendentă persoana responsabilă
                6. sortare descendentă persoană responsabilă
                7. sortare ascendentă categorie
                8. sortare descendentă categorie
                
                Alege dintre acestea ;)

        """)
        # argument folosit in functie de ceeea ce vrem sa sortam
        try:
            self.choices = int(input("Alege numere te rog de la 1 la 8 in functie de mai sus"))
            self.lista_cu_sortare = [self.sortare('task', False), self.sortare('task', True),
                                     self.sortare('data', False), self.sortare('data', True),
                                     self.sortare('persoana', False), self.sortare('task', True),
                                     self.sortare(), self.sortare('categ_task', True)]
            if int(self.choices) not in range(len(self.lista_cu_sortare) + 1):
                print("alegere gresita")
            else:
                return self.lista_cu_sortare[int(self.choices) - 1]
        except ValueError:
            print("Ai ales altceva in afara de numere. Revenire la meniul principal")

    def filtrare_date(self):
        print("""
            Alege in functie de ce vrei sa filtrezi:
                    1.Task
                    2.Dată
                    3.Persoană responsabilă
                    4.Categorie

        """)
        try:
            self.filtru_3 = int(input("Aelge un nmar de la 1 la 4"))
            self.string = input("Alege introducerea unui string utilizat pentru filtrarea în lista inițială de date")
            for values in self.lista_to_do:
                for key, value in values.items():
                    if self.lista[self.filtru_3 - 1] == key and self.string in value:
                        self.lista_filtrare_punctul3.append(values)
                    else:
                        pass
            print(self.lista_filtrare_punctul3)
        except ValueError:
            print("vall")

    def adaugare_nou_task(self):
        self.task = input("Introduceti va rog de la tastatura un task")
        self.data = input("Introduceti va rog data si ora in formatul zz.ll.yyyy hh:mm")

        # Verficare data
        try:
            datetime.datetime.strptime(self.data, '%d.%m.%Y %H:%M')
        except ValueError:
            self.data = '02.10.2011 12:11'

        # Adaugarea de responsabil

        self.responsabil = input("Persoana responsabila este:")

        # adugarea unei categorie pentru acea activitate din lista de task uri.
        # facem si verificare aratand utilizatorului optiunile

        self.categorie_task = input("Introduceti va rog o categorie din urmatoare {}".format(self.lista_task))
        if self.categorie_task not in self.lista_task:
            self.categorie_task = input("Introduceti va rog o categorie din urmatoare nu"
                                        " din altele pe care nu le avem {}".format(self.lista_task))

        # Crearea listei de dictionare pentru fiecare iteratie in while
        self.to_do = {
            'task': self.task, 'data': self.data,
            'persoana': self.responsabil, 'categ_task': self.categorie_task
        }
        self.lista_to_do.append(self.to_do)

        return self.lista_to_do

    def editare_detalii_task(self):
        i = 0
        for values in self.lista_to_do:
            print(i, values)
            i += 1
            for key in values.keys():
                print( key)
        print("Ce linie vrei sa editezi? alege numarul liniei respective")
        try:
            self.linie =int(input(" "))
            if self.linie in range(len(self.lista_to_do)):
                print("Ce task vrei sa editezi? alege task ul  respective")
                self.task_ales =input("")
                if self.task_ales in self.lista:
                    self.lista_to_do[self.linie][self.task_ales] = input(" valoarea noua este")
                else:
                    print("nu exista acest atribut")
            else:
                print("linia nu este in acest range")
            print(self.lista_to_do)
        except ValueError:
            print("valoarea gresita")




    def stergere_task(self):

        i = 0
        for values in self.lista_to_do:
            print(i, values)
            i += 1
        print("Ce task vrei sa stergi? alege numarul task ului respectiv")
        try:
            self.stergere = int(input(" "))
            for index, value in enumerate(self.lista_to_do):
                if self.stergere == index:
                    del self.lista_to_do[index]
        except ValueError:
            print("eroare")

        i = 0
        for values in self.lista_to_do:
            print(i, values)
            i += 1
        print("Ai sters acel task ;)")

    def meniu(self):

        print("Bun venit in acest to do list. Urmatoarele submeniuri sunt disponibile ")
        flag = True
        while flag:
            print("""
                        1. Listare date
                        2. Sortare
                        3. Filtrare date
                        4. Adaugare nou task
                        5. Editare detalii task
                        6. Stergere task
            """)
            try:
                self.optiune = int(input(" alege un numar pentru acele optiuni de mai sus"))
                self.lista_meniuri = [self.sortare, self.metoda1_sortare, self.filtrare_date,
                                      self.adaugare_nou_task, self.editare_detalii_task,
                                      self.stergere_task]
                if self.optiune in range(0, 6):
                    self.lista_meniuri[self.optiune - 1]()
                self.alegere = input("vrei sa mai stai in meniu ? Apasa N pentru a nu mai sta"
                                     " orice altceva inseamna ca mai vrei in meniu")
                if self.alegere.upper() == 'N':
                    flag = False
            except ValueError:
                print('Optiune eronata')


obj1 = TodoList()
obj1.meniu()
