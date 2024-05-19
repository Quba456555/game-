import random
import time


class Boss1:
    def __init__(self):
        self.zycie = 60
        self.strzal_min = 10
        self.strzal_max = 20

    def atak(self, mana):
        strzal = random.randint(self.strzal_min, self.strzal_max)
        print(f"Zadajesz {strzal} obrażeń bossowi 1!")
        self.zycie -= strzal
        return mana - 10

    def kontratak(self, mana):
        obrazenia_bossa = random.randint(5, 10)
        print(f"Boss 1 zużył {obrazenia_bossa} Twojej many!")
        return mana - obrazenia_bossa

class Boss2:
    def __init__(self):
        self.zycie = 100

    def atak(self, mana, wybor):
        if wybor == '1':
            strzal = random.randint(15, 25)
            print(f"Tracisz 10 many. Zadałeś bossowi {strzal} obrażeń!\n")
            self.zycie -= strzal
            return mana - 10
        elif wybor == '2':
            strzal = random.randint(10, 20)
            print(f"Tracisz 5 many. Zadałeś bossowi {strzal} obrażeń!\n")
            self.zycie -= strzal
            return mana - 5
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")
            return mana

    def kontratak(self, mana):
        obrazenia_bossa = random.randint(1, 10)
        print(f"Boss zadał Ci {obrazenia_bossa} obrażeń!\n")
        return mana

class Boss3:
    def __init__(self):
        self.zdrowie = 100

    def atak(self, taktyka):
        if taktyka == 1:
            return random.randint(10, 15)
        elif taktyka == 2:
            return random.randint(5, 20)
        elif taktyka == 3:
            return random.randint(1, 25)

    
