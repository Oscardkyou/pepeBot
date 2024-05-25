import psycopg2
import os

def get_connection():
    DATABASE_URL = os.getenv('DATABASE_URL')
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Подключение к базе данных успешно установлено!")
        return conn
    except psycopg2.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id INTEGER UNIQUE,
            username TEXT,
            referral_code TEXT UNIQUE,
            referred_by INTEGER,
            rewards INTEGER DEFAULT 0,
            level INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
