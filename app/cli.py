import os
import sys

import typer

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import Base, engine, get_db
from services.user_service import insert_primary_presence

app = typer.Typer()


@app.command()
def init_db():
    Base.metadata.create_all(bind=engine)
    typer.echo("Banco de dados inicializado.")


@app.command()
def insert_data_primary_presence(interval: str):
    db = next(get_db())
    insert_primary_presence(db, interval)
    typer.echo("Dados inseridos na tabela primary presence.")


if __name__ == "__main__":
    app()
