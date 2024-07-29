import mysql.connector
from mysql.connector import Error

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register(self):
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                database='user_management',
                user='root',
                password='1111'
            )
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, password, email) VALUES (%s, %s, %s)
                ''', (self.username, self.password, self.email))
                conn.commit()
                conn.close()
                return True
        except Error as e:
            if e.errno == 1062:
                print("Користувач з таким логіном або email вже існує!")
                return False
            else:
                print(f"Error: {e}")
                return False

    @staticmethod
    def login(username, password):
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                database='user_management',
                user='root',
                password='1111'
            )
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute(f'''
                    SELECT * FROM users WHERE username = %s AND password = %s
                ''', (username, password))
                user = cursor.fetchone()
                conn.close()
                return user is not None
        except Error as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def delete_user(username, password, email):
        conn = mysql.connector.connect(
            host='127.0.0.1',
            database='user_management',
            user='root',
            password='1111'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute('''
                            DELETE FROM users WHERE username = %s AND password = %s AND email = %s
                        ''', (username, password, email))
            conn.commit()
            conn.close()
            return True



