"""Доработаем задачи 5-6. Создайте класс-фабрику. 
> Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
> Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Mammals():
    """Млекопитающие"""

    def __init__(self, name, weight, type_food=None):
        self.name = name
        self.weigth = weight
        self.type_food = type_food       
        if self.type_food is None :
            self.type_food = "herbivores"   # травоядные
        else:
            self.type_food = "predator" # хищные
   

    def get_special_info(self):
        return print(f"Mammal {self.name} - {self.type_food}")
    

class Birds():
    """Птицы"""

    def __init__(self, name, weigth, type_motion=None):
        self.name = name
        self.weigth = weigth
        self.type_motion = type_motion
        if self.type_motion is None:
            self.type_motion = "flying"
        else:
            self.type_motion = "not_flying"

    def get_special_info(self):
        return print(f"Bird {self.name} - {self.type_motion}")

class Fish():
    """Рыбы"""

    def __init__(self, name, weigth, living_environment=None):
        self.name = name
        self.weigth = weigth
        self.living_environment = living_environment
        if self.living_environment is None:
            self.living_environment = "river"
        else:
            self.living_environment = "sea"

    def get_special_info(self):
        return print(f"Fish {self.name} - {self.living_environment}")

class Factory():

    def __init__(self, class_name, name, weigth, specifiс=None):
        self.class_name = class_name
        self.name = name
        self.weigth = weigth
        self.specific = specifiс
        self.instance = self.class_name(self.name, self.weigth, self.specific)


if __name__ == "__main__":
    pet_1 = Factory(Mammals, "Rabbit", 2)
    pet_1.instance.get_special_info()
    pet_2 = Factory(Mammals, "Fox", 4, "predator")
    pet_2.instance.get_special_info()
    pet_3 = Factory(Birds, "Parrot", 0.5)
    pet_3.instance.get_special_info()
    pet_4 = Factory(Fish, "Guppy", 0.1)
    pet_4.instance.get_special_info()
        