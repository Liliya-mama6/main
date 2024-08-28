class Animal:
    def __init__(self, name):
        self.name = name

    alive = True
    fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible == True:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print('Животные ниего другого не едят')


class Plant:
    def __init__(self, name):
        self.name = name

    edible = False


class Mammal(Animal):
    edible = True


class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant) == True:
            if food.edible == True:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        elif isinstance(food, Animal) == True:#тут захотелось пошутить))))))
            if isinstance(food, Mammal) == True and food.alive == True:
                print(f'{self.name} съел {food.name}')
                self.fed = True
                food.alive = False
            elif (isinstance(food, Mammal) == True or isinstance(food, Predator) == True) and food.alive == False:
                print(f'{self.name} попытался съесть труп животного {food.name}')
                self.alive = False
            elif isinstance(food, Predator) == True:
                print(f'Из-за сильного голода погли оба хищника и {self.name} и {food.name}')
                self.alive = False
                food.alive = False
        else:
            print('Хищники такого не едят')


class Fruit(Plant):
    edible = True


class Flower(Plant):
    edible = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
