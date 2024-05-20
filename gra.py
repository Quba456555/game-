import random
import time
from przeciwnik import Przeciwnik, Czarodziej, BagnistaZaba1, BagnistaZaba2
from boss import Boss1, Boss2, Boss3
from gracz import Gracz, Player ,Player2 ,Nazgul
from world import World, Battle


#========================================
def start_game():
    
    print("twojim zadaniem jest pokonac wszystkich nazguli i dobyc pierscien")
    player2 = Player2("Twojej", 100, 20,15)

    
    nazgul1 = Nazgul("Król Nazguli", 15, 30, 3, "Morgulskie ostrze")
    nazgul2 = Nazgul("Khamul", 25, 25, 6, "Czarny dart")
    nazgul3 = Nazgul("Adunaphel", 31, 28, 9, "Miecz")

   
    player2.encounter_nazgul(nazgul1)
    player2.encounter_nazgul(nazgul2)
    player2.encounter_nazgul(nazgul3)

    if player2.health > 0:
        print("Gratulacje! Pokonałeś wszystkich Nazgulów i zdobyłeś pierścień!")
    else:
        print("Koniec gry! Nazgulowie pokonali cię.")

def main2():
        player = Player()
        world = World()
        gra=Gra()
        current_level = 1
        enemies_defeated = 0
        enemies_per_level = 3
        max_level = 1

        while current_level <= max_level and player.is_alive():
            print(f"--- Poziom {current_level} ---")
            print("pokonaj 3 przeciwnikow")
            print("1. Przejdź do nowej lokacji")
            print("2. Wyświetl ekwipunek")
            print("3. Wyjdź z gry")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                location = world.generate_location()
                world.enter_location(location, player)
                if not player.is_alive():
                    print("Zostałeś pokonany. Koniec gry.")
                    break
                enemies_defeated += 1
                if enemies_defeated >= enemies_per_level:
                    current_level += 1
                    enemies_defeated = 0
                    if current_level > max_level:
                        print("Gratulacje! pokonałeś zaby.")
                        break
                    else:
                        print(f"Przechodzisz na poziom {current_level}")
            elif choice == "2":
                player.display_inventory()
            elif choice == "3":#
                print("Koniec gry")
                break
            else:
               print("Nieprawidłowy wybór, spróbuj ponownie.")


class Gra:
    def __init__(self):
        self.poziom = 1
        self.wygrane_poziomy = 0
        self.zdrowie = 20
        self.zloto = 50
        self.mana = 0
        self.ekwipunek = []

    

#===============================================
    def sciezka(self):
        print(" Wybierz ścieżkę:")
        print("1. Podejdź do wieży czarodzieja")
        print("2. Wędruj dalej")
        wybor = input("Twój wybór: ")

        if wybor == "1":
            self.wieza_czarodzieja()
        elif wybor == "2":
            self.wedruj_dalej()
        else:
            print("Nieprawidłowy wybór.")

    

    def wieza_czarodzieja(self):
        czarodziej = Czarodziej()
        print(f"Aktualna ilośc zlota: {self.zloto}")
        self.kup_bron()
        bron = self.ekwipunek[-1] 
        self.wyswietl_ekwipunek()
        czarodziej.interakcja_z_czarodziejem(bron)

    def wedruj_dalej(self):
        print("Kontynuujesz swoją wędrówkę...")

        
    


#===============================================================
    def kup_bron(self):
        print("Witaj w sklepie z bronią! Oto dostępne bronie:")
        print("1. Łuk (20 złota)")
        print("2. Miecz (30 złota)")
        print("3. Tarcza i Zbroja (25 złota)")

        wybor = input("Wybierz broń, którą chcesz kupić (1-3): ")

        if wybor == "1":
            if self.zloto >= 20:
                self.zloto -= 20
                print("Kupiłeś łuk za 20 złota. Powodzenia w walce!")
                self.ekwipunek.append("Łuk")
            else:
                print("Nie masz wystarczająco złota.")
        elif wybor == "2":
            if self.zloto >= 30:
                self.zloto -= 30
                print("Kupiłeś miecz za 30 złota. Powodzenia w walce!")
                self.ekwipunek.append("Miecz")
            else:
                print("Nie masz wystarczająco złota.")
        elif wybor == "3":
            if self.zloto >= 25:
                self.zloto -= 25
                print("Kupiłeś tarczę zbroję za 25 złota. Powodzenia w walce!")
                self.ekwipunek.append("Tarcza Zbroja")
            else:
                print("Nie masz wystarczająco złota.")
        else:
            print("Nieprawidłowy wybór. Wybierz numer od 1 do 3.")

    def wyswietl_ekwipunek(self):
        print("Twój aktualny ekwipunek:")
        for przedmiot in self.ekwipunek:
            print(przedmiot)

