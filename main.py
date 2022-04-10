from dataclasses import dataclass

@dataclass(frozen=True)
class Pracownik:
    imie: str
    wynagrodzenie_brutto: int

    def wynagrodzenie_netto(self) -> float:
        poz_c = round(self.wynagrodzenie_brutto * 0.0976,2) + round(self.wynagrodzenie_brutto * 0.015,2) + round(self.wynagrodzenie_brutto * 0.0245,2)
        poz_c = round(poz_c,2)

        poz_d = self.wynagrodzenie_brutto - round(poz_c,2)
        poz_d = round(poz_d,2)

        poz_e = poz_d * 0.09
        poz_e = round(poz_e,2)

        poz_f = poz_d * 0.0775
        poz_f = round(poz_f,2)

        poz_g = 111.25

        poz_h = self.wynagrodzenie_brutto - poz_g
        poz_h = round(poz_h, 2)
        poz_h -= round(poz_c,2)
        poz_h = round(poz_h, 2)
        
        poz_h_18 = poz_h * 0.18
        poz_h_18 = round(poz_h_18, 2)
        poz_i = poz_h_18 - 46.33
        poz_i = round(poz_i,2)

        poz_j = round(poz_i,2) - round(poz_f,2)
        poz_j = round(poz_j,2)
        
        netto = self.wynagrodzenie_brutto
        netto -= round(poz_c,2)
        netto = round(netto,2)
        netto -= round(poz_e,2)
        netto = round(netto,2)
        netto -= round(poz_j,2)
        netto = round(netto,2)
        
        return netto
    
    def skladki_pracodawcy(self) -> float:
        poz_i = round(self.wynagrodzenie_brutto * 0.0976,2) + round(self.wynagrodzenie_brutto * 0.065,2) + round(self.wynagrodzenie_brutto * 0.0193,2) + round(self.wynagrodzenie_brutto * 0.0245,2) + round(self.wynagrodzenie_brutto * 0.001,2)
        poz_i = round(poz_i,2)
        return poz_i
    
    def koszt_pracodawcy(self) -> float:
        poz_i = round(self.wynagrodzenie_brutto * 0.0976,2) + round(self.wynagrodzenie_brutto * 0.065,2) + round(self.wynagrodzenie_brutto * 0.0193,2) + round(self.wynagrodzenie_brutto * 0.0245,2) + round(self.wynagrodzenie_brutto * 0.001,2)
        poz_i = round(poz_i,2)
        koszt = self.wynagrodzenie_brutto + poz_i
        koszt = round(koszt,2)
        return koszt






def main():
    liczba_pracownikow = int(input())
    pracownicy = []
    for _ in range(liczba_pracownikow):
        pracownik = input()
        pracownik = pracownik.split(' ')
        pracownik = Pracownik(pracownik[0], int(pracownik[1]))
        pracownicy.append(pracownik)
    laczny_koszt = 0
    for pracownik in pracownicy:
        netto = pracownik.wynagrodzenie_netto()
        skladki = pracownik.skladki_pracodawcy()
        koszt = pracownik.koszt_pracodawcy()
        laczny_koszt += koszt
        print(pracownik.imie,netto,skladki,koszt)
    
    print(laczny_koszt)

    

if __name__ == "__main__":
    main()