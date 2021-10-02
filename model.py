import random
import time

SIRINA = 7
VISINA = 6

def nova_igra():
    seznam = []
    for i in range(VISINA):
        seznam.append([])
        for j in range(SIRINA):
            seznam[i].append(" ")
    return Polje(seznam)

class Polje:
    def __init__(self, polje):
        self.polje = polje[:]
        self.meti = []
        self.score1 = 0
        self.score2 = 0

    def pravilnost(self, izbira):
        if self.polje[VISINA - 1][izbira] == " ":
            return True
        else: 
            return False

    def dodaj_kovanec_X(self, izbira):
        self.meti.append(izbira)
        if self.pravilnost(izbira) == True:
            for i in range(VISINA):
                if self.polje[i][izbira] == " ":
                    self.polje[i].pop(izbira)
                    self.polje[i].insert(izbira, "X")
                    break

    def dodaj_kovanec_O(self, izbira):
        self.meti.append(izbira)
        if self.pravilnost(izbira) == True:
            for i in range(VISINA):
                if self.polje[i][izbira] == " ":
                    self.polje[i].pop(izbira)
                    self.polje[i].insert(izbira, "O")
                    break

    def get_visina(self, izbira):
        visina = 0
        for i in range(VISINA):
            if self.polje[i][izbira] == " ":
                visina += 1
        return 6 - visina

    def odstrani_kovanec(self, izbira):
        stevilo = 0
        for i in range(VISINA):
            if self.polje[i][izbira] == " ":
                stevilo += 1
        if stevilo != 6:
            self.polje[5 - stevilo].pop(izbira)
            self.polje[5 - stevilo].insert(izbira, " ")

    def seznam_pravilnih(self):
        seznam = []
        for i in range(SIRINA):
            if self.polje[VISINA - 1][i] == " ":
                seznam.append(i)
        return seznam

    def sprintaj(self):
        polje = []
        for i in range(len(self.polje)):
            polje.append("│ " + " │ ".join(str(v) for v in self.polje[i]) + " │")
        polje.insert(0, "│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │")
        polje.insert(1, "=============================")
        novo_polje = []
        for i in range(len(polje)):
            novo_polje.append(polje[-i-1])
        print(*novo_polje, sep = "\n")
    
    def animacija(self, izbira):
        if self.zmaga() == True:
            if self.get_visina(izbira) <= 4:
                time.sleep(1.6)
                self.odstrani_kovanec(izbira)
                for i in range(1, 6 - self.get_visina(izbira)):
                    self.polje[-i][izbira] = "o"
                    print("_____________________________")
                    self.sprintaj()
                    time.sleep(1.1)
                    self.polje[-i][izbira] = " "
                self.dodaj_kovanec_O(izbira)

    def remi(self):
        if self.seznam_pravilnih() == [] and self.zmaga() == False:
            return True
        else:
            return False

    def stevilo_kovancev(self):
        stevilo = 0
        for vrstica in self.polje:
            for element in vrstica:
                if element == "X" or element == "O":
                    stevilo += 1
        return stevilo

    def kdo_je_zmagal(self):
        if self.remi() == True:
            return "Igra je neodločena!"
        if True:
            if self.stevilo_kovancev() % 2 == 1:
                return "Zmagal je Igralec 1 !"
            else:
                return "Zmagal je Igralec 2 !"   

    def kdo_je_zmagal_robot(self):
        if self.stevilo_kovancev() % 2 == 1:
            return "Igralec 1"
        else:
            return "ROBOT"

    def sprazni_polje(self):
        for vrstica in self.polje:
            for i in range(len(vrstica)):
                vrstica.pop(i)
                vrstica.insert(i, " ")
        return self.polje

    def kdo_je_na_vrsti(self):
        if self.stevilo_kovancev() % 2 == 0:
            return "Igralec 1"
        else:
            return "Igralec 2"

    def shiny(self):
        if self.zmaga() == True:
            for i in range(6):
                for j in range(4):
                    if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                        self.polje[i][j] = "o"
                        self.polje[i][j + 1] = "o"
                        self.polje[i][j + 2] = "o"
                        self.polje[i][j + 3] = "o"
                        
            for i in range(3):
                for j in range(7):
                    if (self.polje[i][j] == "O" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "O"):
                        self.polje[i][j] = "o"
                        self.polje[i + 1][j] = "o"
                        self.polje[i + 2][j] = "o"
                        self.polje[i + 3][j] = "o"
    
            for i in range(3):
                for j in range(4):
                    if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                        self.polje[i][j] = "o"
                        self.polje[i + 1][j + 1] = "o"
                        self.polje[i + 2][j + 2] = "o"
                        self.polje[i + 3][j + 3] = "o"
    
            for i in range(3, 5):
                for j in range(4):
                    if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                        self.polje[i][j] = "o"
                        self.polje[i - 1][j + 1] = "o"
                        self.polje[i - 2][j + 2] = "o"
                        self.polje[i - 3][j + 3] = "o"
            for i in range(6):
                for j in range(4):
                    if (self.polje[i][j] == "X" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "X"):
                        self.polje[i][j] = "x"
                        self.polje[i][j + 1] = "x"
                        self.polje[i][j + 2] = "x"
                        self.polje[i][j + 3] = "x"
                        
            for i in range(3):
                for j in range(7):
                    if (self.polje[i][j] == "X" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "X" and self.polje[i + 3][j] == "X"):
                        self.polje[i][j] = "x"
                        self.polje[i + 1][j] = "x"
                        self.polje[i + 2][j] = "x"
                        self.polje[i + 3][j] = "x"
    
            for i in range(3):
                for j in range(4):
                    if (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "X"):
                        self.polje[i][j] = "x"
                        self.polje[i + 1][j + 1] = "x"
                        self.polje[i + 2][j + 2] = "x"
                        self.polje[i + 3][j + 3] = "x"
    
            for i in range(3, 5):
                for j in range(4):
                    if (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "X"):
                        self.polje[i][j] = "x"
                        self.polje[i - 1][j + 1] = "x"
                        self.polje[i - 2][j + 2] = "x"
                        self.polje[i - 3][j + 3] = "x"

