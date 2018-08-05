# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# - + гусей "Серый" и "Белый"
# - + корову "Маньку"
# - + овец "Барашек" и "Кудрявый"
# - + кур "Ко-Ко" и "Кукареку"
# - + коз "Рога" и "Копыта"
# - + и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# - + кормить
# - + корову и коз доить
# - + овец стричь
# - + собирать яйца у кур, утки и гусей
# - + различать по голосам(коровы мычат, утки крякают и т.д.)

# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование,
# определить общие методы взаимодействия с животными и дополнить их в
# дочерних классах, если потребуется.

# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.
import random

class Animals(object):
    weight = 0
    name = ""

    def feed_animal(self, value):  # метод кормить
        self.weight += (value/1000)
        print("{} по имени {} был покормлен. Теперь его вес = {} кг".format(self.animal, self.name, self.weight))

    def get_voice(self):  # метод который будет определять животное по голосу
        user_input = input("Напишите звук, который Вы сейчас слышали")
        if user_input.lower() == "кря":
            print("Вы слышали утку")
        elif user_input.lower() == "га":
            print("Вы слышали гуся")
        elif user_input.lower() == "ко":
            print("Вы слышали курицу")
        elif user_input.lower() == "му":
            print("Вы слышали корову")
        elif user_input.lower() == "бе":
            print("Вы слышали барана")
        elif user_input.lower() == "ме":
            print("Вы слышали овцу")
        else:
            print("Вы слышали неопознанного зверя. Бегите!")

    def __init__(self, name, weight):
        self.weight = weight
        self.name = name
        all_animal.append({"name":self.name, "weight":self.weight})

class Artiodactyls(Animals):  # корова, коза (парнокопытные)
    animal = ""
    milk = 0

    def get_milk(self):  # доить
        if self.animal == "Корова":
            self.milk += random.randint(10, 20)
        elif self.animal == "Коза":
            self.milk += random.randint(2, 8)
        print("{} по имени {} была подоена. У Вас теперь есть {} литров молока".format(self.animal, self.name, self.milk))

class Sheep(Animals):  # овца
    animal = ""

    def get_cut(self):  # подстригать
        print("{} по имени {} была подстрижена".format(self.animal,self.name))

class Bird(Animals):  # гуси, куры, утка (птицы)

    def get_eggs(self):  # собирать яйца
        self.eggs += random.randint(1, 10)
        print("{} по имени {} собрали яйцо. У Вас теперь есть {} яиц".format(self.animal, self.name, self.eggs))

class Duck(Bird): #утка
    animal = ""
    eggs = 0

class Goose(Bird): #гуси
    animal = ""
    eggs = 0

class Chicken(Bird): #куры
    animal = ""
    eggs = 0

all_animal = []

# гусь Серый
gray = Goose("Серый", 4)
gray.animal = "Гусь"

gray.feed_animal(20)
gray.get_eggs()
gray.get_voice()

# гусь Белый
white = Goose("Белый", 5)
white.animal = "Гусь"

white.feed_animal(50)
white.get_eggs()

# корова Манька
cow = Artiodactyls("Манька", 150)
cow.animal = "Корова"

cow.feed_animal(500)
cow.get_milk()

# овца Барашек
sheep_1 = Sheep("Барашек", 45)
sheep_1.animal = "Овца"

sheep_1.feed_animal(50)
sheep_1.get_cut()

# овца Кудрявый
sheep_2 = Sheep("Кудрявый", 33)
sheep_2.animal = "Овца"

sheep_2.feed_animal(80)
sheep_2.get_cut()

# Курица Ко-Ко
chicken_1 = Chicken("Ко-ко", 2)
chicken_1.animal = "Курица"

chicken_1.feed_animal(30)
chicken_1.get_eggs()

# Курица Кукареку
chicken_2 = Chicken("Кукареку", 1)
chicken_2.animal = "Курица"

chicken_2.feed_animal(40)
chicken_2.get_eggs()

# коза Рога
goat_1 = Artiodactyls("Рога", 40)
goat_1.animal = "Коза"

goat_1.feed_animal(40)
goat_1.get_milk()

# коза Копыта
goat_2 = Artiodactyls("Копыта", 47)
goat_2.animal = "Коза"

goat_2.feed_animal(60)
goat_2.get_milk()

# утка Кряква
duck = Duck("Кряква", 1.5)
duck.animal = "Утка"

duck.feed_animal(60)
duck.get_eggs()

total_weight = 0
max_weight = 0
name_animal = ""
for animal in all_animal:
    total_weight += animal["weight"]
    if animal["weight"] > max_weight:
        max_weight = animal["weight"]
        name_animal = animal["name"]

print("Общий вес всех животных на ферме = {}. Животное с максимальным весом {} его вес {}".format(total_weight,name_animal, max_weight))