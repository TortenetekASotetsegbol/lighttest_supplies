'''
Ebben a fájlban vannak a különböző dekódoláshoz szükséges methodok
'''
import hashlib
import json


def string_to_md5(string):
    """
    :param string: az a string, amit dekódolni akarsz MD5-be
    :return: a srting MD5 értéke
    """
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def binary_json_to_json(raw_json=None):
    '''
    :param raw_json: egy bináris json object. például bináris, ha a json b'{json object}' felépítésű
    :return: egy json objektumot ad vissza
    '''
    if raw_json == None:
        return None
    else:
        req_payload_str: str = raw_json.decode(encoding="utf-8")
        req_payload: json = json.loads(req_payload_str)
    return req_payload
