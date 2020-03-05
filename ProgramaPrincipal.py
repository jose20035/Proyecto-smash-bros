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
        print("El numero de actores que tienen las peliculas son:")
        for peli in contar_actores(datos):
            print("La pelicula %s tienen %s actores." % (peli.get("titulo"),peli.get("nºactores")))
        a=input("Pulsa enter para continuar.")
    elif opcion == "3":
        print()
        palabra1=input("Introduce una palabra que creas que este en la sinopsis:> ")
        palabra2=input("Introduce otra palabra que creas que este en la sinopsis:> ")
        print()
        print("Los titulos en los que las palabras estan realcionados con la sinopsis son:")
        for peli in buscar_sinopsis(datos,palabra1,palabra2):
            print(peli)
        a=input("Pulsa enter para continuar.")
    elif opcion == "4":
        print()
        actor=input("Introuce el actor del que quieras buscar sus pelicualas:> ")
        print()
        print("Las peliculas en las que aparece ese actor son:")
        for peli in buscar_por_actor(datos,actor):
            print(peli)
        a=input("Pulsa enter para continuar.")
    elif opcion == "5":
        cont=1
        print()
        fechaini=input("Introduce la fecha inicio con formato (YYYY-MM-DD):> ")
        fechafin=input("Introduce la fecha fin con formato (YYYY-MM-DD):> ")
        print()
        print("Las tres pelias mejor valoradas de esa fecha son:")
        for peli in buscar_por_fecha(datos,fechaini,fechafin):
            print("#%i La peli %s con el poster:%s" % (cont,peli.get("titulo"),peli.get("poster")))
            cont=cont+1
        a=input("Pulsa enter para continuar.")
    elif opcion =="0":
        break