######################################################################################################################################################################

    def vodoravno_4(self):
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O") or (self.polje[i][j] == "X" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "X"):
                    return True

    def navpicno_4(self):
        for i in range(3):
            for j in range(7):
                if (self.polje[i][j] == "O" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "O") or (self.polje[i][j] == "X" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "X" and self.polje[i + 3][j] == "X"):
                    return True

    def posevno_4(self):
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O") or (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "X"):
                    return True

    def posevno2_4(self):
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O") or (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "X"):
                    return True
        
    def zmaga(self):
        if self.vodoravno_4() or self.navpicno_4() or self.posevno_4() or self.posevno2_4() == True:
            return True
        else:
            return False

    
    def st_zmag(self):
        stevilo = 0
        if self.vodoravno_4() or self.navpicno_4() or self.posevno_4() or self.posevno2_4() == True:
            stevilo += 1
        return stevilo

    def zmaga_brez_navp(self):
        if self.vodoravno_4() or self.posevno_4() or self.posevno2_4() == True:
            return True
        else:
            return False

    def vodoravno_4_o(self):
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "o" and self.polje[i][j + 1] == "o" and self.polje[i][j + 2] == "o" and self.polje[i][j + 3] == "o"):
                    return True

    def navpicno_4_o(self):
        for i in range(3):
            for j in range(7):
                if (self.polje[i][j] == "o" and self.polje[i + 1][j] == "o" and self.polje[i + 2][j] == "o" and self.polje[i + 3][j] == "o"):
                    return True

    def posevno_4_o(self):
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "o" and self.polje[i + 1][j + 1] == "o" and self.polje[i + 2][j + 2] == "o" and self.polje[i + 3][j + 3] == "o"):
                    return True

    def posevno2_4_o(self):
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "o" and self.polje[i - 1][j + 1] == "o" and self.polje[i - 2][j + 2] == "o" and self.polje[i - 3][j + 3] == "o"):
                    return True
    
    def zmaga_o(self):
        if self.vodoravno_4_o() or self.navpicno_4_o() or self.posevno_4_o() or self.posevno2_4_o() == True:
            return True
        else:
            return False

    def vodoravno_4_x(self):
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "x" and self.polje[i][j + 1] == "x" and self.polje[i][j + 2] == "x" and self.polje[i][j + 3] == "x"):
                    return True

    def navpicno_4_x(self):
        for i in range(3):
            for j in range(7):
                if (self.polje[i][j] == "x" and self.polje[i + 1][j] == "x" and self.polje[i + 2][j] == "x" and self.polje[i + 3][j] == "x"):
                    return True

    def posevno_4_x(self):
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "x" and self.polje[i + 1][j + 1] == "x" and self.polje[i + 2][j + 2] == "x" and self.polje[i + 3][j + 3] == "x"):
                    return True

    def posevno2_4_x(self):
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "x" and self.polje[i - 1][j + 1] == "x" and self.polje[i - 2][j + 2] == "x" and self.polje[i - 3][j + 3] == "x"):
                    return True

    def zmaga_x(self):
        if self.vodoravno_4_x() or self.navpicno_4_x() or self.posevno_4_x() or self.posevno2_4_x() == True:
            return True
        else:
            return False
        
