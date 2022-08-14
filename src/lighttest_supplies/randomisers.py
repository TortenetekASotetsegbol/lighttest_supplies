'''
funkciók gyűjteménye, amik különböző típusú listákból adnak vissza véletlenszerűen egy elemet
'''
import json
import random
from random import randrange
from random import choice, choices


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
