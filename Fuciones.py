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

