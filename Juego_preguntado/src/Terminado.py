
from Constantes import *
from Funciones import *
import pygame
from datetime import date
import random


pygame.init()
pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("assets/img/icono.png")
pantalla = pygame.display.set_mode(PANTALLA)
fondo_pantalla = pygame.transform.scale(pygame.image.load("assets/img/GAME_OVER.png"), PANTALLA)

pygame.display.set_caption("Ingresar nombre")

boton_carga = crear_elemento_juego("assets/img/mini_caja.png", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA, 670, 450)

def mostrar_fin_juego(pantalla: pygame.Surface, partidas, cola_eventos: list, datos_juegos: dict, texto: str = "") -> tuple:

    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.KEYDOWN:
            TECLA_SONIDO.play()
            if evento.key == pygame.K_BACKSPACE:
                datos_juegos["nombre"] = datos_juegos["nombre"][:-1]
            elif evento.key == pygame.K_RETURN or evento.key == 13:
                CLICK_SONIDO.play()
                
                if len(datos_juegos["nombre"]) > 2 and es_alfabetico(datos_juegos["nombre"]):
                    
                    partidas.append({
                        "nombre": datos_juegos["nombre"],
                        "puntuacion": datos_juegos["puntuacion"],
                        "dia": datos_juegos["fecha_hoy"]
                    })
                    guardar_puntuacion(partidas)
                    retorno = "menu"
                else:
                    ERROR_SONIDO.play()
            elif len(datos_juegos["nombre"]) < 12:
                tecla_presionada = pygame.key.name(evento.key)
                bloc_mayus = pygame.key.get_mods()

                if len(tecla_presionada) == 1:
                    if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2:
                        datos_juegos["nombre"] += tecla_presionada.upper()
                    else:
                        datos_juegos["nombre"] += tecla_presionada.lower()

    pantalla.blit(fondo_pantalla, (0, 0))

    limpiar_superficie(boton_carga, "assets/img/mini_caja.png", ANCHO_BOTON_PREGUNTA, ALTO_BOTON_PREGUNTA)
    pantalla.blit(boton_carga["superficie"], boton_carga["rectangulo"])
    mostrar_texto(boton_carga["superficie"], f"Puntaje: {datos_juegos['puntuacion']} pts", (10, 10), FUENTE_RESPUESTA, COLOR_BLANCO)

    input_rect = pygame.Rect(140, 590, 800, 60)


    nombre_ingresado = datos_juegos["nombre"]
    if nombre_ingresado == "":                               
       
        texto_mostrar = "Ingrese su nombre: "
    else:                                                          
        texto_mostrar = f"{nombre_ingresado}"

    fuente_input = pygame.font.SysFont(FUENTE_JUEGO, 40, True)
    mostrar_texto(pantalla, texto_mostrar, (730, 470), fuente_input, COLOR_NEGRO)

    return retorno, texto
