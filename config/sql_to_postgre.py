import json
import psycopg2
import os

# Connetti al database PostgreSQL
conn = psycopg2.connect(
    host="legalars-app-9yyw9.ondigitalocean.app",
    database="legalars-db",
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS')
)

# Apri il file di backup JSON
with open('blog.json', 'r') as f:
    data = json.load(f)

# Itera sui record nel file JSON e inseriscili nel database PostgreSQL
for record in data:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO blog_categoria (nome, slug) VALUES (%s, %s, %s)",
            (record['nome'], record['slug'])
        )

# Chiudi la connessione al database PostgreSQL
conn.close()
