# _________________ Block of Libraries:
import random
import math

# _________________ Block of Classes:
class Hero:
    'Это класс персонажа'
    def __init__(self, level, intelegence, agity, strenght, charm, name):
        self.level = level
        self.intelegence = intelegence
        self.agity = agity
        self.strenght = strenght
        self.charm = charm
        self.name = name

        health = strenght * 24
        #defence =

    # Experience:
    def getLevel(self):
        return self.level

    # Intellegence:
    def getIntel(self):
        return self.intelegence

    # Agity:
    def getAgity(self):
        return self.agity

    # Strenght:
    def getStrenght(self):
        return self.strenght

    # Charm:
    def getCharm(self):
        return self.charm

    def getName(self):
        return self.name

    # Health сила * 24
    def getHealth(self):
        return self.health

    # Defence ловкость * 0.125

    # Mana интеллект * 12

    # Сharisma = charm * 0.5 + intelegence * 0.2 + current_health / healt


# _________________ Block of Variables:
n = 10


# _________________ Block of Functions:
def roll_the_dice():
    return random.randint(1, 6)

#def show_the_map():

def command():
    input("<<")

def help_function():
    print("M - вывод карты на экран, если подзабыл куда двигаться", '\n')
    print("H - вывод подсказки на экран", '\n')
    print("I - содержимое твоего инвентаря", '\n')
    print("P - характеристики твоего персонажа", '\n')
    print("gN - переход на другое поле, cевернее текущего", '\n')
    print("gS - переход на другое поле, южнее текущего", '\n')
    print("gW - переход на другое поле, западнее текущего", '\n')
    print("gE - переход на другое поле, восточнее текущего", '\n')
    print("T - время до вторжения", '\n')
    print("S - завести разговор", '\n')
    print("A - атаковать", '\n')
    print("R - бросить кубик", '\n')
    print("Q - выход из игры", '\n')

def map_fucntion():
    print(
    "Карта мира (вид сверху):", '\n'
    " ___________________________________________________", '\n',
    "| 2A    | 1A       | ~ ~ ~  | 1B       | 2B         |", '\n',
    "|       |__________|  ~ ~   |__________|            |", '\n',
    "|       /          | river  |           \           |", '\n',
    "|      /           | ~ ~ ~  |            \          |", '\n',
    "|_____/            |  ~ ~   |             \_________|", '\n',
    "| 3A  |            |________|             | 3B      |", '\n',
    "|     |     A      | Bridge |   B         |         |", '\n',
    "|     |   TOWER    |________| TOWER       |         |", '\n',
    "|_____|            |        |             |_________|", '\n',
    "| 4A   \           |  ~ ~   |            / 4B       |", '\n',
    "|       \          | river  |           /           |", '\n',
    "|        \_________|  ~ ~   |__________/            |", '\n',
    "|        | 5A      | ~ ~ ~  | 5B       |            |", '\n',
    "|________|_________|________|__________|____________|", '\n')


# _________________ Legend:
print("Мир: Фентези чистой воды", '\n' "Жанр: текстовая  RPG", '\n')

print("Хочешь посмотреть карту мира?  (отвечай в формате Y/N или y/n)")
if  input() == ('Y' or 'y'):
    print(".... Вы находитесь на мосту между двух башен", '\n'
          "в этой главе вам нужно подготовиться и отбить вторжение....", '\n' "Карта мира (вид сверху):", '\n'
          " ___________________________________________________",  '\n',
          "| 2A    | 1A       | ~ ~ ~  | 1B       | 2B         |", '\n',
          "|       |__________|  ~ ~   |__________|            |", '\n',
          "|       /          | river  |           \           |", '\n',
          "|      /           | ~ ~ ~  |            \          |", '\n',
          "|_____/            |  ~ ~   |             \_________|", '\n',
          "| 3A  |            |________|             | 3B      |", '\n',
          "|     |     A      | Bridge |   B         |         |", '\n',
          "|     |   TOWER    |________| TOWER       |         |", '\n',
          "|_____|            |        |             |_________|", '\n',
          "| 4A   \           |  ~ ~   |            / 4B       |", '\n',
          "|       \          | river  |           /           |", '\n',
          "|        \_________|  ~ ~   |__________/            |", '\n',
          "|        | 5A      | ~ ~ ~  | 5B       |            |", '\n',
          "|________|_________|________|__________|____________|", '\n')
else:
    print("Действительно, кому нужны старые карты....")

