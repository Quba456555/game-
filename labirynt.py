import os

class Labirynt:
    
    def __init__(self):
        
        self.labirynt = [
            "#############################",
            "#  S     #       #          #",
            "# #####   ##### # ####### # #",
            "#                       # # #",
            "# #   # ##### ##### ### # # #",
            "# #   #     # #     #   #   #",
            "# #    ## # # # ######### ###",
            "# #           # #         # #",
            "# # # ### #   # # ####### # #",
            "# # # # # #   # #       # # #",
            "# # # #         ####### # # #",
            "# # #       #       #   #   #",
            "# #       # ####### # ##### #",
            "# #         #       #     # #",
            "# #     ### # ####### ### # #",
            "#                           #",
            "###     #####################",
            "#                           #",
            "#     #######################",
            "#                           #",
            "#####################       #",
            "#                           #",
            "#########   #################",
            "#                           #",
            "#######################T#####"
        ]
        
        self.gracz_x, self.gracz_y = 24, 23

    def drukuj_labirynt(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(len(self.labirynt)):
            for x in range(len(self.labirynt[y])):
                if x == self.gracz_x and y == self.gracz_y:
                    print("P", end="")
                else:
                    print(self.labirynt[y][x], end="")
            print()

    def ruch_do(self, x, y):
        if self.labirynt[y][x] != "#":
            self.gracz_x, self.gracz_y = x, y

    def sprawdz_zwyciestwo(self):
        return self.labirynt[self.gracz_y][self.gracz_x] == 'S'

    def start_gry(self):
        
        while True:
            self.drukuj_labirynt()
            if self.sprawdz_zwyciestwo():
                print("Gratulacje! Znalazłeś skarb!")
                print("Przeszedłeś całą grę.")
                break
            
            ruch = input("przejdz labirynt i zdobadz skarb by wygrac gre \n Wprowadź ruch (WASD): ").upper()
            if ruch == "W" and self.gracz_y > 0:
                self.ruch_do(self.gracz_x, self.gracz_y - 1)
            elif ruch == "S" and self.gracz_y < len(self.labirynt) - 1:
                self.ruch_do(self.gracz_x, self.gracz_y + 1)
            elif ruch == "A" and self.gracz_x > 0:
                self.ruch_do(self.gracz_x - 1, self.gracz_y)
            elif ruch == "D" and self.gracz_x < len(self.labirynt[0]) - 1:
                self.ruch_do(self.gracz_x + 1, self.gracz_y)
            else:
                print("Niepoprawny ruch!")
