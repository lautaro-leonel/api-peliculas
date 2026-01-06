Movies API

Una **API REST** creada con **Python** para consultar información sobre películas de ciencia ficción.

Este proyecto fue desarrollado como práctica de **Backend**, manejo de **APIs**, **bases de datos** y **estructuración de endpoints**.


¿Qué hace esta API?

- Devuelve información de películas
- Permite filtrar datos
- Responde en formato **JSON**
- Simula un servicio real consumible por apps o webs



Tecnologías usadas

- Python
- FastAPI
- SQL (base de datos relacional)
- JSON
- Git & GitHub



Ejemplo de datos

Cada película incluye información como:

- ID
- Título
- Año
- Género
- Subgénero
- Director
- Descripción


Endpoints principales

- `GET /movies` → lista todas las películas  
- `GET /movies/{id}` → obtiene una película por ID  
- `GET /movies?genre=` → filtra por género  
- `GET /movies?year=` → filtra por año  



Cómo ejecutar el proyecto

1. Clonar el repositorio  
2. Instalar dependencias  
3. Ejecutar el servidor  
4. Acceder a la documentación automática en:

