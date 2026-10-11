from sqlalchemy import create_engine, String, Text, Integer, Boolean, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional
import os
from dotenv import load_dotenv

# classe "base"
class Base(DeclarativeBase):
    pass

class Genero(Base):
    __tablename__ = "tabela_genero"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    jogabilidade: Mapped[str] = mapped_column(Text)
    exige_jogar_online: Mapped[bool] = mapped_column(Boolean, default=False)
    publico_alvo: Mapped[str] = mapped_column(String(50))
    jogo: Mapped[List["Jogo"]] = relationship(back_populates="genero")




class Jogo(Base):
    __tablename__ = "tabela_de_jogos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    desenvolvedora: Mapped[str] = mapped_column(String(250))
    ano_lancamento: Mapped[int] = mapped_column(Integer)
    preco: Mapped[float] = mapped_column(Numeric(10, 2))
    genero: Mapped[Genero] = relationship(back_populates="jogo")

    