#==============================================================

    def zatrzymaj(self):
        print("Złap 10 świetlików!\nNaciśnij enter")
        input()
        for i in range(1, 11):
            print(i)
            time.sleep(0.1)
        return 10

    def kasyno(self):
        while True:
            print("Kasyno. Co chcesz zrobić?")
            print("(1) Graj")
            print("(2) Zakończ")

            wybor = input("Twój wybór: ")

            if wybor == "1":
                zmiana_zlota = random.randint(-10, 10)
                self.zloto += zmiana_zlota
                if zmiana_zlota > 0:
                    print(f"\nWygrałeś {zmiana_zlota} sztuk złota. Masz teraz {self.zloto} złota\n")
                    time.sleep(1)
                else:
                    print(f"\nPrzegrałeś {abs(zmiana_zlota)} sztuk złota. Masz teraz {self.zloto} złota\n")
                    time.sleep(1)
            elif wybor == "2":
                print("Zakończono grę w kasynie.")
                break
            else:
                print("Nieprawidłowy wybór. Wybierz 1 lub 2.")

    def spotkanie(self):
        while True:
            print("Spotkanie z nieznaną postacią... Możesz zyskać manę. Naciśnij enter")
            input()
            dodaj_many = random.randint(10, 50)
            print(f"Twoja mana wynosi teraz {dodaj_many}. Czy szukasz kolejnego spotkania? (Naciśnij 't' aby losować ponownie)")
            wybor = input("Twój wybór: ")
            if wybor != 't':
                break
        return dodaj_many

    def wybierz_taktyke(self):
        while True:
            print("Wybierz taktykę:\n(1) Atak frontalny\n(2) Atak z flanki\n(3) Ataki z ukrycia\n")
            wybor_taktyki = input("Twój wybór: ")
            if wybor_taktyki.isdigit() and 1 <= int(wybor_taktyki) <= 3:
                break
            print("Podaj liczbę z zakresu 1-3.")
        return int(wybor_taktyki)

    def walka(self, taktyka_gracza, przeciwnik):
        print(f"\nWalczyłeś z {przeciwnik}!")
        wynik_walki = random.randint(1, 6)
        modifier = random.randint(-2, 2)

        if taktyka_gracza == 1:
            wynik_walki += 4
        elif taktyka_gracza == 2:
            wynik_walki += modifier
        elif taktyka_gracza == 3:
            wynik_walki += 4

        return wynik_walki

    def sklep(self):
        ilosc_many_str = input("Ile many chcesz kupić? 1 złoto = 1 mana (Wpisz 0, aby zakończyć zakupy): ")

        if not ilosc_many_str.isdigit():
            print("Wprowadź liczbę całkowitą.")
            return

        ilosc_many = int(ilosc_many_str)
        cena = ilosc_many

        if cena > self.zloto:
            print("Nie masz wystarczająco złota. Spróbuj mniejszą ilość.")
        else:
            self.mana += ilosc_many
            self.zloto -= cena
            print(f"Kupiłeś {ilosc_many} many za {cena} złota.")

    

    def walka_z_bossem(self, mana):
        print("Walka z bossem 1!")
        boss1 = Boss1()

        while mana >= 0:
            print(f"\nAktualne życie bossa 1: {boss1.zycie}")
            print(f"Aktualna ilość many: {mana}")
            input("Naciśnij enter, aby strzelić...\n")

            mana = boss1.atak(mana)
            time.sleep(1)

            if boss1.zycie <= 0:
                print("\nPokonałeś bossa 1! Gratulacje! Idziesz dalej!\n")
                time.sleep(1)
                break

            print("\nBoss 1 kontratakuje!")
            time.sleep(1)
            mana = boss1.kontratak(mana)

            if mana <= 0:
                print("Za mało many, aby kontynuować walkę!")
                break


    def walka_z_bossem2(self, nowa_mana):
        print("Walka z bossem 2!")
        boss2 = Boss2()
    
        while boss2.zycie > 0 and nowa_mana >= 10:
            print(f"\nAktualne życie bossa 2: {boss2.zycie}")
            print(f"Aktualna ilość many: {nowa_mana}")
            print("Wybierz akcję:")
            print("1. Atak mocny - zużywa 10 many, może zdać 15-25 obrażeń bossowi")
            print("2. Atak słaby - zużywa 5 many, może zadać 10-20 obrażeń bossowi")
            wybor = input("Twój wybór: ")
        
            if wybor == '1':
                strzal = random.randint(15, 25)
                boss2.zycie -= strzal
                nowa_mana -= 10
                print(f"Tracisz 10 many. Zadałeś bossowi 2 {strzal} obrażeń!\n")
                time.sleep(1)
            elif wybor == '2':
                strzal = random.randint(10, 20)
                boss2.zycie -= strzal
                nowa_mana -= 5
                print(f"Tracisz 5 many. Zadałeś bossowi 2 {strzal} obrażeń!\n")
                time.sleep(1)
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.\n")
                continue
        
            if boss2.zycie <= 0:
                print("Brawo! Pokonałeś bossa 2!")
                time.sleep(1)
                break
        
           
            print("\nBoss 2 atakuje!")
            time.sleep(1)
            obrazenia_bossa = random.randint(1, 10)
            print(f"Boss 2 zadał Ci {obrazenia_bossa} obrażeń!\n")
            nowa_mana -= obrazenia_bossa
            time.sleep(1)
        
            if nowa_mana <= 0:
                print("Nie masz już many. Nie udało Ci się pokonać bossa 2. Uciekasz!")
                break
