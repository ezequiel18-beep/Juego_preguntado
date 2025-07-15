import random
from Constantes import *
import pygame
import json
import copy
import os

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    """_summary_

    Args:
        surface (_type_): _description_
        text (_type_): _description_
        pos (_type_): _description_
        font (_type_): _description_
        color (_type_, optional): _description_. Defaults to pygame.Color('black').
    """
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#GENERAL
def mezclar_lista(lista_preguntas:list) -> None:
    """_summary_

    Args:
        lista_preguntas (list): _description_
    """
    random.shuffle(lista_preguntas)

#GENERAL
def reiniciar_estadisticas(datos_juego:dict) -> None:
    """_summary_

    Args:
        datos_juego (dict): _description_
    """
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = 30


def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    """_summary_

    Args:
        textura (str): _description_
        ancho (int): _description_
        alto (int): _description_
        pos_x (int): _description_
        pos_y (int): _description_

    Returns:
        dict: _description_
    """
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    elemento_juego["rectangulo"] = elemento_juego["superficie"].get_rect()
    elemento_juego["rectangulo"].x = pos_x
    elemento_juego["rectangulo"].y = pos_y
    
    return elemento_juego

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int) -> None:
    """_summary_

    Args:
        elemento_juego (dict): _description_
        textura (str): _description_
        ancho (int): _description_
        alto (int): _description_
    """
    elemento_juego["superficie"] =  pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    
def obtener_respuesta_click(boton_respuesta_uno:dict,boton_respuesta_dos:dict,boton_respuesta_tres:dict,boton_respuesta_cuatro:dict,pos_click:tuple):
    """_summary_

    Args:
        boton_respuesta_uno (dict): _description_
        boton_respuesta_dos (dict): _description_
        boton_respuesta_tres (dict): _description_
        boton_respuesta_cuatro (dict): _description_
        pos_click (tuple): _description_

    Returns:
        _type_: _description_
    """
    lista_aux = [boton_respuesta_uno["rectangulo"],boton_respuesta_dos["rectangulo"],boton_respuesta_tres["rectangulo"], boton_respuesta_cuatro["rectangulo"]]
    respuesta = None
    
    for i in range(len(lista_aux)):
        if lista_aux[i].collidepoint(pos_click):
            respuesta = i + 1

    
    return respuesta

def cambiar_pregunta(lista_preguntas:list,indice:int,caja_pregunta:dict,boton_respuesta_uno:dict,boton_respuesta_dos:dict,boton_respuesta_tres:dict,boton_respuesta_cuatro:dict) -> dict:
    """_summary_

    Args:
        lista_preguntas (list): _description_
        indice (int): _description_
        caja_pregunta (dict): _description_
        boton_respuesta_uno (dict): _description_
        boton_respuesta_dos (dict): _description_
        boton_respuesta_tres (dict): _description_
        boton_respuesta_cuatro (dict): _description_

    Returns:
        dict: _description_
    """
    
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(caja_pregunta,"assets/img/textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA)
    limpiar_superficie(boton_respuesta_uno,"assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_dos,"assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_tres,"assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_cuatro,"assets/img/textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA) 

    return pregunta_actual

def crear_botones_menu() -> list:
    
    lista_botones = []
    pos_y = 135

    for i in range(4):
        boton = crear_elemento_juego("assets/img/mini_caja.png",ANCHO_BOTON,ALTO_BOTON,570,pos_y)
        pos_y += 130
        lista_botones.append(boton)
        
    return lista_botones


def guardar_puntuacion(datos: list)-> None:
   with open("data/partidas.json", 'w') as partidas:
    json.dump(datos,partidas, indent = 4)

def limpiar_string(texto:str) -> str:
    return ""

def limpiar_diccionario(diccionario:dict) -> str:
    return ""

def ordenar_top(partidas:list)-> list:

    
    lista = partidas.copy()


    for i in range(len(lista)):
        for j in range(0, len(lista) - 1):
            if lista[i]["puntuacion"] > lista[j ]["puntuacion"]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


    top_diez = lista[:10]
    return top_diez

#Especifica
def leer_csv_preguntas(nombre_archivo:str,lista_preguntas:list,separador:str = ",") -> bool:

    if os.path.exists(nombre_archivo) == True:
        with open(nombre_archivo,"r", encoding="utf-8") as archivo:
            #Falsa lectura --> Una lectura fantasma, para evitar que cuando se recorra con el for de abajo me muestre la cabecera
            archivo.readline()
            
            for linea in archivo:
                preguntas = crear_diccionario_preguntas(linea,separador)
                lista_preguntas.append(preguntas)
        
        retorno = True
    else:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        retorno = False
        
    return retorno

def crear_diccionario_preguntas(linea:str,separador:str = ",") -> dict:

    linea = linea.replace("","")
    lista_valores = linea.split(separador)
    
    preguntas = {}
    preguntas["pregunta"] = lista_valores[0]
    preguntas["respuesta_1"] = lista_valores[1]
    preguntas["respuesta_2"] = lista_valores[2]
    preguntas["respuesta_3"] = lista_valores[3]
    preguntas["respuesta_4"] = lista_valores[4]
    preguntas["respuesta_correcta"] = int(lista_valores[5])
    preguntas["dificultad"] = lista_valores[6]
    
    return preguntas

def es_alfabetico(cadena:str) -> bool:
    """Verifica si una cadena contiene únicamente letras y espacios.

    Args:
        cadena (str): Cadena de caracteres a validar.

    Returns:
        bool: True si la cadena es alfabética (letras y espacios)
    """
    if len(cadena) > 0:
        retorno = True
     
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])

            if not (65 <= valor_ascii <= 90 or 97 <= valor_ascii <= 122 or valor_ascii == 32):
                retorno = False
                break
    else:
        retorno = False

    return retorno

