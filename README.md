# GeminiAi-qa-api
Conéctate a la IA Gemini para enviar preguntas y recibir respuestas automáticamente.

# Gemini QA API

Este repositorio proporciona una solución para conectarse a la IA Gemini, hacerle preguntas y recibir respuestas de forma programática. 

## Funcionalidades

- Conexión básica a la IA Gemini
- Envío de preguntas y recepción de respuestas
- Iteración de consultas y análisis de respuestas

### Características futuras

- Configuración y despliegue como una API RESTful
- Manejo de autenticación y permisos
- Registro y monitoreo de peticiones y respuestas

## Instalación

Sigue los siguientes pasos para instalar y ejecutar el proyecto:

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/GeminiAi-qa-api.git
    cd GeminiAi-qa-api
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Configura el entorno añadiendo tu API key de la IA Gemini en un archivo `.env`:

    ```bash
    GEMINI_API_KEY=tu_apikey
    ```

4. Inicia el servidor:

    ```bash
   python3 main.py
    ```

## Uso

Inicialmente, este proyecto te permite hacer preguntas a la IA Gemini con un script sencillo. A medida que el proyecto avance, también será posible interactuar mediante endpoints API.