######################################################################################################################################################################

    def vodoravno_4_0(self):
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    return True

    def navpicno_4_0(self):
        for i in range(3):
            for j in range(7):
                if (self.polje[i][j] == "O" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "O"):
                    return True

    def posevno_4_0(self):
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    return True


    def posevno2_4_0(self):
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    return True

    def zmaga_0(self):
        if self.vodoravno_4_0() or self.posevno2_4_0() or self.posevno_4_0() == True:
            return True
        else:
            return False

######################################################################################################################################################################
    
    def vodoravno_3(self):
        stevilo = 0
        for i in range(6):
            for j in range(5):
                if self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O":
                    stevilo += 1
        return stevilo

    def navpicno_3(self):
        stevilo = 0
        for i in range(4):
            for j in range(7):
                if self.polje[i][j] == "O" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "O":
                    stevilo += 1
        return stevilo

    def posevno_3(self):
        stevilo = 0
        for i in range(4):
            for j in range(5):
                if self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O":
                    stevilo += 1
        return stevilo

    def posevno2_3(self):
        stevilo = 0
        for i in range(2, 5):
            for j in range(5):
                if self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O":
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def vodoravno_2_0(self):
        stevilo = 0
        for i in range(6):
            for j in range(5):
                if self.polje[i][j] == "O" and self.polje[i][j + 1] == "O":
                    stevilo += 1
        return stevilo

    def navpicno_2_0(self):
        stevilo = 0
        for i in range(5):
            for j in range(7):
                if self.polje[i][j] == "O" and self.polje[i + 1][j] == "O":
                    stevilo += 1
        return stevilo

    def posevno_2_0(self):
        stevilo = 0
        for i in range(5):
            for j in range(6):
                if self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O":
                    stevilo += 1
        return stevilo

    def posevno2_2_0(self):
        stevilo = 0
        for i in range(1, 5):
            for j in range(6):
                if self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O":
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def blokada_zmage_vodoravno(self):
        stevilo = 0
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "X" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "X"):
                    stevilo += 1
        return stevilo

    def blokada_zmage_navpicno(self):
        stevilo = 0
        for i in range(3):
            for j in range(7):
                if (self.polje[i][j] == "O" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "X" and self.polje[i + 3][j] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "X" and self.polje[i + 3][j] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "X"):
                    stevilo += 1
                if ( self.polje[i][j] == "X" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "X" and self.polje[i + 3][j] == "O"):
                    stevilo += 1
        return stevilo

    def blokada_zmage_posevno(self):
        stevilo = 0
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
        return stevilo

    def blokada_zmaga_posevno2(self):
        stevilo = 0
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def blokada_zmage_vodoravno_O(self):
        stevilo = 0
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
        return stevilo

    def blokada_zmage_posevno_O(self):
        stevilo = 0
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "X"):
                    stevilo += 1
        return stevilo

    def blokada_zmaga_posevno2_O(self):
        stevilo = 0
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "X"):
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def blokada_vodoravno_3(self):
        stevilo = 0
        for i in range(6):
            for j in range(5):
                if self.polje[i][j] == "X" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "X":
                    stevilo += 1
                if self.polje[i][j] == "X" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "X":
                    stevilo += 1
        return stevilo

    def blokada_navpicno_3(self):
        stevilo = 0
        for i in range(4):
            for j in range(7):
                if self.polje[i][j] == "X" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "X":
                    stevilo += 1
                if self.polje[i][j] == "X" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "X":
                    stevilo += 1     
        return stevilo

    def blokada_posevno_3(self):
        stevilo = 0
        for i in range(4):
            for j in range(5):
                if self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "X":
                    stevilo += 1
                if self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "X":
                    stevilo += 1
        return stevilo

    def blokada_posevno2_3(self):
        stevilo = 0
        for i in range(2, 5):
            for j in range(5):
                if self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "X":
                    stevilo += 1
                if self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "X":
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def blokada_vodoravno_2(self):
        stevilo = 0
        for i in range(6):
            for j in range(5):
                if self.polje[i][j] == "X" and self.polje[i][j + 1] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i][j + 1] == "X":
                    stevilo += 1
        return stevilo

    def blokada_navpicno_2(self):
        stevilo = 0
        for i in range(5):
            for j in range(7):
                if self.polje[i][j] == "X" and self.polje[i + 1][j] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i + 1][j] == "X":
                    stevilo += 1
        return stevilo

    def blokada_posevno_2(self):
        stevilo = 0
        for i in range(5):
            for j in range(6):
                if self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "X":
                    stevilo += 1
        return stevilo

    def blokada_posevno2_2(self):
        stevilo = 0
        for i in range(1, 5):
            for j in range(6):
                if self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "O":
                    stevilo += 1
                if self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "X":
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def blokada_nase_zmage_vodoravno(self):
        stevilo = 0
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "X"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "X" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "X" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "X" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
        return stevilo

    def blokada_nase_zmage_navpicno(self):
        stevilo = 0
        for i in range(3):
            for j in range(7):
                if (self.polje[i][j] == "X" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j] == "X" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "X" and self.polje[i + 3][j] == "O"):
                    stevilo += 1
                if ( self.polje[i][j] == "O" and self.polje[i + 1][j] == "O" and self.polje[i + 2][j] == "O" and self.polje[i + 3][j] == "X"):
                    stevilo += 1
        return stevilo

    def blokada_nase_zmage_posevno(self):
        stevilo = 0
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == "X" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "X" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "X" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "X"):
                    stevilo += 1        
        return stevilo

    def blokada_nase_zmage_posevno2(self):
        stevilo = 0
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == "X" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "X" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "X" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "X"):
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def zmaga_vodoravno_presledek(self):
        stevilo = 0
        for i in range(6):
            for j in range(4):
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == " "):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == " " and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i][j + 1] == " " and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == " " and self.polje[i][j + 1] == "O" and self.polje[i][j + 2] == "O" and self.polje[i][j + 3] == "O"):
                    stevilo += 1
        return stevilo

    def zmaga_posevno_presledek(self):
        stevilo = 0
        for i in range(3):
            for j in range(4):
                if (self.polje[i][j] == " " and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == " " and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == " " and self.polje[i + 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i + 1][j + 1] == "O" and self.polje[i + 2][j + 2] == "O" and self.polje[i + 3][j + 3] == " "):
                    stevilo += 1
        return stevilo

    def zmaga_posevno2_presledek(self):
        stevilo = 0
        for i in range(3, 5):
            for j in range(4):
                if (self.polje[i][j] == " " and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == " " and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == " " and self.polje[i - 3][j + 3] == "O"):
                    stevilo += 1
                if (self.polje[i][j] == "O" and self.polje[i - 1][j + 1] == "O" and self.polje[i - 2][j + 2] == "O" and self.polje[i - 3][j + 3] == " "):
                    stevilo += 1
        return stevilo

