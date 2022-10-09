'''
funkciók gyűjteménye, amik különböző típusú listákból adnak vissza véletlenszerűen egy elemet
'''
import json
import random
from random import randrange
from random import choice, choices
from lighttest_supplies.json_object_methods import find_value_in_json


def rand_listelem(list: list):
    tuple_list = tuple(list)

    return tuple_list[randrange(len(tuple_list))]


def rand_val_from_jsonarray(jsonarray: [json], key: str):
    '''

    :param jsonarray: egy lista, ami json objektumokat tartalmaz
    :param key: a véletlenszerűen kiválasztott json objektum egy mezőjének a neve, aminek vissza akrod kapni az értékét
    :return: a megadott key mezőhöz tartozó value
    '''
    val = rand_listelem(jsonarray)[key]
    return val


def rand_dict_key(dictinoray: dict, keys_number: int = 1):
    '''

    :param dictinoray: az a dictinoray, amiből ki kell választani  k darab elemet
    :param keys_number: a véletlenszerűen kiválasztani akart elemek száma
    :return: egy lista, ami a kiválsztott elemeket tartalmazza
    '''
    keys = random.choices(list(dictinoray.keys()), k=keys_number)
    return keys


def rand_bool(true_ratio_percent: int = 50):
    '''

    :return: True or False value, randomly
    '''
    if true_ratio_percent == 50:
        return random.choice([True, False])
    else:
        true_table = tuple(True for pecentige in range(true_ratio_percent))
        false_table = tuple(False for pecentige in range(100 - true_ratio_percent))
        return random.choice(true_table + false_table)


def json_randomiser(json_obj: dict, different_true_ratio: dict = {}):
    if type(json_obj) != dict:
        raise TypeError("it is not a dict object, you fool!")
    for key, value in json_obj.items():
        if type(value) == int:
            json_obj[key] = randrange(20)
        elif type(value) == str:
            json_obj[key] = f'generált{randrange(20)}'
        elif type(value) == bool and different_true_ratio == {}:
            json_obj[key] = rand_bool()
        elif type(value) == bool and different_true_ratio != {}:
            if key in different_true_ratio.keys():
                json_obj[key] = rand_bool(true_ratio_percent=different_true_ratio[key])
            else:
                json_obj[key] = rand_bool()
        elif type(value) == dict:
            json_randomiser(value)

    return json_obj
