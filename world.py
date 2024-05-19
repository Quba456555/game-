import random
from przeciwnik import BagnistaZaba1, BagnistaZaba2

class World:
    def __init__(self):
        self.enemies = []

    def generate_enemy(self):
        if random.choice([True, False]):
            enemy = BagnistaZaba1()
        else:
            enemy = BagnistaZaba2()
        self.enemies.append(enemy)

    def print_enemies(self):
        for i, enemy in enumerate(self.enemies, start=1):
            print(f"{i}. {enemy.name} ({enemy.character.health} HP)")

    def remove_defeated_enemies(self):
        self.enemies = [enemy for enemy in self.enemies if enemy.is_alive()]

    def generate_location(self):
        location_names = ["Las", "Góry", "Jaskinia", "Wioska"]
        name = random.choice(location_names)
        description = f"Jesteś teraz w lokacji: {name}"
        return {
            "name": name,
            "description": description
        }

    def enter_location(self, location, player):
        print(location["description"])
        self.generate_enemy()
        if self.enemies:
            print("Spotkałeś wroga!")
            battle = Battle(player, self)
            battle.start_battle()

#=======================================================

class Battle:
    def __init__(self, player, world):
        self.player = player
        self.world = world

    def start_battle(self):
        while self.player.is_alive() and self.world.enemies:
            self.world.print_enemies()
            choice = input("wcisnij 1 by zaczac walke 'q' by uciec: ")
            if choice.lower() == 'q':
                print("Uciekasz z walki!")
                break

            try:
                enemy_index = int(choice) - 1
                enemy = self.world.enemies[enemy_index]
            except (ValueError, IndexError):
                print("Niepoprawny wybór!")
                continue

            action = input("Wybierz akcję: 1. Atakuj 2. Unik 3. Użyj szóstego zmysłu 4. Użyj eliksiru leczenia: ")
            if action == '1':
                self.player.attack_enemy(enemy)
                print(f"Atakujesz {enemy.name}!")
            elif action == '2':
                if random.random() < 0.5:
                    print("Udało ci się uniknąć ataku!")
                    continue
                else:
                    print("Nie udało ci się uniknąć ataku.")
            elif action == '3':
                if self.player.use_sixth_sense():
                    print("Używasz szóstego zmysłu i unikasz następnego ataku!")
                    continue
                else:
                    print("Już użyłeś szóstego zmysłu w tej walce!")
            elif action == '4':
                if self.player.use_healing_potion():
                    print("Używasz eliksiru leczenia i odzyskujesz zdrowie!")
                else:
                    print("Nie masz eliksiru leczenia!")

            if enemy.is_alive():
                enemy.attack_player(self.player)
                print(f"{enemy.name} atakuje cię!")
            else:
                print(f"Pokonałeś {enemy.name}!")
                self.world.remove_defeated_enemies()

        if not self.player.is_alive():
            print("Zostałeś pokonany! ")
        elif not self.world.enemies:
            print("Pokonałeś wszystkich wrogów w tej lokacji!")
