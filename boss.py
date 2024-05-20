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

#============================================================================

class ElderRing:
    def __init__(self, name: str, effect: str, material: str) -> None:
        self.name = name
        self.effect = effect
        self.material = material

    def activate(self):
        print(f"Aktuwacja {self.name}. Efekt: {self.effect}")

    def change_material(self, new_material: str):
        print(f"Zmiana materiału {self.name} na: {new_material}")
        self.material = new_material


class ArchmageHat:
    def __init__(self, name: str, type: str, power: str) -> None:
        self.name = name
        self.type = type
        self.power = power

    def cover(self):
        print(f"{self.name} zapewnia ochronę przed czarami wroga!")

    def change_power(self, new_power: str):
        print(f"Zmiana mocy {self.name} na: {new_power}")
        self.power = new_power


class MysticShield:
    def __init__(self, name: str, material: str, enchantment: str) -> None:
        self.name = name
        self.material = material
        self.enchantment = enchantment

    def defend(self):
        print(f"{self.name} oferuje doskonałą ochronę!")

    def change_enchantment(self, new_enchantment: str):
        print(f"Zmiana zaklęcia {self.name} na: {new_enchantment}")
        self.enchantment = new_enchantment


class SacredStaff:
    def __init__(self, name: str, wood: str, power: int) -> None:
        self.name = name
        self.wood = wood
        self.power = power

    def cast_spell(self):
        print(f"{self.name} wzmacnia moc zaklęć!")

    def change_wood(self, new_wood: str):
        print(f"Zmiana drewna {self.name} na: {new_wood}")
        self.wood = new_wood


class MysticAmulet:
    def __init__(self, name: str, effect: str, material: str) -> None:
        self.name = name
        self.effect = effect
        self.material = material

    def activate(self):
        print(f"Aktywacja {self.name}. Efekt: {self.effect}")

    def change_material(self, new_material: str):
        print(f"Zmiana materiału {self.name} na: {new_material}")
        self.material = new_material


# Creating magical items
elder_ring = ElderRing(name="Pierścień Mądrości", effect="Nadaje niezniszczalność", material="Platyna")
archmage_hat = ArchmageHat(name="Kapelusz Mistrzowski", type="Arcy", power="Ochrona przed siłami ciemności")
mystic_shield = MysticShield(name="Tarcza Wartości", material="Mithril", enchantment="Absorpcja zaklęć")
sacred_staff = SacredStaff(name="Laska Oświecenia", wood="Dębina", power=100)
mystic_amulet = MysticAmulet(name="Amulet Arcany", effect="Wzmacnia moc zaklęć", material="Runiczny kamień")

    
