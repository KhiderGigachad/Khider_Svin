# database.py
# Здесь разместите ваши данные для подключения к PostgreSQL

DB_HOST = '46.32.185.109'
DB_PORT = "5432"
DB_NAME = "Khider_Svin"
DB_USER = "postgres"
DB_PASSWORD = "rtqnkby662621"

import psycopg2

def get_connection():
    """
    Возвращает новое соединение с базой данных PostgreSQL
    """
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )