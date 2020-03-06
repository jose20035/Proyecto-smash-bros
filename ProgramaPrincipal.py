import json
from Funciones import *
import os

ndatos=input("Intrudoce el nombre del archivo .json:> ")
f=open(ndatos)
datos=json.load(f)
f.close()
while True:
    os.system("clear")
    print('''
    1.Listar los juegos.
    2.Comparar Nº Persinajes entre dos juegos.
    3.Listar los estadios de un juego.
    4.Buscar juegos en los que aparece un personaje.
    5.Busca un juego en el que aparezca un personaje y un estadio concreto.
    0.Salir''')
    print()
    opcion=input(":> ")
    while opcion not in ("0","1","2","3","4","5"):
        print("Error opción no correcta.")
        opcion=input(":> ")
    if opcion =="1":
        print()
        print("Los juegos registrados son:")
        for jue in ListarTodo(datos):
            print("Nombre: %s Abreviación: %s Caratula: %s" % (jue.get("Juego"),jue.get("Abreviacion"),jue.get("baner")))
        a=input("Pulsa enter para continuar.")
    elif opcion =="2":
        print()
        print("Introduce dos juegos:")
        jue1=input(":> ")
        jue2=input(":> ")
        if 
        a=input("Pulsa enter para continuar.")
    '''elif opcion == "3":
        
        a=input("Pulsa enter para continuar.")
    elif opcion == "4":
        
        a=input("Pulsa enter para continuar.")
    elif opcion == "5":
        
        a=input("Pulsa enter para continuar.")
    elif opcion =="0":
        break'''