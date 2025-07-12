import pygame 
from Constantes import *
from Menu import *
from Juego import *
from Funciones import *
from Configuracion import *
from Rankings import *
from Terminado import *
from datetime import date

pygame.init()
pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("assets/img/icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(PANTALLA)
pygame.mixer.init()


datos_juego = {
    "puntuacion":0,
    "vidas":CANTIDAD_VIDAS,
    "nombre":"","r_correctas_seguidas":0,
    "tiempo_restante":30,
    "indice":0,
    "volumen_musica":100,
    "fecha_hoy":str(date.today()),
    }

partidas = [
]

corriendo = True
texto = ""
reloj = pygame.time.Clock()
bandera_musica = False
bandera_juego = False

ventana_actual = "menu" #VENTANA POR DEFECTO / LAS CAMBIA SEGÚN REQUIERA MOSTRAR

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get() #EJECUTA NUEVA COLA DE EVENTOS
  
    
    if ventana_actual == "menu":
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        if bandera_juego == True:
            texto = limpiar_string(texto)
            reiniciar_estadisticas(datos_juego)
            bandera_juego = False
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
         ventana_actual,texto = mostrar_fin_juego(pantalla, partidas ,cola_eventos, datos_juego,texto)
    elif ventana_actual == "juego":
       
        bandera_juego = True
        porcentaje_volumen = datos_juego["volumen_musica"] / 100

        if bandera_musica == False:
            pygame.mixer.music.load("assets/audio/musica.mp3")
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_musica = True

        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_submenu_config(pantalla, cola_eventos) #mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,partidas)
    elif ventana_actual == "volumen":
        ventana_actual = mostrar_ajustes(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "agregar_preguntas":
        ventana_actual = mostrar_agregar_preguntas(pantalla, cola_eventos)
    elif ventana_actual == "dificultad":
        ventana_actual = mostrar_dificultad(pantalla, cola_eventos, datos_juego)

    pygame.display.flip()

pygame.quit()