print("Нужна ли тебе подсказка? (отвечай в формате Y/N или y/n)")
if input() == ('Y' or 'y'):
    print("Все управление в этой игре осуществляется через консоль", '\n')
    print("После символа << вводи свою команду. Они бывают такими:", '\n')
    print("M - вывод карты на экран, если подзабыл куда двигаться", '\n')
    print("H - вывод подсказки на экран", '\n')
    print("I - содержимое твоего инвентаря", '\n')
    print("P - характеристики твоего персонажа", '\n')
    print("gN - переход на другое поле, cевернее текущего", '\n')
    print("gS - переход на другое поле, южнее текущего", '\n')
    print("gW - переход на другое поле, западнее текущего", '\n')
    print("gE - переход на другое поле, восточнее текущего", '\n')
    print("L - осмотреться", '\n')
    print("T - время до вторжения", '\n')
    print("S - завести разговор", '\n')
    print("A - атаковать", '\n')
    print("R - бросить кубик", '\n')
    print("Q - выход из игры", '\n')

else:
    print("Подсказки это для слабоков!")

print("Хочешь создать своего персонажа?  (отвечай в формате Y/N или y/n)")
if input() == ('Y' or 'y'):
    name = input("имя: ")
    main_hero = Hero(1, 0, 0, 0, 0, name)

    print(main_hero.name, ", твой уровень сейчас", main_hero.getLevel() )
    print("Давай распределим твои навыки. Их четыре: интеллект, ловкость, сила, обаяние:")
    print("1. интеллект, позволяет тебе собирать новые устройства, использовать новые предметы")
    print("2. ловкость, повышает твою скорострельность и уворачиваемость")
    print("3. сила, увеличивает твою грузоподъемность, и ты сможешь пользоваться тяжелой броней и оружием ")
    print("4. обаяние, позволяет привлекать новых персонажей в свой отряд и эффективнее вести диалоги")
    print("у тебя есть", 10 * main_hero.getLevel(), "очков для распределения навыков")

    main_hero.intelegence = int(input("Сколько из них потратим на интеллект?"))
    print("у тебя осталось", n * main_hero.getLevel() - main_hero.intelegence, "очков")
    main_hero.agity = int(input("Сколько из них потратим на ловкость?"))
    print("у тебя осталось", n * main_hero.getLevel() - main_hero.intelegence - main_hero.agity, "очков")
    main_hero.strenght = int(input("Сколько из них потратим на cилу?"))
    print("у тебя осталось", n * main_hero.getLevel() - main_hero.intelegence - main_hero.agity - main_hero.strenght, "очков")
    main_hero.charm = int(input("Сколько из них потратим на обаяние?"))

    # Проверка анти-чит:
    sum = main_hero.intelegence + main_hero.agity + main_hero.strenght + main_hero.charm
    main_hero.intelegence = main_hero.intelegence / sum * n
    main_hero.agity = main_hero.agity / sum * n
    main_hero.strenght = main_hero.strenght / sum * n
    main_hero.charm = main_hero.charm / sum * n

else:
    name = "Nick"
    main_hero = Hero(1, 2, 2, 2, 2, name)

print("Поздравляю персонаж", name, "создан!")
print("Твои характеристики:")
print("ИНТЕЛЛЕКТ", "%.2f" % (main_hero.getIntel()))
print("ЛОВКОСТЬ", "%.2f" % (main_hero.getAgity()))
print("СИЛА", "%.2f" % (main_hero.getStrenght()))
print("ОБАЯНИЕ", "%.2f" % (main_hero.getCharm()))


chance = input("Ночной сумрак поглощает пространство вокруг тебя...ты стоишь перед дверью в подземелье готов ли ты открыть ее?")

if chance == 'да' or chance == 'ДА' or chance == 'Да':
    print("дверь закрылась за тобой зловеще и со скрипом...")
elif chance == 'нет' or chance == 'НЕТ' or chance == 'Нет':
    print("твоего персонажа сьели неизвестные существа...")
else:
    print("Продолжение следует... ")

# _________________  Game:
# Tower A - тут арсенал, а значит можно вооружиться
# Tower B - тут казарма, а значит можно взять помощника
# 1A -
# 2A -
# 3A - дорога в Западную Башню. торговец, у него можно купить хорошее оружее
# 4A -
# 5A - таверна, тут те кто обидел торговца
# 1B - северное болото, тут локальный монстр
# 2B - заболоченная местность, можно помочь девушке
# 3B - дорога в Восточную Башню.
# 4B -
# 5B - песчанная пустыня, тут живет маг-отшельник у которого можно выучить заклинания
#

while command != "Q":
    command = input("<<")
    if command == 'H':
        help_function()
    elif command == 'M':
        map_fucntion()
    elif command == 'gW':
        print("Башня A - арсенал")
    elif command == 'gE':
        print("Башня Б - казарма")
    elif command == 'R':
        print(roll_the_dice())
    else:
        print("продолжение следует")


