import os
import re

# Extensiones por tipo
extensiones_img = ("assets/img/.png", "assets/img/.jpg", "assets/img/.webp")
extensiones_audio = ("assets/audio/.mp3", "assets/audio/.wav")
extensiones_data = ("data/.csv", "data/.json")

# Carpetas destino
rutas = {
    "img": "assets/img/",
    "audio": "assets/audio/",
    "data": "data/"
}

# Archivos a procesar (todos los .py)
def obtener_archivos_py(ruta_raiz):
    archivos_py = []
    for carpeta_actual, _, archivos in os.walk(ruta_raiz):
        for archivo in archivos:
            if archivo.endswith(".py"):
                archivos_py.append(os.path.join(carpeta_actual, archivo))
    return archivos_py

# Reemplazo de rutas
def actualizar_rutas_en_archivo(path_archivo):
    with open(path_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    contenido_modificado = contenido

    # Imagen
    for ext in extensiones_img:
        contenido_modificado = re.sub(
            rf'(["\'])((?!assets/img/)[\w\-\/]*{re.escape(ext)})\1',
            rf'"\1{rutas["img"]}\2"',
            contenido_modificado
        )

    # Audio
    for ext in extensiones_audio:
        contenido_modificado = re.sub(
            rf'(["\'])((?!assets/audio/)[\w\-\/]*{re.escape(ext)})\1',
            rf'"\1{rutas["audio"]}\2"',
            contenido_modificado
        )

    # Data
    for ext in extensiones_data:
        contenido_modificado = re.sub(
            rf'(["\'])((?!data/)[\w\-\/]*{re.escape(ext)})\1',
            rf'"\1{rutas["data"]}\2"',
            contenido_modificado
        )

    if contenido_modificado != contenido:
        with open(path_archivo, "w", encoding="utf-8") as f:
            f.write(contenido_modificado)
        print(f"✅ Rutas actualizadas en: {path_archivo}")
    else:
        print(f"↪️  Sin cambios: {path_archivo}")

# Ejecutar
if __name__ == "__main__":
    archivos = obtener_archivos_py(".")
    for archivo in archivos:
        actualizar_rutas_en_archivo(archivo)
