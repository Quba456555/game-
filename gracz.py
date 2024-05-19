
import random 
class Gracz:
    def __init__(self, poziom, wygrane_poziomy, zdrowie, zloto, mana):
        self.poziom = poziom
        self.wygrane_poziomy = wygrane_poziomy
        self.zdrowie = zdrowie
        self.zloto = zloto
        self.mana = mana
        self.ekwipunek = ekwipunek


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

class Character2:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} został pokonany!")

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.take_damage(damage)
        print(f"{self.name} atakuje {enemy.name} za {damage} obrażeń!")

class Player:
    def __init__(self,  health=100, attack=10, defense=5):
        self.character = Character(health, attack, defense)
        self.ekwipunek = ["6 zmysł", "Eliksir leczenia"] 
        self.sixth_sense_used = False
        
        
    def is_alive(self):
        return self.character.health > 0

    def take_damage(self, damage):
        self.character.take_damage(damage)

    def attack_enemy(self, enemy):
        self.character.attack_enemy(enemy)

    def use_healing_potion(self):
        for przedmiot in self.ekwipunek:
            if przedmiot == "Eliksir leczenia":
                self.character.health += 50
                self.ekwipunek.remove(przedmiot)
                return True
        return False

    def use_sixth_sense(self):
        if not self.sixth_sense_used:
            self.sixth_sense_used = True
            return True
        return False

    def display_inventory(self):
        print("Twój aktualny ekwipunek:Miecz")
        for przedmiot in self.ekwipunek:
            print(przedmiot)

    
class Nazgul(Character2):
    def __init__(self, name, health, attack, defense, weapon):
        super().__init__(name, health, attack, defense)
        self.weapon = weapon

    def use_weapon(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.take_damage(damage)
        print(f"{self.name} z użyciem {self.weapon} atakuje {enemy.name} za {damage} obrażeń!")


class Player2(Character2):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def encounter_nazgul(self, nazgul):
        print(f"Na drodze {self.name}a pojawia się groźny {nazgul.name}!")
        while nazgul.health > 0 and self.health > 0:
            action = input("Co chcesz zrobić? (atakuj/leczenie)")
            if action == "atakuj":
                self.attack_enemy(nazgul)
                if nazgul.health > 0:
                    nazgul.use_weapon(self)
            elif action == "leczenie":
                self.lecz()
                nazgul.use_weapon(self)
            else:
                print("Nieprawidłowa akcja! Potykasz się i tracisz swoją turę.")
                nazgul.use_weapon(self)

    def lecz(self):
        amount = random.randint(10, 20)
        self.health = min(100, self.health + amount)
        print(f"{self.name} leczy się, odzyskując {amount} punktów życia.")
