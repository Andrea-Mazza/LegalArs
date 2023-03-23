import json
import psycopg2
from django.core.management.base import BaseCommand
from django.conf import settings
from blog.models import Categoria, Articolo, FontiCategoria, Fonti


def import_data():
    # Connessione al database PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myusername",
        password="mypassword"
    )

    # Apertura del file di backup JSON
    with open('blog.json') as f:
        data = json.load(f)

    # Ciclo for per importare i dati del modello Categoria
    for record in data['categoria']:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO myapp_categoria (nome, slug) VALUES (%s, %s)",
            (record['nome'], record['slug'])
        )
        cur.close()

    # Ciclo for per importare i dati del modello Articolo
    for record in data['articolo']:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO myapp_articolo (titolo, slug, copertina, corpo, descrizione, categoria_id, publish, autore_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (record['titolo'], record['slug'], record['copertina'], record['corpo'],
             record['descrizione'], record['categoria_id'], record['publish'], record['autore_id'])
        )
        cur.close()

    # Ciclo for per importare i dati del modello FontiCategoria
    for record in data['fonticategoria']:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO myapp_fonticategoria (nome, slug) VALUES (%s, %s)",
            (record['nome'], record['slug'])
        )
        cur.close()

    # Ciclo for per importare i dati del modello Fonti
    for record in data['fonti']:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO myapp_fonti (titolo, sotto_titolo, slug, corpo, descrizione, categoria_id, publish, autore_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (record['titolo'], record['sotto_titolo'], record['slug'], record['corpo'],
             record['descrizione'], record['categoria_id'], record['publish'], record['autore_id'])
        )
        cur.close()

    # Commit delle modifiche al database
    conn.commit()

    # Chiusura della connessione al database
    conn.close()


if __name__ == '__main__':
    import_data()
