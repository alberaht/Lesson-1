
class Hero:
    # Конструктор класса
    def __init__(self, nick, hp, lvl):
        self.nick = nick
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f"{self.nick} base action activate!"

# Обьект
kirito = Hero("Aradus", 100, 1)
asuna = Hero("Asuna", 1000, 101)

print(kirito.nick)
print(kirito.action())
# print(asuna.nick)