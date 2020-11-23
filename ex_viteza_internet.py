description = ('Country', [
   '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '
])

dataset = [
   ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
   ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
   ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
   ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
   ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
   ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
   ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
   ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
   ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
   ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
   ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
   ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
   ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
   ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
   ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
   ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
   ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
   ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
   ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
   ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
   ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
   ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
   ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
   ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
   ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
   ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
   ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
   ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
   ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
   ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
   ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
   ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
   ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
   ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
   ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
   ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
   ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
   ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
   ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]


class Metod_afisare:

    def __init__(self):
        _, self.list_year = description
        self.list_country = []
        self.list_values = []
        self.lista_punctul_1 =[]
        self.dictionar_year_coverage1 = self.dictionar_year_coverage2 = []
        self.dictionar_year_coverage_country = self.dict_punctul1 = {}
        self.counter_in_lista = 0
        self.med = 0

    def printare(self):
        for self.value in dataset:
            self.country, self.values = self.value
            self.list_country.append(self.country)
            self.list_values.append(self.values)


        for i in self.list_values:

            self.dictionar_year_coverage1 = []
            for index, self.value in enumerate(i):
                self.list_year[index] = ''.join(self.list_year[index].split())
                self.value = ''.join(self.value.split())
                self.value  = ''.join(x for x in self.value if x.isdigit())
                self.dictionar_year_coverage ={

                                'year' : self.list_year[index],
                                'coverage' : self.value


                    }
                self.dictionar_year_coverage1.append(self.dictionar_year_coverage)
            self.dictionar_year_coverage_country = {
                                self.list_country[self.counter_in_lista]: self.dictionar_year_coverage1

                }
            self.dictionar_year_coverage2.append(self.dictionar_year_coverage_country)
            self.counter_in_lista += 1

    def metoda_punctul_1(self, dataset, choice):
        while choice not in self.list_year:
            choice = input('Alege din lista de ani {}'. format(self.list_year))
        dataset = self.dictionar_year_coverage2
        self.locul = [index for index, valoare in enumerate(self.list_year) if choice == valoare]
        for values in self.dictionar_year_coverage2:
            for key, values in values.items():
                for year in values:
                    if year['year'] == choice:
                        self.viteza_anul_acela = year['coverage']
                self.tupleee = (key, self.viteza_anul_acela)
                self.lista_punctul_1.append(self.tupleee)

        self.dict_punctul1 = {

                        choice : self.lista_punctul_1
        }

        return self.dict_punctul1

    def metoda_punctul2(self, dataset, choice_tara):
        while choice_tara not in self.list_country:
            choice_tara = input('Alege din lista de tari {}'.format(self.list_country))
        dataset = self.dictionar_year_coverage2
        for self.value in dataset:
           for key, values in self.value.items():
                if key == choice_tara:
                    self.dict_punctul2 = {

                        key : values
                    }

        return self.dict_punctul2

    def metoda_punctul3(self,dataset, choice_tara):
        while choice_tara not in self.list_country:
            choice_tara = input('Alege din lista de tari {}'.format(self.list_country))
        dataset = self.dictionar_year_coverage2
        for self.value in dataset:
           for key, values in self.value.items():
                if key == choice_tara:
                    for coverage in values:
                        if coverage['coverage'] == '':
                            self.med += 0
                        else:
                            self.med += int(coverage['coverage'])
        self.med = self.med/len(self.list_year)
        return self.med




def meniu():

    obj1 = Metod_afisare()
    obj1.printare()
    lista_meniu = [obj1.metoda_punctul_1, obj1.metoda_punctul2, obj1.metoda_punctul3]

    print("""
            Bun Venit in acest program!
            Pentru filtrare in functie de year_date apasa 1
            Pentru filtrare get_country_dataset apasa 2
            Pentru filtrarea mediei pe tara apasa 3
            Orice alt raspuns aduce la meniul principal
            
    """)
    flag = True
    while flag:

        try:
            alegere_tip_filtrare = int(input("In functie de ce printezi?"))
            if alegere_tip_filtrare == 1:
                choice = input("alege an ")
                printare = lista_meniu[alegere_tip_filtrare - 1](dataset, choice)
                print(printare)
                meniu_inchidere = input("Vrei sa mai filtrezi? D/N").upper()
                if meniu_inchidere == 'N':
                    flag = False
            elif alegere_tip_filtrare == 2:
                alegere_tara = input("alege tara ")
                printare = lista_meniu[alegere_tip_filtrare - 1](dataset, alegere_tara)
                print(printare)
                meniu_inchidere = input("Vrei sa mai filtrezi? D/N").upper()
                if meniu_inchidere == 'N':
                    flag = False
            elif alegere_tip_filtrare == 3:
                alegere_tara = input("alege tara ")
                printare = lista_meniu[alegere_tip_filtrare - 1](dataset, alegere_tara)
                print(printare)
                meniu_inchidere = input("Vrei sa mai filtrezi? D/N").upper()
                if meniu_inchidere == 'N':
                    flag = False

        except Exception:
            print("Ai ales gresit boss")


    return True


meniu()
# obj1.metoda_punctul3(dataset, alegere_tara)

