import pygame
from Constantes import *
from Funciones import *
from Configuracion import *

pygame.init()
lista_botones = crear_botones_menu()
print(lista_botones)
fondo_menu = pygame.transform.scale(pygame.image.load("assets/img/fondo.jpg"),PANTALLA)


def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "menu"
    #Gestionar Eventos
    for evento in cola_eventos:
        #Actualizaciones
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        if i == BOTON_JUGAR:
                            retorno = "juego"
                        elif i == BOTON_PUNTUACIONES:
                            retorno = "rankings"
                        elif i == BOTON_CONFIG:
                            retorno = "ajustes"
                        else:
                            retorno = "salir"
        
    
    #Dibujar en pygame
    pantalla.blit(fondo_menu,(0,0))
    for i in range(len(lista_botones)):
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"   JUGAR   ",(135,25),FUENTE_TEXTO,COLOR_NEGRO)#aparece
    mostrar_texto(lista_botones[BOTON_PUNTUACIONES]["superficie"],"  RANKING  ",(120,25),FUENTE_TEXTO,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_CONFIG]["superficie"],"  CONFIGURACIÓN  ",(50,25),FUENTE_CONFIGURACION,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"     SALIR   ",(135,25),FUENTE_TEXTO,COLOR_NEGRO)#aparece


    return retorno