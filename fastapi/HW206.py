import hashlib

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Підключення до бази даних MySQL
engine = create_engine("sqlite:///db.db", echo=False)

Base = declarative_base()


# Визначення моделі User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)  # Задано довжину 50
    password = Column(String(64), nullable=False)  # SHA-256 хеш має довжину 64 символи
    email = Column(String(100), unique=True, nullable=False)  # Задано довжину 100


# Визначення моделі SiteRegistration
class SiteRegistration(Base):
    __tablename__ = "site_registrations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_name = Column(String(100), nullable=False)  # Задано довжину 100
    login = Column(String(50))
    password = Column(String(64))
    auth_type = Column(String(20), nullable=False)  # Задано довжину 20
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="registrations")


User.registrations = relationship(
    "SiteRegistration", order_by=SiteRegistration.id, back_populates="user"
)

# Створення таблиць
Base.metadata.create_all(engine)

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()


class UserManager:
    def __init__(self, session: "Session"):
        self.session = session

    def hash_password(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str, email: str):
        hashed_password = self.hash_password(password)
        new_user = User(username=username, password=hashed_password, email=email)
        self.session.add(new_user)
        try:
            self.session.commit()
            print(f"Користувач {username} успішно зареєстрований!")
        except IntegrityError:
            self.session.rollback()
            print("Помилка реєстрації: користувач з таким іменем або email вже існує.")

    def login(self, username, password):
        hashed_password = self.hash_password(password)
        user = (
            self.session.query(User)
            .filter_by(username=username, password=hashed_password)
            .first()
        )
        return user

    def add_site_registration(
        self, user, site_name, auth_type, login=None, password=None
    ):
        new_registration = SiteRegistration(
            site_name=site_name,
            auth_type=auth_type,
            login=login,
            password=password,
            user_id=user.id,
        )
        self.session.add(new_registration)
        self.session.commit()
        print(
            f"Реєстрація на сайті {site_name} успішно додана для користувача {user.username}!"
        )

    def get_user_registrations(self, user):
        registrations = (
            self.session.query(SiteRegistration).filter_by(user_id=user.id).all()
        )
        for reg in registrations:
            print(
                f"Сайт: {reg.site_name}, Тип входу: {reg.auth_type}, Логін: {reg.login}, Пароль: {reg.password}"
            )


def main():
    user_manager = UserManager(session)

    current_user = None

    while True:
        print("Виберіть опцію:")
        if current_user:
            print("1 - Додати реєстрацію на сайті")
            print("2 - Переглянути реєстрації")
            print("3 - Вийти")
        else:
            print("1 - Зареєструватися")
            print("2 - Увійти")
            print("3 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1" and current_user:
            site_name = input("Введіть назву сайту: ")
            auth_type = input("Введіть тип входу (Google, Apple, Facebook або інша): ")
            if auth_type.lower() not in ["google", "apple", "facebook"]:
                login = input("Введіть логін: ")
                password = input("Введіть пароль: ")
            else:
                login = password = None
            user_manager.add_site_registration(
                current_user, site_name, auth_type, login, password
            )
        elif choice == "2" and current_user:
            user_manager.get_user_registrations(current_user)
        elif choice == "3":
            print("До побачення!")
            break
        elif choice == "1":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            email = input("Введіть email: ")
            user_manager.register(username, password, email)
        elif choice == "2":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            user = user_manager.login(username, password)
            if user:
                current_user = user
                print("Успішний вхід!")
            else:
                print("Неправильні дані!")
        else:
            print("Неправильний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
