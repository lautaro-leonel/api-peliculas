Movies API

Movies API es una API REST desarrollada en Python para consultar información sobre películas de ciencia ficción.  
El proyecto fue creado con el objetivo de practicar desarrollo backend, diseño de APIs y trabajo con bases de datos.

Descripcion

La API permite obtener información estructurada sobre películas y consumirla desde aplicaciones externas como sitios web o aplicaciones móviles.  
Las respuestas se entregan en formato JSON.

Tecnologias utilizadas

Python  
FastAPI  
SQL  
JSON  
Git  
GitHub  

Funcionalidades

Obtencion de todas las peliculas  
Busqueda de peliculas por ID  
Filtrado por genero  
Filtrado por año  

Estructura de datos

Cada pelicula contiene informacion como:

ID  
Titulo  
Año  
Genero  
Subgenero  
Director  
Descripcion  

Endpoints principales

GET /movies  
GET /movies/{id}  
GET /movies?genre=  
GET /movies?year=  

Ejecucion del proyecto

Clonar el repositorio  
Instalar las dependencias  
Ejecutar el servidor  
Acceder a la documentacion automatica en el navegador

http://localhost:8000/docs

Objetivo del proyecto

Aplicar conocimientos de Python en un proyecto real  
Comprender el funcionamiento de una API REST  
Desarrollar un proyecto para portfolio profesional

Estado del proyecto

El proyecto se encuentra en desarrollo y se planean futuras mejoras como autenticacion, paginacion y despliegue en la nube
