from Class_User import User
from Class_SiteRegister import SiteRegister
import mysql.connector
from mysql.connector import Error
import re
from post import send_email
import random

def create_code():
    digits = '123456789'
    code = ''.join(random.choice(digits) for _ in range(5))
    return code

def is_gmail_correct(email):
    pattern = r'@gmail\.com$'
    return re.search(pattern, email) is not None


def main():
    while True:
        print("Виберіть опцію:")
        print("1 - Зареєструватися")
        print("2 - Увійти")
        print("3 - Видалити користувача")
        print("4 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            email = input("Введіть email: ")
            if is_gmail_correct(email):
                code = create_code()
                send_email(email, code)
                code_confirmation = str(input('Введіть код підтвердження: '))
                if code_confirmation == code:
                    user = User(username, password, email)
                    if user.register():
                        print("Реєстрація пройшла успішно!")
                    else:
                        print("Користувач з таким ім'ям або email вже існує!")
                else:
                    print("Неправильний код")
            else:
                print("Неправильний емейл")

        elif choice == "2":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")

            if User.login(username, password):
                print("Успішний вхід!")
                user_id = get_user_id(username)
                while True:
                    print("Виберіть опцію:")
                    print("1 - Додати сайт")
                    print("2 - Переглянути сайти")
                    print("3 - Видалити сайт")
                    print("4 - Повернутись назад")

                    site_choice = input("Ваш вибір: ")

                    if site_choice == "1":
                        site_name = input("Введіть назву сайту: ")
                        login_type = input("Введіть тип входу (Google, Apple, Facebook, Інше): ")

                        if login_type == "Google" or login_type == "Apple" or login_type == "Facebook":
                            login = ""
                            password = ""
                        else:
                            login = input("Введіть логін: ")
                            password = input("Введіть пароль: ")

                        site = SiteRegister(user_id, site_name, login, password, login_type)
                        if site.register_site():
                            print("Сайт додано успішно!")
                        else:
                            print("Помилка при додаванні сайту!")
                    elif site_choice == "2":
                        sites = SiteRegister.get_user_sites(user_id)
                        if sites:
                            for site in sites:
                                print(f"Сайт: {site[0]}, Логін: {site[1]}, Тип входу: {site[2]}")
                        else:
                            print("Помилка при отриманні списку сайтів!")
                    elif site_choice == "3":
                        site_name = input("Введіть назву сайту")
                        login_type = input("Введіть тип входу (Google, Apple, Facebook, Інше): ")
                        if SiteRegister.delete_site(site_name, login_type):
                            print("Сайт успішно видалено!")
                        else:
                            print("Невдача(")
                    elif site_choice == "4":
                        break
                    else:
                        print("Невідома опція! Спробуйте ще раз.")
            else:
                print("Неправильні дані!")
        elif choice == "3":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            email = input("Введіть email: ")

            if User.delete_user(username, password, email):
                print("Користувача успішно видалено")
            else:
                print("Невірний нікнейм, пароль чи емейл. Можливо проблема з підключенням")
        elif choice == "4":
            print("My message is: goodbye...")
            break
        else:
            print("Невідома опція! Спробуйте ще раз.")

def get_user_id(username):
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
                SELECT id FROM users WHERE username = %s
            ''', (username,))
            user_id = cursor.fetchone()
            conn.close()
            return user_id[0] if user_id else None
    except Error as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()
