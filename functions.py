from werkzeug.security import generate_password_hash, check_password_hash
from flask import session as cookies

def passwordHash(password:str):
    return generate_password_hash(password)

def passwordVerify(passHash:str, passUnHashed):
    return check_password_hash(passHash, passUnHashed)

def toJson(objetc):
    json = {}
    for atribute in dir(objetc):
        if not atribute.startswith("_"):
            json[atribute] = getattr(object, atribute)
    return json


def requiredSession(f):
    def decorated(*args, **kwargs):
        if 'idUser' not in cookies:
            raise ValueError('Se requiere una sesión activa para ver la información')
        return f(*args, **kwargs)
    return decorated