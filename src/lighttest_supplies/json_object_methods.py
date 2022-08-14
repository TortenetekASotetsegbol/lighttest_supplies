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
    except TypeError(json):
        print(
            f'find_value_in_json(json_object: json, key: str, value): The given object is not a json object. Given object type: {type(json_object)}')
    return False


def not_empty_jsonarray(jsonarray: [json]):
    if len(jsonarray) > 0:
        return True
    else:
        return False
