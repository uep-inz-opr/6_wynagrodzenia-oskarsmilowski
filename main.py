from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Pracownik:
    imie: str
    wynagrodzenie_brutto: int

    def wynagrodzenie_netto(self) -> float:
        poz_c = self.wynagrodzenie_brutto * 0.1371
        poz_c = round(poz_c,2)

        poz_d = self.wynagrodzenie_brutto - poz_c

        poz_e = poz_d * 0.09
        poz_e = round(poz_e,2)

        poz_f = poz_d * 0.0775
        poz_f = round(poz_f,2)

        poz_g = 111.25

        poz_h = self.wynagrodzenie_brutto - poz_g - poz_c
        poz_h = round(poz_h, 2)
        
        poz_h_18 = poz_h * 0.18
        poz_h_18 = round(poz_h_18, 2)
        poz_i = poz_h_18 - 46.33

        poz_j = poz_i - poz_f
        poz_j = round(poz_j,2)
        

        netto = self.wynagrodzenie_brutto - poz_c - poz_e - poz_j
        netto = round(netto, 2)
        return netto
    
    def skladki_pracodawcy(self) -> float:
        poz_i = self.wynagrodzenie_brutto * 0.2074
        poz_i = round(poz_i,2)
        return poz_i
    
    def koszt_pracodawcy(self) -> float:
        poz_i = self.wynagrodzenie_brutto * 0.2074
        poz_i = round(poz_i,2)
        return self.wynagrodzenie_brutto + poz_i






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
        print(pracownik.imie, netto,skladki,koszt)
    
    print(laczny_koszt)

    

if __name__ == "__main__":
    main()