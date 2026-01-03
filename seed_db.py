from database import SessionLocal, engine
from models import Base, Pelicula

# Asegura que la tabla exista
Base.metadata.create_all(bind=engine)

# TU lista actual (la copiás de API_1.py)
peliculas = [
    {
        "id": 1,
        "titulo": "Alien",
        "anio": 1979,
        "subgenero": "terror",
        "director": "Ridley Scott",
        "rating": 8.5
    },
    {
        "id": 2,
        "titulo": "Blade Runner",
        "anio": 1982,
        "subgenero": "ciencia ficcion",
        "director": "Ridley Scott",
        "rating": 8.1
    },
    {
        "id": 3,
        "titulo": "The Matrix",
        "anio": 1999,
        "subgenero": "accion",
        "director": "Wachowski",
        "rating": 8.7
    },
    {
        "id":4,
        "titulo": "interstelar",
        "anio": 2014,
        "subgenero": "ciencia ficcion",
        "director": "Christopher Nolan",
        "rating": 8.6
    }
]

db = SessionLocal()

try:
    for p in peliculas:
        existe = db.query(Pelicula).filter(Pelicula.id == p["id"]).first()
        if not existe:
            pelicula_db = Pelicula(**p)
            db.add(pelicula_db)

    db.commit()
    print("Películas cargadas en SQLite")
finally:
    db.close()
