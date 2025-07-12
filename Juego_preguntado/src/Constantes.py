import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_GRIS_CLARO = (255, 255, 255)
AZUL_ELECTRICO = (0, 150, 255) 
COLOR_AMARILLO_BRILLANTE = (255, 220, 0)
COLOR_AMARILLO_PASTEL = (255, 239, 184)
ANCHO = 1750
ALTO = 800
PANTALLA = (ANCHO,ALTO)
FPS = 30

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

ANCHO_PREGUNTA = 400
ALTO_PREGUNTA = 200
ANCHO_BOTON = 600
ALTO_BOTON = 100
ANCHO_BOTON_PREGUNTA = 400
ALTO_BOTON_PREGUNTA = 80
ANCH0_CORAZON = 60
ALTO_CORAZON = 60
ANCH0_BOTON_BONUS = 150
ALTO_BOTON_BONUS = 150
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
CLICK_SONIDO = pygame.mixer.Sound("assets/audio/click.mp3")
#TECLA_SONIDO = pygame.mixer.Sound(""assets/audio/TECLA.mp3")
TECLA_SONIDO = pygame.mixer.Sound("assets/audio/keyboard.mp3")
ERROR_SONIDO = pygame.mixer.Sound("assets/audio/error.mp3")


#GAME_OVER_IMAGEN = pygame.mixer.


FUENTE_PREGUNTA = pygame.font.SysFont("Press Start 2P",55,True)
FUENTE_RESPUESTA = pygame.font.SysFont("Press Start 2P",40,True)
FUENTE_RESPUESTA_VOLVER = pygame.font.SysFont("Press Start 2P",35,True)
FUENTE_TEXTO = pygame.font.SysFont("Press Start 2P",80,True)
FUENTE_CONFIGURACION = pygame.font.SysFont("Press Start 2P",70,True)
FUENTE_SUBMENU = pygame.font.SysFont("Press Start 2P",55,True)

FUENTE_VOLUMEN = pygame.font.SysFont("Press Start 2P",50,True)
FUENTE_DATOS = pygame.font.SysFont("Press Start 2P",60,True)
FUENTE_DATOS_TIEMPO = pygame.font.SysFont("Press Start 2P",45,True)
FUENTE_DATOS_PUNTUACION = pygame.font.SysFont("Press Start 2P",45,True)
FUENTE_JUEGO = "Press Start 2P"
FUENTE_TOP_10 = pygame.font.SysFont("Press Start 2P",40,True)

BOTON_JUGAR = 0

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25