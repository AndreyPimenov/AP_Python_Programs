#Домашнее задание к лекции 1.5 «Классы и их применение в Python» Вы приехали помогать на ферму к Бабушке =) и видите вокруг себя множество разных животных:
'''
гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
утку "Кряква"

Со всеми животными вам необходимо как-то взаимодействовать:
кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
'''
#Задача №1. Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
class Livestock:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  #имя вес
  def __str__(self):
    return '{} - {}'.format(self.name, self.weight) 

  #кормить:
  def feed(self):
    self.food = 'yes'

  #различать по голосам:
  def scream(self):
    self.sound = 'scream' 

  #взаимодействовать:
  def interaction(self):
    self.interact = ''  
  

  #суммарный вес:
  def summa (self, other):
    return ( self.weight + other.weight) 

  #самого тяжелого в классе: 
  def heavier(self, other):
    if self.weight > other.weight:
      return self.name
    else:
      return other.name  

  def __repr__(self):
    return self.weight

  def __retr__(self):
    return self.name + " " +self.weight

class Gouse(Livestock):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'Ga-Ga-Ga'
    self.interact = 'pick_up_eggs'

class Cow(Livestock):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'Moo-Oo-Oo'
    self.interact = 'milk'

class Sheep(Livestock):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'Be-Ee-Ee'
    self.interact = 'cut'

class Chiken(Livestock):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'Koood-Daakh-Koood-Daakh'
    self.interact = 'pick_up_eggs'

class Goat(Livestock):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'Ea-ea-ea'
    self.interact = 'milk'

class Duck(Livestock):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'Kria-Kria-Kria'
    self.interact = 'pick_up_eggs'

# Задача №2. Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

gouse_0 = Gouse('Beluy', 5) 
gouse_1 = Gouse('Seruy', 6)
cow_0 = Cow('Manka', 450)
sheep_0 = Sheep('Barashek', 60)
sheep_1 = Sheep('Kudriavy', 80)
chiken_0 = Chiken('Ko-Ko', 2)
chiken_1 = Chiken('Kokoreky', 3)
goat_0 = Goat('Roga', 36)
goat_1 = Goat('Koputa', 40)
duck_0 = Duck('Kryakva', 3)

print(gouse_0.__dict__)
print(gouse_1.__dict__)
print(cow_0.__dict__)
print(sheep_0.__dict__)
print(sheep_1.__dict__)
print(chiken_0.__dict__)
print(chiken_1.__dict__)
print(goat_0.__dict__)
print(goat_1.__dict__)
print(duck_0.__dict__)

#Задача №3. У каждого животного должно быть определено имя(self.name) и вес(self.weight).Необходимо посчитать общий вес всех животных(экземпляров класса); Вывести название самого тяжелого животного.

#общий вес животных в своем классе:
print(Gouse.summa(gouse_0, gouse_1))
print(Sheep.summa(sheep_0, sheep_1))
print(Chiken.summa(chiken_0, chiken_1))
print(Goat.summa(goat_0, goat_1))

# поиск самых тяжелых животных в своем классе:
print(Gouse.heavier(gouse_0, gouse_1))
print(Sheep.heavier(sheep_0, sheep_1))
print(Chiken.heavier(chiken_0, chiken_1))
print(Goat.heavier(goat_0, goat_1))
