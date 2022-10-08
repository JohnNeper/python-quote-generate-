import random
import json

quotes = ["ecoutez moi", "Monsieur John","de me prier", "d'arreter de voler", "de la nourriture","john est de retour"]
characters = ["alvin","checkmunks","john", "ripple","neper","johnny"]

def read_values_from_json_file():
    return
    

def get_random_item(my_list):
    rand_numb = random.randint(0,len(my_list)-1)
    item = my_list[rand_numb]
    return item

def capitalize(worlds):
    for world in worlds:
        world.capitalize()

def message(characters, quotes):
    capitalize(characters)
    capitalize(quotes)
    return "{} a dit: {}".format(characters,quotes)

user = input("taper 'ok' pour avoir une autre citation ou non pour quitter")
while user !="non":
    print(message(get_random_item(characters),get_random_item(quotes)))
    break

    