def mostrar_top_10(top_diez:list,boton_ranking:dict,pantalla) -> None:
    """_summary_

    Args:
        top_diez (list): _description_
        boton_ranking (dict): _description_

    Returns:
        _type_: _description_
        
    """
    boton_ranking["superficie"].fill((200, 200, 200, 180)) 


    y_pos = 50
    i = 1
    
    for entrada in top_diez:
        texto = f"{i}. {entrada['nombre']} - {entrada['puntuacion']} pts - Fecha: {entrada['dia']}"
        # texto_2 = f""
        mostrar_texto(boton_ranking["superficie"], texto, (50, y_pos), FUENTE_TOP_10, COLOR_NEGRO)
        y_pos += 40
        # mostrar_texto(boton_ranking["superficie"], texto_2, (50, y_pos), FUENTE_TOP_10, COLOR_NEGRO)
        # y_pos += 40
        i += 1


def convertir_a_lista(preguntas:list) -> list:
    """_summary_

    Args:
        preguntas (list): _description_

    Returns:
        list: _description_
    """
    with open("data/preguntas.json", "r", encoding="utf-8") as archivo:
        lista_preguntas = json.load(archivo)

    return lista_preguntas

def generar_comodin_bomba(lista_preguntas:list) -> None:
    """_summary_

    Args:
        lista_preguntas (list): _description_
    """
    respuestas = ["respuesta_1","respuesta_2","respuesta_3","respuesta_4"]
    indice_correcto = lista_preguntas["respuesta_correcta"]

def verificar_respuesta(datos_juego:dict,pregunta:dict,respuesta:int,comodines:dict) -> bool:
    """_summary_

    Args:
        datos_juego (dict): _description_
        pregunta (dict): _description_
        respuesta (int): _description_
        comodines (dict): _description_

    Returns:
        bool: _description_
    """
    if respuesta == pregunta["respuesta_correcta"]:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
    else:
        if datos_juego["puntuacion"] > 0:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        retorno = False 


    return retorno

def usar_bomba(pregunta_actual:list) -> list:
    """_summary_

    Args:
        pregunta_actual (list): _description_

    Returns:
        list: _description_
    """
    respuesta_correcta = pregunta_actual["respuesta_correcta"]
    indices = [1,2,3,4]

    indices.remove(respuesta_correcta)

    eliminadas = random.sample(indices, 2)
    return eliminadas

def limpiar_dic(comodines:dict) -> None:
    comodines["eliminadas"] = [0]
    comodines["bandera_c_por_2"] = False
    comodines["bandera_c_doble_chance"] = False
    comodines["bandera_c_bomba"] = False
    comodines["corazones_eliminados"] = 0
    comodines["bandera_c_pasar"] = False
    return