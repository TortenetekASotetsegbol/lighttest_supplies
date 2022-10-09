import json


def find_value_in_array(jsonarray: [json], key: str, value):
    '''
    ellenőrzi, hogy a megadott array json objektumai közül bármelyik tartalmazza-e a keresett mező megadott értékét

    :param jsonarray: az a lista, ami tartalmazza az átnézendő objektumokat
    :param key: az ellenőrzendő mező megnevezése
    :param value: a keresett érték
    :return: True, ha megtalálta az értéket. False, ha nem vagy a a kapott objektum enm egy lista
    '''
    try:
        for json in jsonarray:
            if json[key] == value:
                return True
    except TypeError(list):
        return False

    return False


def find_value_in_json(json_object: json, key: str, value):
    try:
        if json_object[key] == value:
            return True
    except TypeError(dict):
        print(
            f'find_value_in_json(json_object: json, key: str, value): The given object is not a json object. Given object type: {type(json_object)}')
    return False


def not_empty_jsonarray(jsonarray: [json], raise_error=False):
    '''
    check whether a list is empty or not.
    :param jsonarray: an unknown sized jsonarray or list
    :param raise_error:it it true and the jsonarray is empty or not a list at all, raise error
    :return: true, if the list's size is 1 or greater
    '''
    if len(jsonarray) > 0 and type(jsonarray) == list:
        return True
    else:
        if raise_error:
            raise Exception(f'this object is not a list or empty. The given list: {jsonarray}')
        return False


def find_json_in_array(jsonarray: list, key: str, value):
    for json in jsonarray:
        if json[key] == value:
            return json

    return None


def fill_json(json_obj: dict, int_values=None, str_values=None, bool_values=None):
    if type(json_obj) != dict:
        raise TypeError("it is not a dict object, you fool!")
    for key, value in json_obj.items():
        if type(value) == int:
            json_obj[key] = int_values
        if type(value) == str:
            json_obj[key] = str_values
        if type(value) == bool:
            json_obj[key] = bool_values
        if type(value) == dict:
            json_randomiser(value)

    return json_obj