######################################################################################################################################################################

    def izbira_poteze_robot(self):
        slovar = {}
        dobre_poteze = []
        seznam = []
        for izbira in self.seznam_pravilnih():
            slovar[izbira] = 0
        
        for izbira in self.seznam_pravilnih():
            if izbira == 2 or izbira == 3 or izbira == 4:
                slovar[izbira] = slovar[izbira] + 150
        
        for izbira in self.seznam_pravilnih():
            if self.get_visina(izbira) == 1 or self.get_visina(izbira) == 2 or self.get_visina(izbira) == 3:
                slovar[izbira] = slovar[izbira] + 150

        # preveri zmago
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            if self.zmaga() == True:
                slovar[izbira] = slovar[izbira] + 100000000000000000000000000000000000000
            self.odstrani_kovanec(izbira)
        
        # gradi svoje trojke
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            slovar[izbira] = slovar[izbira] + (self.vodoravno_3() + self.navpicno_3() + self.posevno_3() + self.posevno2_3()) * 2700
            self.odstrani_kovanec(izbira)
        
        # dela svoje dvojice
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            slovar[izbira] = slovar[izbira] + (self.vodoravno_2_0() + self.navpicno_2_0() + self.posevno_2_0() + self.posevno2_2_0())*300
            self.odstrani_kovanec(izbira)
        
        # ce po dodattku kovanca nasprotnik zmaga to prepreci
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            if self.get_visina(izbira) != 6:
                self.dodaj_kovanec_X(izbira)
                if self.zmaga() == True:
                        slovar[izbira] = slovar[izbira] - 10000000000000000000000
                self.odstrani_kovanec(izbira)
            self.odstrani_kovanec(izbira)
        
        # ce mu po metu kovanca, nasprotnik unici 4ko, to prepreci
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            k = self.blokada_zmage_vodoravno_O() + self.blokada_zmage_posevno_O() + self.blokada_zmaga_posevno2_O()
            if self.get_visina(izbira) != 6:
                self.dodaj_kovanec_X(izbira)
                l =  self.blokada_zmage_vodoravno_O() + self.blokada_zmage_posevno_O() + self.blokada_zmaga_posevno2_O()
                if k < l:
                    slovar[izbira] = slovar[izbira] - 100000000
                self.odstrani_kovanec(izbira)
            self.odstrani_kovanec(izbira)
        
        # ce lahko prepreci zmago nasprotnika jo prepreci
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            slovar[izbira] = slovar[izbira] + (self.blokada_zmage_vodoravno() + self.blokada_zmage_navpicno() + self.blokada_zmage_posevno() + self.blokada_zmaga_posevno2())*10000000000000000000000000000
            self.odstrani_kovanec(izbira)
     
        # prisiljeno zmago naredi
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            k = self.blokada_zmage_vodoravno_O() + self.blokada_zmage_posevno_O() + self.blokada_zmaga_posevno2_O()
            if self.get_visina(izbira) < 5:
                self.dodaj_kovanec_X(izbira)
                l = self.blokada_zmage_vodoravno_O() + self.blokada_zmage_posevno_O() + self.blokada_zmaga_posevno2_O()
                if k < l:
                    self.dodaj_kovanec_O(izbira)
                    if self.zmaga_0() == True:
                        slovar[izbira] = slovar[izbira] + 100000000000000000
                    self.odstrani_kovanec(izbira)
                self.odstrani_kovanec(izbira)
            self.odstrani_kovanec(izbira)
 
        # blokira nasprotnikove trojke
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            slovar[izbira] = slovar[izbira] + (self.blokada_vodoravno_3() + self.blokada_navpicno_3() + self.blokada_posevno_3() + self.blokada_posevno2_3())*1000
            self.odstrani_kovanec(izbira)

        # trojice s presledkom
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            slovar[izbira] = slovar[izbira] + (self.zmaga_vodoravno_presledek() +  self.zmaga_posevno_presledek() + self.zmaga_posevno2_presledek()) * 2000
            self.odstrani_kovanec(izbira)
        
        #ne vrze trojke na vrh
        for izbira in self.seznam_pravilnih():
            k = self.navpicno_3()
            self.dodaj_kovanec_O(izbira)
            if self.get_visina(izbira) == 6:
                l = self.navpicno_3()
                if k < l:
                    slovar[izbira] = slovar[izbira] - 2000
            self.odstrani_kovanec(izbira)
        
        # ne mece v kot ce je troijca
        for izbira in self.seznam_pravilnih():
            k = self.vodoravno_3() + self.posevno_3() + self.posevno2_3()
            self.dodaj_kovanec_O(izbira)
            if izbira == 0 or izbira == 6:
                l = self.vodoravno_3() + self.posevno_3() + self.posevno2_3()
                if k < l:
                    slovar[izbira] = slovar[izbira] - 2000
            self.odstrani_kovanec(izbira)  
        
        # ce sta po dodatku kovanca dve razlicni zmagi, to naredi
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_O(izbira)
            stevilo_zmag = 0
            for i in self.seznam_pravilnih():
                self.dodaj_kovanec_O(i)
                stevilo_zmag += self.st_zmag()
                self.odstrani_kovanec(i)
            if stevilo_zmag >= 2:
                slovar[izbira] = slovar[izbira] + 10000000000000000
            self.odstrani_kovanec(izbira)
        
        #blokira potezo ki naredi dva poraza
        for izbira in self.seznam_pravilnih():
            self.dodaj_kovanec_X(izbira)
            stevilo_porazov = 0
            for i in self.seznam_pravilnih():
                self.dodaj_kovanec_X(i)
                stevilo_porazov += self.st_zmag()
                self.odstrani_kovanec(i)
            if stevilo_porazov >= 2:
                slovar[izbira] = slovar[izbira] + 100000000000000
            self.odstrani_kovanec(izbira)

        for n in self.seznam_pravilnih():
            seznam.append(slovar[n])
        if seznam == []:
            return None
        else:
            m = max(seznam)
            for j in self.seznam_pravilnih():
                if slovar[j] == m:
                    dobre_poteze.append(j)
            k = random.randint(0, len(dobre_poteze) - 1)
            if self.seznam_pravilnih() == []:
                return None
            else:
                return dobre_poteze[k]

    def izbira_poteze_robot_easy(self):
        izbira = random.randint(0, 6)
        return izbira
 
    def zeton_na_mestu(self, vrstica, stolpec):
        return self.polje[vrstica][stolpec]
     