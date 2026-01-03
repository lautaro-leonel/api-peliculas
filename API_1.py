from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, get_db
from models import Base, Pelicula
from typing import Optional
from sqlalchemy import func
from fastapi import Depends


app = FastAPI()

Base.metadata.create_all(bind=engine)

class PeliculaCreate(BaseModel):
    titulo: str
    anio: int
    subgenero: Optional[str] = None
    director: Optional[str] = None
    rating: Optional[float] = None
    

@app.get("/peliculas/{pelicula_id}")
def obtener_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    peli = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if not peli:
        return {"error": "Pelicula no encontrada"}
    return peli


@app.get("/peliculas")
def obtener_peliculas(
    anio: Optional[int] = None,
    subgenero: Optional[str] = None,
    director: Optional[str] = None,
    
    rating_min: Optional[float] = Query(None, ge=0, le=10),
    rating_max: Optional[float] = Query(None, ge=0, le=10),
    
    ordenar_por: str = "anio",   # "anio" o "rating"
    orden: str = "asc",          # "asc" o "desc"
    
    
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),

    db: Session = Depends(get_db)
):
    query = db.query(Pelicula)

    if anio is not None:
        query = query.filter(Pelicula.anio == anio)

    if subgenero is not None:
        query = query.filter(
            func.lower(Pelicula.subgenero) == subgenero.lower()
        )
     
    if director is not None:
        query = query.filter(
            func.lower(Pelicula.director).contains(director.lower())
        )
    
    if rating_min is not None:
        query = query.filter(Pelicula.rating >= rating_min)
             
    if rating_max is not None:
        query = query.filter(Pelicula.rating <= rating_max)   
        
    if ordenar_por not in {"anio", "rating"}:
        raise HTTPException(status_code=400, detail="ordenar_por debe ser 'anio' o 'rating'")

    if orden not in {"asc", "desc"}:
        raise HTTPException(status_code=400, detail="orden debe ser 'asc' o 'desc'")

    columna = Pelicula.anio if ordenar_por == "anio" else Pelicula.rating
    query = query.order_by(columna.asc() if orden == "asc" else columna.desc())     


    offset = (page - 1) * size
    query = query.offset(offset).limit(size)
    


    return query.all()

@app.put("/peliculas/{pelicula_id}")
def actualizar_pelicula(
    pelicula_id: int,
    pelicula: dict,
    db: Session = Depends(get_db)
):
    peli_db = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()

    if not peli_db:
        return {"error": "Pelicula no encontrada"}

    peli_db.titulo = pelicula.titulo
    peli_db.anio = pelicula.anio
    peli_db.subgenero = pelicula.subgenero
    peli_db.director = pelicula.director
    peli_db.rating = pelicula.rating

    db.commit()
    db.refresh(peli_db)

    return peli_db


@app.post("/peliculas")
def crear_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    nueva = Pelicula(
        titulo=pelicula.titulo,
        anio=pelicula.anio,
        subgenero=pelicula.subgenero,
        director=pelicula.director,
        rating=pelicula.rating
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@app.get("/")
def inicio(db):
    return db.query(Pelicula).all()
