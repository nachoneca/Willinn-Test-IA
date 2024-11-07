# Preguntas y Respuestas con Flask y LangChain

Este proyecto utiliza Flask para crear una API que permite hacer preguntas sobre un documento PDF y obtener respuestas utilizando el modelo `nemotron-mini` de Ollama, LangChain y FAISS. El sistema realiza un análisis de texto del documento PDF y utiliza un modelo de lenguaje para responder preguntas basadas en el contenido de dicho documento.

## Requisitos

Asegúrate de tener los siguientes paquetes instalados:

- `Flask` para la creación de la API.
- `PyPDF2` para la extracción de texto desde un archivo PDF.
- `LangChain` para el procesamiento de textos y uso de modelos de lenguaje.
- `FAISS` para crear un índice de búsqueda basado en las embeddings generadas a partir del texto.
- `Ollama` para interactuar con el modelo `nemotron-mini`.

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install Flask PyPDF2 langchain langchain-community faiss-cpu

```
Aquí tienes el archivo README.md actualizado con las instrucciones sobre cómo fue probado el proyecto utilizando Postman:

markdown
Copy code
# Preguntas y Respuestas con Flask y LangChain

Este proyecto utiliza Flask para crear una API que permite hacer preguntas sobre un documento PDF y obtener respuestas utilizando el modelo `nemotron-mini` de Ollama, LangChain y FAISS. El sistema realiza un análisis de texto del documento PDF y utiliza un modelo de lenguaje para responder preguntas basadas en el contenido de dicho documento.

## Requisitos

Asegúrate de tener los siguientes paquetes instalados:

- `Flask` para la creación de la API.
- `PyPDF2` para la extracción de texto desde un archivo PDF.
- `LangChain` para el procesamiento de textos y uso de modelos de lenguaje.
- `FAISS` para crear un índice de búsqueda basado en las embeddings generadas a partir del texto.
- `Ollama` para interactuar con el modelo `nemotron-mini`.

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install Flask PyPDF2 langchain langchain-community faiss-cpu
Instalación y Configuración
```
1. Instalar Ollama
Primero, debes instalar Ollama en tu máquina. Sigue las instrucciones desde la página oficial: Ollama Installation.

2. Descargar el Modelo nemotron-mini
Descarga el modelo nemotron-mini utilizando el siguiente comando:

```bash
Copy code
ollama pull nemotron-mini
```
Este comando descargará el modelo nemotron-mini, que se utilizará para responder las preguntas.

3. Iniciar Ollama
Asegúrate de que Ollama esté corriendo antes de intentar hacer peticiones a la API. Ejecuta el siguiente comando para iniciar Ollama:

```bash
Copy code
ollama start
```
Esto iniciará el servidor de Ollama en http://localhost:11434.

4. Subir el Archivo PDF
Coloca el archivo PDF (por ejemplo, vikingos.pdf) en la carpeta PDF dentro del directorio del proyecto. Este PDF se utilizará para generar las embeddings y crear el índice de búsqueda.

5. Ejecutar el Servidor Flask
Ejecuta el servidor Flask con el siguiente comando:

```bash
Copy code
python app.py
```
Esto iniciará la API en http://localhost:3333.

## Cómo Funciona
La aplicación permite hacer preguntas a un modelo de lenguaje entrenado en un conjunto de datos 
extraído de un archivo PDF. La API expone un solo endpoint:

Endpoint: /nemotron-mini
Método: POST

Cuerpo: El cuerpo de la solicitud debe ser un JSON que contenga la pregunta que deseas realizar.

Ejemplo:

{
  "question": "¿Qué son los vikingos?"
}

Respuesta: La respuesta será un JSON con la respuesta generada por el modelo, basada en el contenido del PDF.

Ejemplo de respuesta:

{
  "answer": "The Vikings were a group of people from the Nordic countries who traveled to other lands in search of loot."
}

## Pruebas con Postman
Este proyecto fue probado utilizando Postman para realizar solicitudes POST al endpoint /nemotron-mini y obtener respuestas basadas en el contenido del archivo PDF.

Resumen de la prueba con Postman
Durante la prueba, se envió una solicitud POST con el siguiente JSON en el cuerpo:

{
  "question": "¿Qué son los vikingos?"
}
La API respondió correctamente con la siguiente respuesta:

{
  "answer": "The Vikings were a group of people from the Nordic countries who traveled to other lands in search of loot."
}
## Estructura del Proyecto
app.py: El archivo principal que contiene el servidor Flask y la lógica de procesamiento.
PDF/: Carpeta que contiene el archivo PDF que se utilizará para generar las embeddings.

## Conclusión
Este proyecto proporciona una solución simple para realizar preguntas sobre documentos PDF utilizando la tecnología de procesamiento de lenguaje natural y búsqueda de similitud, integrando herramientas como Flask, LangChain, FAISS y Ollama. La API fue probada exitosamente con Postman, asegurando que las preguntas y respuestas se generen correctamente en base al contenido del archivo PDF.