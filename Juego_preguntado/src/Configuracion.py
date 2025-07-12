import pygame
from Constantes import *
from Funciones import *

pygame.init()
pantalla = pygame.display.set_mode(PANTALLA)
fondo_pantalla = pygame.transform.scale(pygame.image.load("assets/img/fondo.jpg"),PANTALLA)

bandera_musica = False

boton_suma = crear_elemento_juego("assets/img/mas.webp",60,60,1000,300)
boton_resta = crear_elemento_juego("assets/img/menos.webp",60,60,600,300)
boton_volver = crear_elemento_juego("assets/img/textura_respuesta.jpg",100,40,420,130)
caja_volumen = crear_elemento_juego("assets/img/mini_caja.png", 250,120,720,255)
#boton_off_musica = crear_elemento_juego("assets/img/on_mute.png",60,60,500,200)
boton_on_musica = crear_elemento_juego("assets/img/mute.png",60,60,800,400)
# Botones

boton_volumen_config = crear_elemento_juego("assets/img/mini_caja.png", 600, 100, 580, 200)
boton_agregar_preguntas = crear_elemento_juego("assets/img/mini_caja.png", 600, 100, 580, 350)
boton_dificultad = crear_elemento_juego("assets/img/mini_caja.png", 600, 100, 580, 500) 
boton_volver_config = crear_elemento_juego("assets/img/textura_respuesta.jpg", 100, 40, 420, 130)

# BOTONES
boton_facil = crear_elemento_juego("assets/img/mini_caja.png", 300, 80, 700, 200)
boton_medio = crear_elemento_juego("assets/img/mini_caja.png", 300, 80, 700, 300)
boton_dificil = crear_elemento_juego("assets/img/mini_caja.png", 300, 80, 700, 400)
boton_volver = crear_elemento_juego("assets/img/textura_respuesta.jpg", 100, 40, 420, 130)

# Crear botones
boton_proponer = crear_elemento_juego("assets/img/mini_caja.png", 600, 80, 500, 350)
boton_importar = crear_elemento_juego("assets/img/mini_caja.png", 600, 80, 500, 500)


def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "volumen"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_suma["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_musica"] <= 95:
                        datos_juego["volumen_musica"] += 5
                        CLICK_SONIDO.play()
                    else:
                        ERROR_SONIDO.play()
                elif boton_resta["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_musica"] > 0:
                        datos_juego["volumen_musica"] -= 5
                        CLICK_SONIDO.play()
                    else: 
                        ERROR_SONIDO.play()
                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
            
                            
                if boton_on_musica["rectangulo"].collidepoint(evento.pos): 
                    if datos_juego["volumen_musica"] < 100:
                        datos_juego["volumen_musica"] = 100
                        retorno = "volumen"
                        CLICK_SONIDO.play()
                    else:
                        datos_juego["volumen_musica"] = 0
                        retorno = "volumen"
                        CLICK_SONIDO.play()
                        #ERROR_SONIDO.play()

    
    
    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    pantalla.blit(caja_volumen["superficie"],caja_volumen["rectangulo"])
    

    pantalla.blit(boton_on_musica["superficie"],boton_on_musica["rectangulo"])
   
    #######
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(800,300),FUENTE_VOLUMEN,COLOR_AMARILLO_PASTEL)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(2,-15),FUENTE_RESPUESTA_VOLVER,COLOR_BLANCO)

    return retorno

def mostrar_submenu_config(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "ajustes"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volumen_config["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "volumen"
                elif boton_agregar_preguntas["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "agregar_preguntas"
                elif boton_dificultad["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "dificultad"
                elif boton_volver_config["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(boton_volumen_config["superficie"], boton_volumen_config["rectangulo"])
    pantalla.blit(boton_agregar_preguntas["superficie"], boton_agregar_preguntas["rectangulo"])
    pantalla.blit(boton_dificultad["superficie"], boton_dificultad["rectangulo"])
    pantalla.blit(boton_volver_config["superficie"], boton_volver_config["rectangulo"])

    mostrar_texto(boton_volumen_config["superficie"], "VOLUMEN", (170, 28), FUENTE_CONFIGURACION, COLOR_NEGRO)
    mostrar_texto(boton_agregar_preguntas["superficie"], "TU PREGUNTA", (115,30), FUENTE_CONFIGURACION, COLOR_NEGRO)
    mostrar_texto(boton_dificultad["superficie"], "DIFICULTAD", (150,28), FUENTE_CONFIGURACION, COLOR_NEGRO)
    mostrar_texto(boton_volver_config["superficie"], "VOLVER", (2,-15), FUENTE_RESPUESTA_VOLVER, COLOR_BLANCO)

    return retorno



def mostrar_agregar_preguntas(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event]) -> str: 
    retorno = "agregar_preguntas"

    # Gestionar eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_proponer["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "agregar_manual"  # a definir en main
                elif boton_importar["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "agregar_csv"     # a definir en main
                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "ajustes"

    # Dibujar fondo y elementos
    pantalla.blit(fondo_pantalla, (0, 0))

    # Texto explicativo
    mostrar_texto(pantalla, "ELIGE LA MANERA DE AGREGAR\nTUS PREGUNTAS AL JUEGO:", (530, 230), FUENTE_VOLUMEN, COLOR_AMARILLO_PASTEL)

    # Botones
    pantalla.blit(boton_proponer["superficie"], boton_proponer["rectangulo"])
    pantalla.blit(boton_importar["superficie"], boton_importar["rectangulo"])
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])

    mostrar_texto(boton_proponer["superficie"], "PROPONER PREGUNTA", (80, 25), FUENTE_RESPUESTA, COLOR_NEGRO)
    mostrar_texto(boton_importar["superficie"], "IMPORTAR CSV", (100, 25), FUENTE_RESPUESTA, COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"], "VOLVER", (2, -15), FUENTE_RESPUESTA_VOLVER, COLOR_BLANCO)

    return retorno


def mostrar_dificultad(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], datos_juego:dict) -> str:
    retorno = "dificultad"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_facil["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    datos_juego["dificultad"] = "Facil"
                    retorno = "ajustes"
                elif boton_medio["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    datos_juego["dificultad"] = "Medio"
                    retorno = "ajustes"
                elif boton_dificil["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    datos_juego["dificultad"] = "Dificil"
                    retorno = "ajustes"
                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "ajustes"

    # DIBUJO
    pantalla.blit(fondo_pantalla, (0, 0))
    pantalla.blit(boton_facil["superficie"], boton_facil["rectangulo"])
    pantalla.blit(boton_medio["superficie"], boton_medio["rectangulo"])
    pantalla.blit(boton_dificil["superficie"], boton_dificil["rectangulo"])
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])

    mostrar_texto(boton_facil["superficie"], "FÁCIL", (95, 22), FUENTE_VOLUMEN, COLOR_NEGRO)
    mostrar_texto(boton_medio["superficie"], "MEDIO", (90, 25), FUENTE_VOLUMEN, COLOR_NEGRO)
    mostrar_texto(boton_dificil["superficie"], "DIFÍCIL", (90, 23), FUENTE_VOLUMEN, COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"], "VOLVER", (2, -15), FUENTE_RESPUESTA_VOLVER, COLOR_BLANCO)

    return retorno
