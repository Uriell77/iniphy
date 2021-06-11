import sqlite3
import os

DATABASE = 'base.db'


def consulta(tabla):
    conect = sqlite3.connect(DATABASE)
    cur = conect.cursor()
    cur.execute("SELECT * FROM {}".format(tabla))
    a = cur.fetchall()
    conect.close()
    return a


def consultadato(tabla,dato):
    conect = sqlite3.connect(DATABASE)
    cur = conect.cursor()
    if tabla == 'user':
        cur.execute("SELECT * FROM '{0}' WHERE id =='{1}' OR username =='{1}' OR email =='{1}' OR password == '{1}'".format(tabla,dato))
    elif tabla == 'articulos':
        cur.execute("SELECT * FROM '{0}' WHERE id =='{1}' OR nombredelarticulo =='{1}' OR descripcion =='{1}' OR precio == '{1}' OR categoria == '{1}' ".format(tabla,dato))
    a = cur.fetchall()
    conect.close()
    return a

def consultaart(dato):
    conect = sqlite3.connect(DATABASE)
    cur = conect.cursor()
    cur.execute("SELECT * FROM 'articulos' WHERE id =='{}'".format(dato))
    a = cur.fetchall()
    conect.close()
    return a

def tresillo(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs


def consultaartid(dato):
    conect = sqlite3.connect(DATABASE)
    cur = conect.cursor()
    cur.execute("SELECT * FROM 'articulos' WHERE id_art =='{}'".format(dato))
    a = cur.fetchall()
    conect.close()
    return a




def nuevo(*wargs):
    print(wargs)
    datos = wargs[0]
    conect = sqlite3.connect(DATABASE)
    cur = conect.cursor()
    cur.execute("INSERT INTO user(username, email, password, slogan) VALUES (?, ?, ?, ?)",(datos[0], datos[1], datos[2], datos[3],))
    conect.commit()
  #  directorio = consultadato('user', '{}'.format(datos[0]))
 #   os.mkdir('static/img/{}'.format(directorio[0][0]))
    conect.close()


