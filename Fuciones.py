def ListarTodo(datos):
    respuesta=[]
    for i in datos:
        respuesta.append({"Juego":i.get("name"),"Abreviacion":i.get("abbreviation"),"baner":i.get("BannerUrl")})
    return respuesta

def NumeroPersonajesEntre(datos,juego1,juego2):
    for i in datos:
        if i.get("name") == juego1:
            nºperjuego1=len(i.get("characters"))
        if i.get("name") == juego2:
            nºperjuego2=len(i.get("characters"))
    if nºperjuego1 > nºperjuego2:
        return {"JuegoConMasPersonajes":juego1,"NºPersonajes":juego1-juego2}
    elif nºperjuego2 > nºperjuego1:
        return {"JuegoConMasPersonajes":juego2,"NºPersonajes":juego2-juego1}
    else:
        return True

def ListarEstadios(datos,juego):
    estadios=[]
    for i in datos:
        if i.get("name") == juego:
            for o in i.get("stages"):
                estadios.append(o.get("Name"))
    return estadios

def BuscarPesonaje(datos,personaje):
    juegos=[]
    for i in datos:
        for o in i.get("characters"):
            if personaje == o.get("Name"):
                juegos.append(i.get("name"))
    return juegos

def BuscarCoincidencia(datos,personaje,estadio):
    juegos=[]
    for i in datos:
        for perso in i.get("characters"):
            for estadio in i.get("stages"):
                if perso.get("Name") == personaje and estadio.get("Name") == estadio:
                    juegos.append(i.get("name"))
    return juegos