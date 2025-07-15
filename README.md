# 🎮 Juego Preguntado

Este es un juego de preguntas y respuestas estilo **"Preguntados"**, desarrollado en **Python** utilizando la librería **Pygame**.

## 📌 Objetivo del Juego

Responder correctamente la mayor cantidad de preguntas posibles.  
El jugador contará con comodines que pueden ayudarlo a avanzar cuando no sabe una respuesta.

---

## 🧠 ¿Cómo se juega?

1. Se muestra una pregunta con **cuatro opciones posibles**.
2. El jugador debe seleccionar la respuesta correcta.
3. Puede usar comodines especiales:
   - 💣 **Bomba**: Elimina dos respuestas incorrectas.
   - 🔁 **Doble chance**: Permite intentar dos veces.
   - ❌ **X2**: Duplica la puntuación si responde bien.
   - ⏭️ **Pasar**: Saltea la pregunta sin perder puntos.
4. El juego registra tu puntuación y la guarda en un **ranking de los 10 mejores**.

---

## 🧩 Características

- Preguntas leídas desde archivo CSV.
- Interfaz visual con botones y textos.
- Soporte para comodines.
- Sistema de puntuación.
- Pantalla de **Top 10** con los mejores puntajes.

---

## ▶️ Cómo ejecutar

1. Asegurate de tener Python 3 instalado.
2. Instalá Pygame:

```bash
pip install pygame

