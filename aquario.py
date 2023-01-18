# DESEJO COLOCAR TODOS OS ANIMAIS DO TIPO FISH NO TANQUE DE NÚMERO 42

import json

f = open("aquario.json", encoding="utf8")
data_aquario = json.load(f)
animals = data_aquario["data"]

#print(type(animals))
#print(type(data_aquario))

#exemplo usando a função pontual lambda:
#animals_fish = list(filter(lambda animal:(animal["type"] == "fish"), animals))

#Usando uma função e depois chamando ela:
def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False

animals_fish = list(filter(verify_fish, animals))
print(animals_fish)

def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)

def assign_to_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = new_tank_number
        return animal
    return list(map(change_tank_number, animals))

new_aquarium = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquarium)
