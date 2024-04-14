import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('referral_system.db')
cursor = conn.cursor()


# Создание таблицы для хранения данных о пользователях и рефералах
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT,
    referral_code TEXT UNIQUE,
    referred_by INTEGER,
    rewards INTEGER DEFAULT 0,
    level INTEGER DEFAULT 0
)
''')
conn.commit()


# Обновление уровня пользователя в зависимости от количества наград
def update_user_level(user_id):
    cursor.execute('SELECT rewards FROM users WHERE user_id = ?', (user_id,))
    rewards = cursor.fetchone()[0]
    level = rewards // 10  # Например, новый уровень каждые 10 наград
    cursor.execute('UPDATE users SET level = ? WHERE user_id = ?', (level, user_id))
    conn.commit()


def check_registration(user_id, ):
    # Проверка, зарегистрирован ли уже пользователь
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    if cursor.fetchone() is None:
        # Регистрация нового пользователя
        new_referral_code = generate_referral_code()
        cursor.execute('INSERT INTO users (user_id, username, referral_code) VALUES (?, ?, ?)', (user_id, username, new_referral_code))

        # Если пользователь зарегистрировался по реферальной ссылке
        if referral_code:
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referral_code,))
            referrer = cursor.fetchone()
            if referrer:
                cursor.execute('UPDATE users SET referred_by = ? WHERE user_id = ?', (referrer[0], user_id))
                # Начисление награды рефереру
                cursor.execute('UPDATE users SET rewards = rewards + 1 WHERE user_id = ?', (referrer[0],))
                # Обновление уровня реферера
                update_user_level(referrer[0])

        conn.commit()


# Обработчик для кнопки "Реферальная ссылка"
def get_referal_code(user_id):
   cursor.execute('SELECT referral_code FROM users WHERE user_id = ?', (user_id,))
   referral_code = cursor.fetchone()
   return referral_code

# Обработчик для кнопки "Мои баллы"
def get_rewards(user_id):
   cursor.execute('SELECT rewards FROM users WHERE user_id = ?', (user_id,))
   rewards = cursor.fetchone()
   return rewards