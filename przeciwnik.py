
import random



class Przeciwnik:
    def __init__(self, poziom):
        if poziom <= 3:
            self.typy = ["Gruby wolny, ale silny", "Średnio szybki i silny", "Chudy słaby, ale szybki"]
        else:
            self.typy = ["Czarownik", "Troll", "Elf"]
        self.wylosowany = random.choice(self.typy)


class Czarodziej:
    def __init__(self):
        self.eliksir_leczenia = False
        self.zycie = 20

    def interakcja_z_czarodziejem(self, bron):
        print("Przychodzisz do wieży czarodzieja...\n")
        print("Czarodziej okazuje się być złym czarownikiem!\n")
        print("Więzi cię i daje zadania matematyczne do rozwiązania...\n")

        if self.rozwiazano_zadania():
            print("Udało Ci się uwolnić! Teraz toczysz pojedynek z czarownikiem.\n")
            if self.walka_z_czarodziejem(bron):
                self.eliksir_leczenia = True
                print("Pokonałeś czarodzieja! Zdobywasz eliksir leczenia i 6 zmysł.\n")
            else:
                print("Niestety, przegrałeś pojedynek z czarodziejem.")
        else:
            print("Nie udało Ci się rozwiązać zadań matematycznych. Pozostajesz więziony.\n")

    def rozwiazano_zadania(self):
        print("Rozwiązujesz zadania matematyczne...\n")
        for _ in range(3):
            if not self.rozwiaz_zadanie():
                return False
        return True

    def rozwiaz_zadanie(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        wynik = a * b
        odpowiedz = input(f"Ile wynosi {a} * {b}? ")
        try:
            odpowiedz = int(odpowiedz)
            return odpowiedz == wynik
        except ValueError:
            print("Nieprawidłowy format odpowiedzi. Podaj liczbę całkowitą.\n")
            return False


    def walka_z_czarodziejem(self, bron):
        print("Walczyłeś z czarodziejem...\n")
        
        while self.zycie > 0:
            obrazenia = self.obrazenia_gracza(bron)
            atak_czarodzieja = random.randint(1, 5)

            print(f"Twój atak używając {bron}: {obrazenia}")
            print(f"Atak czarodzieja: {atak_czarodzieja}")

            if obrazenia > atak_czarodzieja:
                print("Trafiłeś czarodzieja!\n")
                self.zycie -= obrazenia
                print(f"Zycie czarodzieja: {self.zycie}")
            elif obrazenia < atak_czarodzieja:
                print("Czarodziej trafił Cię!\n")
                print(f"Twój aktualny poziom życia: {obrazenia}")
            else:
                print("Wymiana ataków, nikt nie trafia...\n")

            if self.zycie <= 0:
                return True
            else:
                print("Czarodziej jest wpieniony!\n")
                input("Naciśnij Enter, dojechać czarodzieja\n")

        return False

    def obrazenia_gracza(self, bron):
        if bron == "Miecz":
            return random.randint(7, 10)
        elif bron == "Łuk":
            return random.randint(5, 8)
        elif bron == "Tarcza i Zbroja":
            return random.randint(4, 6)
        else:
            print("Używasz pięści.")
            return random.randint(1, 3)


#=============================================

class Character:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.character.defense)
        enemy.take_damage(damage)

class BagnistaZaba1:
    def __init__(self):
        self.name = "Bagnista Zaba 1"
        self.character = Character(health=25, attack=5, defense=5)

    def is_alive(self):
        return self.character.health > 0

    def take_damage(self, damage):
        self.character.take_damage(damage)

    def attack_player(self, player):
        self.character.attack_enemy(player)

class BagnistaZaba2:
    def __init__(self):
        self.name = "Bagnista Zaba 2"
        self.character = Character(health=35, attack=5, defense=5)

    def is_alive(self):
        return self.character.health > 0

    def take_damage(self, damage):
        self.character.take_damage(damage)

    def attack_player(self, player):
        self.character.attack_enemy(player)


class Nazgul(Character):
    def __init__(self, name, health, attack, defense, weapon):
        super().__init__(health, attack, defense)
        self.name = name
        self.weapon = weapon

    def use_weapon(self, enemy):
        print(f"{self.name} with {self.weapon} strikes {enemy.name}!")
        enemy.take_damage(self.attack)

# Tworzymy trzech Nazgulów
nazgul1 = Nazgul("Witch-king", 150, 30, 20, "Morgul Blade")
nazgul2 = Nazgul("Khamul", 130, 25, 15, "Black Dart")
nazgul3 = Nazgul("Adunaphel", 140, 28, 18, "Sword")
           