#========================================================
    def walka_z_bossem3(self, boss):
        print("Walka z bossem 3!")

        while boss.zdrowie > 0 and self.zdrowie > 0:
            print(f"Aktualne życie bossa 3: {boss.zdrowie}")
            print(f"Twoje aktualne zdrowie: {self.zdrowie}")

            taktyka_gracza = self.wybierz_taktyke2()
            obrazenia_gracza = boss.atak(taktyka_gracza)
            print(f"Zadajesz bossowi 3 {obrazenia_gracza} obrażeń!")

            taktyka_bossa = random.randint(1, 3)
            obrazenia_bossa = boss.atak(taktyka_bossa)
            print(f"Boss 3 zadaje Ci {obrazenia_bossa} obrażeń!")

            self.zdrowie -= obrazenia_bossa
            boss.zdrowie -= obrazenia_gracza
            time.sleep(1)

        if self.zdrowie <= 0:
            print("Przegrałeś walkę z bossem 3.")

    def wybierz_taktyke2(self):
        while True:
            print("Wybierz taktykę mistrzów:")
            print("1. Atak agresywny")
            print("2. Atak zrównoważony")
            print("3. Atak defensywny")
            wybor_taktyki = input("Twój wybór: ")

            if wybor_taktyki.isdigit() and 1 <= int(wybor_taktyki) <= 3:
                return int(wybor_taktyki)
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę od 1 do 3.")

    def przegraj_z_bossem3(self):
        print("Boss 3 oferuje ci układ...")
        print("1. Przegrasz i stracisz 50% swojego złota.")
        print("2. Zgodzisz się dać mu 40 sztuk złota i uciekniesz.")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            self.zloto *= 0.5
            print(f"Straciłeś połowę swojego złota. Aktualna liczba złota: {self.zloto}")
        elif wybor == "2":
            if self.zloto >= 40:
                self.zloto -= 40
                print("Zgodziłeś się dać bosowi 40 sztuk złota i uciekniesz.")
            else:
                print("Nie masz wystarczająco złota, aby zapłacić bossowi.")
        else:
            print("Nieprawidłowy wybór.")

    
    






    def skarbiec(self):
        print("Udało Ci się znaleźć skarbiec bossa z maną.\nZgadnij liczbę aby go otworzyć!")
        liczba_do_odgadniecia = random.randint(1, 10)
        liczba_prob = 0
        zakres_dolny = 1
        zakres_gorny = 10

        while True:
            strzal = int(input(f"Zgadnij liczbę (od {zakres_dolny} do {zakres_gorny}): "))
            liczba_prob += 1

            if strzal < liczba_do_odgadniecia:
                print("Za mało! Spróbuj ponownie.")
                zakres_dolny = strzal + 1
            elif strzal > liczba_do_odgadniecia:
                print("Za dużo! Spróbuj ponownie.")
                zakres_gorny = strzal - 1
            else:
                print(f"Brawo! Odgadłeś tę liczbę {liczba_do_odgadniecia} i otworzyłeś skarbiec!")
                print(f"Zajęło Ci to {liczba_prob} prób.")
                print("Zgarniasz 200 many i 100 zlota")
                self.zloto+= 100        
                self.mana += 200
                print(f" Aktualna ilość many i zlota : {self.mana} , {self.zloto}")
                time.sleep(1)
                break

    def logika_gry(self):

       #==============================
        #start_game()
        #main2()

        print("\nWygraj 5 poziomów aby przejść dalej!\n")
        time.sleep(1)

        while self.wygrane_poziomy < 5:
            przeciwnik = Przeciwnik(self.poziom).wylosowany
            print(f"Walczysz na poziomie {self.poziom} z {przeciwnik}!")
            
            taktyka_gracza = self.wybierz_taktyke()
            wynik_walki = self.walka(taktyka_gracza, przeciwnik)
            print(f"Wynik walki: {wynik_walki}")
            time.sleep(1)

            if wynik_walki >= 5:
                    self.wygrane_poziomy += 1
                    self.poziom += 1
                    self.zdrowie += 3
                    if self.zdrowie > 10:
                        self.zdrowie = 10
                    print(f"Pokonałeś przeciwnika! Twoje zdrowie {self.zdrowie}. Wygrane poziomy {self.wygrane_poziomy}\n")
                    time.sleep(1)
                   
            else:
                self.zdrowie -= 2
                self.wygrane_poziomy -= 1
                if self.wygrane_poziomy < 1:
                    self.wygrane_poziomy = 0
                print(f"Przegrałeś walkę. Twoje zdrowie {self.zdrowie}. Wygrane poziomy {self.wygrane_poziomy}. Spróbuj ponownie.\n")
                if self.zdrowie <= 0:
                    print("Straciłeś wszystkie punkty zdrowia. Koniec gry.")
                    break
            
            if self.wygrane_poziomy == 5:
                self.wygrane_poziomy += 1
                print("Wygrałeś wszystkie walki!\n")

        print(f"Masz teraz {self.zloto} sztuk złota. Idziesz do kasyna")
        self.kasyno()
        print(f"Masz teraz {self.zloto} sztuk złota.\n")

        print(f"Masz teraz {self.mana} many.")
        self.mana = self.spotkanie()
        print(f"Twoja mana wynosi teraz {self.mana}.\n")
        
        print(f"Wchodzisz do sklepu, możesz kupić many do walki z bossem. Teraz mana {self.mana}, złoto {self.zloto}.\n")
        self.sklep()
        print(f"Twoja mana wynosi teraz {self.mana}, a złoto {self.zloto}.\n")
        time.sleep(1)

        self.walka_z_bossem(self.mana)

        print("Złap max 10 magicznych świtlików. To kluczowe aby zwiększyć manę przed walką z Bossem 2!")
        wynik = self.zatrzymaj()
        nowa_mana = wynik*10
        print(f'Złapałeś {wynik} magicznych świetlików. Twoja nowa mana {wynik}*10={nowa_mana}')
        time.sleep(1)

        self.walka_z_bossem2(nowa_mana)


        self.skarbiec()

        
        gra = Gra()
        boss3 = Boss3()
        gra.walka_z_bossem3(boss3)
        gra.przegraj_z_bossem3()

        print(f"Masz  {self.zloto} złota do dyspozycji")
        
        self.sciezka()

        main2()

        start_game()

        

        print("Zdobyłes najpotezniejszy atefakt jestes nie pokonany, wygrales gre ")
        print("\nGAME OVER!")
        
