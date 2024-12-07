import sqlite3
import aioschedule as schedule
from bot import *

conn = sqlite3.connect('Geeks.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Geeks (
    user_id INTEGER PRIMARY KEY,
    time TEXT NOT NULL
)
""")
conn.commit()

async def send_reminder():
    now = datetime.now().strftime('%H:%M')
    cursor.execute('SELECT user_id FROM schedulers WHERE time = ?', (now,))
    users = cursor.fetchall()
    
    for user in users:
        await bot.send_message(user[0], "Пора выполнить задачу!")