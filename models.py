from sqlalchemy import Column, Integer, String, Float
from database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    subgenero = Column(String, nullable=False)
    director = Column(String, nullable=False)
    rating = Column(Float, nullable=False)



