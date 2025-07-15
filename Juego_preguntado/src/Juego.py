import pygame
from Constantes import *
from Funciones import *
from datetime import date
import random # Se agregó esta importación para usar random.sample


pygame.init()

pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("assets/img/icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)

fondo_pantalla = pygame.transform.scale(pygame.image.load("assets/img/fondo.jpg"),PANTALLA)

# Se asume que la función crear_elemento_juego en Funciones.py

caja_pregunta = crear_elemento_juego("assets/img/textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA,710,125)
boton_respuesta_uno = crear_elemento_juego("assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,450,400)
boton_respuesta_dos = crear_elemento_juego("assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,900,400)
boton_respuesta_tres = crear_elemento_juego("assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,450,500)
boton_respuesta_cuatro = crear_elemento_juego("assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA,900,500)
corazon_vida_uno = crear_elemento_juego("assets/img/corazon_vida.jpg",ANCH0_CORAZON,ALTO_CORAZON,415,125)
corazon_vida_dos = crear_elemento_juego("assets/img/corazon_vida.jpg",ANCH0_CORAZON,ALTO_CORAZON,475,125)
corazon_vida_tres = crear_elemento_juego("assets/img/corazon_vida.jpg",ANCH0_CORAZON,ALTO_CORAZON,535,125)

reloj_tiempo = crear_elemento_juego("assets/img/RELOJ.png",ANCH0_CORAZON,ALTO_CORAZON,1135,125)


boton_bomba = crear_elemento_juego("assets/img/BOMBA.png",ANCH0_BOTON_BONUS,ALTO_BOTON_BONUS,100,37)
boton_duplicar_vida = crear_elemento_juego("assets/img/DUPLICAR.png",ANCH0_BOTON_BONUS,ALTO_BOTON_BONUS,100,225)
boton_por_dos = crear_elemento_juego("assets/img/X2.png",ALTO_BOTON_BONUS,ALTO_BOTON_BONUS,100,406)
boton_pasar = crear_elemento_juego("assets/img/PASAR.png",ALTO_BOTON_BONUS,ALTO_BOTON_BONUS,100,590)

pygame.draw.rect(pantalla, (255,0,0), boton_bomba["rectangulo"], 2)
pygame.draw.rect(pantalla, (0,255,0), boton_duplicar_vida["rectangulo"], 2)
pygame.draw.rect(pantalla, (0,0,255), boton_por_dos["rectangulo"], 2)
pygame.draw.rect(pantalla, (255,255,0), boton_pasar["rectangulo"], 2)

lista_preguntas = []
ruta_archivo = "data/preguntas.csv"

if not leer_csv_preguntas(ruta_archivo, lista_preguntas):
    exit()

mezclar_lista(lista_preguntas)

corriendo = True
reloj = pygame.time.Clock()
evento_tiempo = pygame.USEREVENT
pygame.time.set_timer(evento_tiempo,1000)

comodines = {
    "eliminadas" : [], 
    "bandera_c_bomba": False,           
    "bandera_c_por_2": False,           
    "bandera_c_doble_chance": False,    
    "bandera_c_pasar": False,
    "modo_doble_chance": False, 
    "intento_doble_chance": False, 
    "aplicar_x2": False,
    "corazones_eliminados":0 
    }



def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    """_summary_

    Args:
        pantalla (pygame.Surface): _description_
        cola_eventos (list[pygame.event.Event]): _description_
        datos_juego (dict): _description_

    Returns:
        str: _description_
    """
    retorno = "juego"
    pregunta_actual = lista_preguntas[datos_juego['indice']]
    
    if datos_juego["vidas"] == 0 or datos_juego["tiempo_restante"] == 0:
        limpiar_dic(comodines)
        retorno = "terminado"    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            limpiar_dic(comodines)
            retorno = "salir"
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            respuesta = obtener_respuesta_click(boton_respuesta_uno,boton_respuesta_dos,boton_respuesta_tres,boton_respuesta_cuatro,evento.pos)
            if respuesta in comodines.get("eliminadas",[]):
                    continue
            if respuesta != None:
                avanzar_pregunta = False
                
                
                if comodines["modo_doble_chance"]:
                    if respuesta == pregunta_actual["respuesta_correcta"]:
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO 
                        CLICK_SONIDO.play()
                        datos_juego["r_correctas_seguidas"] += 1
                        avanzar_pregunta = True
                        comodines["modo_doble_chance"] = False
                    else:
                        ERROR_SONIDO.play()
                        datos_juego["vidas"] -= 1 
                        datos_juego["r_correctas_seguidas"] = 0
                        comodines["corazones_eliminados"] += 1
                        avanzar_pregunta = True
                        comodines["modo_doble_chance"] = False 
                    comodines["eliminadas"] = [0]
                
                elif comodines["aplicar_x2"] == True:
                    comodines["aplicar_x2"] = False
                    if respuesta == pregunta_actual["respuesta_correcta"]:
                        datos_juego["puntuacion"] += 200 
                        CLICK_SONIDO.play()
                        avanzar_pregunta = True
                        datos_juego["r_correctas_seguidas"] += 1
                    else:
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        else:
                            datos_juego["vidas"] -= 1
                        comodines["corazones_eliminados"] += 1
                        ERROR_SONIDO.play()
                        datos_juego["r_correctas_seguidas"] = 0
                        avanzar_pregunta = True 
                    comodines["eliminadas"] = [0]
                else: 
                    if respuesta == pregunta_actual["respuesta_correcta"]:
                        CLICK_SONIDO.play()
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                        datos_juego["r_correctas_seguidas"] += 1
                        avanzar_pregunta = True
                    else:
                        ERROR_SONIDO.play()
                        datos_juego["r_correctas_seguidas"] = 0
                        if comodines["intento_doble_chance"] and not comodines["modo_doble_chance"]:
                            comodines["modo_doble_chance"] = True 
                            comodines["intento_doble_chance"] = False 
                            datos_juego["tiempo_restante"] += 5 
                            avanzar_pregunta = False 
                        else:
                            datos_juego["vidas"] -= 1
                            comodines["corazones_eliminados"] += 1
                            avanzar_pregunta = True 
                    comodines["eliminadas"] = [0]
                if avanzar_pregunta:
                    if datos_juego["r_correctas_seguidas"] == 5:
                        datos_juego["vidas"] += 1
                        datos_juego["tiempo_restante"] += 10
                        datos_juego["r_correctas_seguidas"] = 0
                    
                    datos_juego['indice'] += 1
                    if datos_juego['indice'] == len(lista_preguntas):
                        mezclar_lista(lista_preguntas)
                        datos_juego['indice'] = 0
                    pregunta_actual = cambiar_pregunta(lista_preguntas,datos_juego['indice'],caja_pregunta,boton_respuesta_uno,boton_respuesta_dos,boton_respuesta_tres,boton_respuesta_cuatro)    
                
            if boton_pasar["rectangulo"].collidepoint(evento.pos):
                if not comodines["bandera_c_pasar"]:
                    CLICK_SONIDO.play()
                    comodines["bandera_c_pasar"] = True
                    datos_juego['indice'] += 1
                    if datos_juego['indice'] == len(lista_preguntas):
                        mezclar_lista(lista_preguntas)
                        datos_juego['indice'] = 0    
                    pregunta_actual = cambiar_pregunta(lista_preguntas,datos_juego['indice'],caja_pregunta,boton_respuesta_uno,boton_respuesta_dos,boton_respuesta_tres,boton_respuesta_cuatro) 
                    comodines["eliminadas"] = [0]   
                else:
                    ERROR_SONIDO.play()

            if boton_por_dos["rectangulo"].collidepoint(evento.pos):
                if not comodines["bandera_c_por_2"]:
                    comodines["bandera_c_por_2"] = True
                    comodines["aplicar_x2"] = True
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()

            if boton_duplicar_vida["rectangulo"].collidepoint(evento.pos):
                if not comodines["bandera_c_doble_chance"]:
                    CLICK_SONIDO.play()
                    comodines["bandera_c_doble_chance"] = True  
                    comodines["intento_doble_chance"] = True  
                else:
                    ERROR_SONIDO.play()
            
          
            if boton_bomba["rectangulo"].collidepoint(evento.pos):
                if not comodines["bandera_c_bomba"]:
                    CLICK_SONIDO.play()
                    comodines["bandera_c_bomba"] = True 
                    comodines["eliminadas"] = usar_bomba(pregunta_actual) 
                else:
                    ERROR_SONIDO.play()
                                           
        
        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(caja_pregunta["superficie"],caja_pregunta["rectangulo"])
    
    
    if 1 not in comodines.get("eliminadas",[]):
        pantalla.blit(boton_respuesta_uno["superficie"],boton_respuesta_uno["rectangulo"])
    if 2 not in comodines.get("eliminadas",[]):
        pantalla.blit(boton_respuesta_dos["superficie"],boton_respuesta_dos["rectangulo"])
    if 3 not in comodines.get("eliminadas",[]):
        pantalla.blit(boton_respuesta_tres["superficie"],boton_respuesta_tres["rectangulo"])
    if 4 not in comodines.get("eliminadas",[]):
        pantalla.blit(boton_respuesta_cuatro["superficie"],boton_respuesta_cuatro["rectangulo"])
        
    pantalla.blit(corazon_vida_uno["superficie"],corazon_vida_uno["rectangulo"])
    
    pantalla.blit(boton_bomba["superficie"],boton_bomba["rectangulo"])
    pantalla.blit(boton_duplicar_vida["superficie"],boton_duplicar_vida["rectangulo"])
    pantalla.blit(boton_por_dos["superficie"],boton_por_dos["rectangulo"])
    pantalla.blit(boton_pasar["superficie"],boton_pasar["rectangulo"])


    pantalla.blit(reloj_tiempo["superficie"],reloj_tiempo["rectangulo"])

    mostrar_texto(caja_pregunta["superficie"],pregunta_actual["pregunta"],(20,10),FUENTE_PREGUNTA,COLOR_NEGRO)
   
    # Solo muestra el texto de los botones si están visibles
    if boton_respuesta_uno.get("visible", True):
        mostrar_texto(boton_respuesta_uno["superficie"],pregunta_actual["respuesta_1"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    if boton_respuesta_dos.get("visible", True):
        mostrar_texto(boton_respuesta_dos["superficie"],pregunta_actual["respuesta_2"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    if boton_respuesta_tres.get("visible", True):
        mostrar_texto(boton_respuesta_tres["superficie"],pregunta_actual["respuesta_3"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    if boton_respuesta_cuatro.get("visible", True):
        mostrar_texto(boton_respuesta_cuatro["superficie"],pregunta_actual["respuesta_4"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)

    pantalla.blit(corazon_vida_uno["superficie"],corazon_vida_uno["rectangulo"])
    if comodines.get("corazones_eliminados") <= 1:
        pantalla.blit(corazon_vida_dos["superficie"],corazon_vida_dos["rectangulo"])
    if comodines.get("corazones_eliminados") == 0:
        pantalla.blit(corazon_vida_tres["superficie"],corazon_vida_tres["rectangulo"])

    

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(415,195),FUENTE_DATOS_PUNTUACION)
    mostrar_texto(pantalla,f"{datos_juego['tiempo_restante']} s",(1200,140),FUENTE_DATOS_TIEMPO)

    return retorno
