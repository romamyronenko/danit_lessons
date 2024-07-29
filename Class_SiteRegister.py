import mysql.connector
from mysql.connector import Error

class SiteRegister:
    def __init__(self, user_id, site_name, login, password, login_type):
        self.user_id = user_id
        self.site_name = site_name
        self.login = login
        self.password = password
        self.login_type = login_type

    def register_site(self):
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
                    INSERT INTO site_registrations (user_id, site_name, login, password, login_type) VALUES (%s, %s, %s, %s, %s)
                ''', (self.user_id, self.site_name, self.login, self.password, self.login_type))
                conn.commit()
                conn.close()
                return True
        except Error as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def get_user_sites(user_id):
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
                    SELECT site_name, login, login_type FROM site_registrations WHERE user_id = %s
                ''', (user_id))
                sites = cursor.fetchall()
                conn.close()
                return sites
        except Error as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def delete_site(site_name, login_type):
        conn = mysql.connector.connect(
            host='127.0.0.1',
            database='user_management',
            user='root',
            password='1111'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute('''
                                DELETE FROM site_registrations WHERE site_name = %s AND login = %s
                            ''', (site_name,login_type))
            conn.commit()
            conn.close()
            return True