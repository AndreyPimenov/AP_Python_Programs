# _________________ Block of Libraries:
import random
import math
import time


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
        # defence =

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


class Location:
    'Это класс Локация'

    def __init__(self, location):
        self.location = location


# _________________ Block of Variables:
n = 10  # мультипликтаор
position_flag = "Bridge"  # начальная позиция
time_flag = " "  # начальное значение флага дня
command = " "
time_now = 12  # полдень первого дня


# _________________ Block of Functions:

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


def move_function(direction, position_flag_local, time2move):
    # -------- MAP Graph:
    #            bridge (Home position)
    #            /   \
    #       Tower A  Tower B
    #         |         |
    #        3A         3B
    #       /   \      /   \
    #      2A   4A    2B   4B
    #      |     |     |    |
    #      1A    5A   1B    5B
    # -------------------------
    print("Ты находишься в локации", position_flag_local)

    if position_flag_local == "Bridge":
        print("МОСТ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            time2move = time2move + 0.25
            position_flag_local = "Tower A"
        elif direction == "gE":
            time2move = time2move + 0.25
            position_flag_local = "Tower B"
        elif direction == "gN":
            position_flag_local = "Bridge"
            print("тут северная река. хода нет")
        elif direction == "gS":
            position_flag_local = "Bridge"
            print("тут южная река. хода нет")
        else:
            print("ER1 - Какая-то ошибка ввода")

    elif position_flag_local == "Tower A":
        print("БАШНЯ А - АРСЕНАЛ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            time2move = time2move + 0.5
            position_flag_local = "A3"
        elif direction == "gE":
            time2move = time2move + 0.25
            position_flag_local = "Bridge"
        elif direction == "gN":
            position_flag_local = "Tower A"
            print("чтобы попасть в A1 нужно пройти через A3, а потом A2")
        elif direction == "gS":
            position_flag_local = "Tower A"
            print("чтобы попасть в A5 нужно пройти через A3, а потом A4")
        else:
            print("ER2 -Какая-то ошибка ввода")

    elif position_flag_local == "Tower B":
        print("БАШНЯ Б - КАЗАРМА", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            time2move = time2move + 0.25
            position_flag_local = "Bridge"
        elif direction == "gE":
            time2move = time2move + 0.5
            position_flag_local = "B3"
        elif direction == "gN":
            position_flag_local = "Tower B"
            print("чтобы попасть в B1 нужно пройти через B3, а потом B2")
        elif direction == "gS":
            position_flag_local = "Tower B"
            print("чтобы попасть в B5 нужно пройти через B3, а потом B4")
        else:
            print("ER3 -Какая-то ошибка ввода")

    elif position_flag_local == "A3":
        print("А3 - ТОРГОВЕЦ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "A3"
            print("туда хода нету...")
        elif direction == "gE":
            time2move = time2move + 0.5
            position_flag_local = "Tower A"
            print("возвращаешься в башню А")
        elif direction == "gN":
            position_flag_local = "A2"
            print("А2 - ЛЕС СЕВЕРНЫЙ - ЛАГЕРЬ ЛЕСОРУБОВ", '\n')
            time2move = time2move + 1
        elif direction == "gS":
            position_flag_local = "A4"
            print("А4 - ПОЛЕ ЗАПАДНОЕ", '\n')
            time2move = time2move + 1
        else:
            print("ER4 -Какая-то ошибка ввода")

    elif position_flag_local == "A2":
        print("А2 - ЛЕС СЕВЕРНЫЙ - ЛАГЕРЬ ЛЕСОРУБОВ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "A2"
            print("туда хода нету... (граница карты)")
        elif direction == "gE":
            position_flag_local = "A1"
            print("ты заходишь в чащу северного леса...")
            time2move = time2move + 2
        elif direction == "gN":
            position_flag_local = "A2"
            print("туда хода нету...(граница карты)")
        elif direction == "gS":
            position_flag_local = "A3"
            print("возвращаешься к торговцу", '\n')
            time2move = time2move + 1
        else:
            print("ER5 -Какая-то ошибка ввода")

    elif position_flag_local == "A1":
        print("А1 - ЛЕС СЕВЕРНЫЙ - ЧАЩА", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "A2"
            print("возвращаешься в более редкий лес")
            time2move = time2move + 2
        elif direction == "gE":
            position_flag_local = "A1"
            print("хода нет... (тут течет река)")
        elif direction == "gN":
            position_flag_local = "A1"
            print("хода нет... (граница карты)", '\n')
        elif direction == "gS":
            position_flag_local = "A1"
            print("хода нет... ", '\n')
        else:
            print("ER6 -Какая-то ошибка ввода")

    elif position_flag_local == "A4":
        print("А4 - ПОЛЕ ЗАПАДНОЕ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "A4"
            print("туда хода нету...(граница карты)")
        elif direction == "gE":
            position_flag_local = "A5"
            print("идешь на мельницу...")
            time2move = time2move + 1
        elif direction == "gN":
            position_flag_local = "A3"
            print("возвращение к торговцу...", '\n')
            time2move = time2move + 1
        elif direction == "gS":
            position_flag_local = "A4"
            print("туда хода нету...(граница карты)")
        else:
            print("ER7 -Какая-то ошибка ввода")

    elif position_flag_local == "A5":
        print("А5 - МЕЛЬНИЦА", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "A4"
            print("возвращаешься на поле")
            time2move = time2move + 1
        elif direction == "gE":
            position_flag_local = "A5"
            print("туда хода нету...(река)")
        elif direction == "gN":
            position_flag_local = "A5"
            print("туда хода нету...")
        elif direction == "gS":
            position_flag_local = "A5"
            print("туда хода нету...(граница карты)")
        else:
            print("ER8 -Какая-то ошибка ввода")

    elif position_flag_local == "B3":
        print("B3 - ДОРОГА К ВОСТОЧНОЙ БАШНЕ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "Tower B"
            print("возвращаешься в башню Б...")
            time2move = time2move + 0.5
        elif direction == "gE":
            position_flag_local = "B3"
            print("туда хода нету...")
        elif direction == "gN":
            position_flag_local = "B2"
            print("B2 - болота сверные", '\n')
            time2move = time2move + 2
        elif direction == "gS":
            position_flag_local = "B4"
            print("B4 - ПОЛЕ ВОСТОЧНОЕ", '\n')
            time2move = time2move + 2
        else:
            print("ER9 -Какая-то ошибка ввода")

    elif position_flag_local == "B2":
        print("B2 - СЕВЕРНЫЕ БОЛОТА", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "B1"
            print("дальше в болота...")
            time2move = time2move + 2
        elif direction == "gE":
            position_flag_local = "B2"
            print("туда хода нет... (граница карты)")
        elif direction == "gN":
            position_flag_local = "B2"
            print("туда хода нет... (граница карты)")
        elif direction == "gS":
            position_flag_local = "B3"
            print("Возвращаешься в B3", '\n')
            time2move = time2move + 2
        else:
            print("ER10 -Какая-то ошибка ввода")

    elif position_flag_local == "B1":
        print("B1 - ЛОГОВО НА БОЛОТАХ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "B1"
            print("туда хода нету...(река)")
        elif direction == "gE":
            position_flag_local = "B2"
            print("возвращаешься в B2")
            time2move = time2move + 2
        elif direction == "gN":
            position_flag_local = "B1"
            print("туда хода нет...(граница карты)", '\n')
        elif direction == "gS":
            position_flag_local = "B1"
            print("туда хода нет...", '\n')
        else:
            print("ER11 -Какая-то ошибка ввода")

    elif position_flag_local == "B4":
        print("B4 - ЮЖНЫЙ ТРАКТ", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "B5"
            print("Попадаешь к магу пустыннику...")
            time2move = time2move + 2
        elif direction == "gE":
            position_flag_local = "B4"
            print("туда хода нет...")
        elif direction == "gN":
            position_flag_local = "B3"
            print("возвращаешься в B3", '\n')
            time2move = time2move + 2
        elif direction == "gS":
            position_flag_local = "B3"
            print("туда хода нет...(граница карты)", '\n')
        else:
            print("ER12 -Какая-то ошибка ввода")

    elif position_flag_local == "B5":
        print("B5 - МАГ ПУСТЫННИК", '\n')
        # тут можно добавить описание локации
        if direction == "gW":
            position_flag_local = "B5"
            print("туда хода нету...(река)")
        elif direction == "gE":
            position_flag_local = "B4"
            print("возвращаешься в B4")
            time2move = time2move + 2
        elif direction == "gN":
            position_flag_local = "B5"
            print("туда хода нет...", '\n')
        elif direction == "gS":
            position_flag_local = "B5"
            print("Туда хода нет...(граница карты)", '\n')
        else:
            print("ER13 -Какая-то ошибка ввода")

    else:
        print("ошибка")

    return position_flag_local, time2move


def map_function():
    print(".... Ты находишься: ", position_flag , '\n'
                                                      "в этой главе тебе нужно подготовиться и отбить вторжение....",
          '\n'

          "навигация по миру осуществляется:", '\n',
          "          gN         ", '\n',
          "         / \         ", '\n',
          "          |          ", '\n',
          "gW  <-----|----->  gE", '\n',
          "          |          ", '\n',
          "         \ /         ", '\n',
          "          gS         ", '\n',
          "Карта мира (вид сверху):", '\n'
                                      " ___________________________________________________", '\n',
          "| A2    | A1       | ~ ~ ~  | B1       | B2         |", '\n',
          "|       |__________|  ~ ~   |__________|            |", '\n',
          "|       /          | river  |           \           |", '\n',
          "|      /           | ~ ~ ~  |            \          |", '\n',
          "|_____/            |  ~ ~   |             \_________|", '\n',
          "| A3  |            |________|             | B3      |", '\n',
          "|     |     A      | Bridge |   B         |         |", '\n',
          "|     |   TOWER    |________| TOWER       |         |", '\n',
          "|_____|            |        |             |_________|", '\n',
          "| A4   \           |  ~ ~   |            / B4       |", '\n',
          "|       \          | river  |           /           |", '\n',
          "|        \_________|  ~ ~   |__________/            |", '\n',
          "|        | A5      | ~ ~ ~  | B5       |            |", '\n',
          "|________|_________|________|__________|____________|", '\n')


def roll_the_dice():
    return random.randint(1, 6)


def time_function(time_flag_local):
    DD = time_now // 24
    HH = time_now % 24
    if HH > 20 or HH <= 9:
        time_flag_local = "NIGHT"
    else:
        time_flag_local = "DAY"
    print("День: ", DD, "час: ", HH, "время суток:", time_flag_local)
    return time_flag_local

def person_function():
    print( name, '\n')
    print("Твои характеристики:")
    print("ИНТЕЛЛЕКТ", "%.2f" % (main_hero.getIntel()))
    print("ЛОВКОСТЬ", "%.2f" % (main_hero.getAgity()))
    print("СИЛА", "%.2f" % (main_hero.getStrenght()))
    print("ОБАЯНИЕ", "%.2f" % (main_hero.getCharm()))

def look_around_function():
    if position_flag == "Bridge":
        print('...мост...')
    elif position_flag == "Tower A":
        print('...башня А, в ней арсенал...')
    elif position_flag == "Tower B":
        print('...башня Б, в ней казармы...')
    elif position_flag == "A1":
        print('...A1...')
    elif position_flag == "A2":
        print('...A2...')
    elif position_flag == "A3":
        print('...A3...')
    elif position_flag == "A4":
        print('...A4...')
    elif position_flag == "A5":
        print('...A5...')
    elif position_flag == "B1":
        print('...B1...')
    elif position_flag == "B2":
        print('...B2...')
    elif position_flag == "B3":
        print('...B3...')
    elif position_flag == "B4":
        print('...B4...')
    elif position_flag == "B5":
        print('...B5...')
    else:
        print("...")

# I - инвентарь
# S - начать разговор
# A - атаковать

# _________________ Legend:
print("Мир: Фэнтези чистой воды", '\n' "Жанр: текстовая  RPG", '\n')

print("Хочешь посмотреть карту мира?  (отвечай в формате Y/N или y/n)")
if input() == ('Y' or 'y'):
    print(".... Ты находишься: ", position_flag , '\n'
                                                      "в этой главе тебе нужно подготовиться и отбить вторжение....",
          '\n' "Карта мира (вид сверху):", '\n'
                                           "навигация по миру осуществляется:", '\n',
          "          gN         ", '\n',
          "         / \         ", '\n',
          "          |          ", '\n',
          "gW  <-----|----->  gE", '\n',
          "          |          ", '\n',
          "         \ /         ", '\n',
          "          gS         ", '\n',
          " ___________________________________________________", '\n',
          "| A2    | A1       | ~ ~ ~  | B1       | B2         |", '\n',
          "|       |__________|  ~ ~   |__________|            |", '\n',
          "|       /          | river  |           \           |", '\n',
          "|      /           | ~ ~ ~  |            \          |", '\n',
          "|_____/            |  ~ ~   |             \_________|", '\n',
          "| A3  |            |________|             | B3      |", '\n',
          "|     |     A      | Bridge |   B         |         |", '\n',
          "|     |   TOWER    |________| TOWER       |         |", '\n',
          "|_____|            |        |             |_________|", '\n',
          "| A4   \           |  ~ ~   |            / B4       |", '\n',
          "|       \          | river  |           /           |", '\n',
          "|        \_________|  ~ ~   |__________/            |", '\n',
          "|        | A5      | ~ ~ ~  | B5       |            |", '\n',
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
    print("Подсказки это для слабаков!")

print("Хочешь создать своего персонажа?  (отвечай в формате Y/N или y/n)")
if input() == ('Y' or 'y'):
    name = input("имя: ")
    main_hero = Hero(1, 0, 0, 0, 0, name)

    print(main_hero.name, ", твой уровень сейчас", main_hero.getLevel())
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
    print("у тебя осталось", n * main_hero.getLevel() - main_hero.intelegence - main_hero.agity - main_hero.strenght,
          "очков")
    main_hero.charm = int(input("Сколько из них потратим на обаяние?"))

    # Проверка анти-чит:
    sum = main_hero.intelegence + main_hero.agity + main_hero.strenght + main_hero.charm
    main_hero.intelegence = main_hero.intelegence / sum * n
    main_hero.agity = main_hero.agity / sum * n
    main_hero.strenght = main_hero.strenght / sum * n
    main_hero.charm = main_hero.charm / sum * n

else:
    name = "Noob"
    main_hero = Hero(1, 2, 2, 2, 2, name)

print("Поздравляю персонаж", name, "создан!")
print("Твои характеристики:")
print("ИНТЕЛЛЕКТ", "%.2f" % (main_hero.getIntel()))
print("ЛОВКОСТЬ", "%.2f" % (main_hero.getAgity()))
print("СИЛА", "%.2f" % (main_hero.getStrenght()))
print("ОБАЯНИЕ", "%.2f" % (main_hero.getCharm()))

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

print("игра началась", '\n')
print("5...", '\n')
time.sleep(1)
print("4...", '\n')
time.sleep(1)
print("3...", '\n')
time.sleep(1)
print("2...", '\n')
time.sleep(1)
print("1...", '\n')
time.sleep(1)
print("0...", '\n')
time.sleep(1)
print("Поехали!", '\n')
time.sleep(1)

print(main_hero.name,
      "ты весь мокрый и стоишь на широком мосту между двух огромных башен. Что ты будешь делать? (для подсказкви набери H)")

while command != ("Q" or "q"):
    command = input("<<")
    if command == 'H':
        help_function()
    elif command == "M":
        map_function()
    elif command == 'gW':
        position_flag, time_now = move_function(command, position_flag, time_now)
        print("теперь ты находишься в локации: ", position_flag)
    elif command == 'gE':
        position_flag, time_now = move_function(command, position_flag, time_now)
        print("теперь ты находишься в локации: ", position_flag)
    elif command == 'gN':
        position_flag, time_now = move_function(command, position_flag, time_now)
        print("теперь ты находишься в локации: ", position_flag)
    elif command == 'gS':
        position_flag, time_now = move_function(command, position_flag, time_now)
        print("теперь ты находишься в локации: ", position_flag)
    elif command == 'T':
        time_flag = time_function(time_flag)
    elif command == 'P':
        person_function()
    elif command == 'R':
        print(roll_the_dice())
    elif command == 'L':
        look_around_function()
    else:
        print("продолжение следует")
