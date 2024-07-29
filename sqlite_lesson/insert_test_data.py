import datetime

from sqlalchemy import create_engine, Engine, event
from sqlalchemy.orm import sessionmaker

# Замініть 'sqlite:///test.db' на URL до вашої бази даних
# engine = create_engine('sqlite:///test.db', echo=False)
engine = create_engine("mysql+mysqlconnector://root:hjvfhjvf@localhost", echo=False)

# Імпорт ваших класів моделі
from models import (
    Base,
    Status,
    Person,
    Authors,
    PublishingHouses,
    Books,
    BookAuthor,
    Records,
)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    # cursor.execute("CREATE DATABASE librarydb")  # create db
    cursor.execute("USE librarydb")
    # cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


# Створення таблиць
Base.metadata.create_all(engine)
# with engine.begin() as conn:


# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()


class SessionManager:
    _session: Session

    @property
    def session(self):
        return


class DBManager:
    def __init__(self, engine):
        self._session = Session(engine)

    def create_status(self, name):
        status = Status(name=name)
        session.add(status)
        session.commit()
        return status


db_manager1 = DBManager(...)
db_manager2 = DBManager(...)


class MultipleDBManager:
    def __init__(self, *db_managers):
        self._db_managers = db_managers

    def create_status(self, name):
        for db_manager in self._db_managers:
            db_manager.create_status(name)


# multiple_db_manager.
# Наповнення тестовими даними
try:
    # Створення статусів
    status1 = Status(name="Active")
    status2 = Status(name="Inactive")

    session.add_all([status1, status2])
    session.flush()  # Виконуємо flush для отримання id статусів

    print(f"Status1 ID: {status1.id}, Status2 ID: {status2.id}")

    # Створення осіб
    person1 = Person(last_name="Smith", first_name="John", status_id=status1.id)
    person2 = Person(last_name="Doe", first_name="Jane", status_id=status2.id)

    session.add_all([person1, person2])
    session.flush()  # Виконуємо flush для отримання id осіб

    print(f"Person1 ID: {person1.id}, Person2 ID: {person2.id}")

    # Створення авторів
    author1 = Authors(last_name="Rowling", first_name="J.K.", father_name="")
    author2 = Authors(last_name="Tolkien", first_name="J.R.R.", father_name="")

    session.add_all([author1, author2])
    session.flush()  # Виконуємо flush для отримання id авторів

    print(f"Author1 ID: {author1.id}, Author2 ID: {author2.id}")

    # Створення видавництв
    pub_house1 = PublishingHouses(name="Bloomsbury", city="London")
    pub_house2 = PublishingHouses(name="HarperCollins", city="New York")

    session.add_all([pub_house1, pub_house2])
    session.flush()  # Виконуємо flush для отримання id видавництв

    print(f"PubHouse1 ID: {pub_house1.id}, PubHouse2 ID: {pub_house2.id}")

    # Створення книг
    book1 = Books(
        title="Harry Potter",
        pages=500,
        year=1997,
        is_taking=True,
        publishing_house_id=pub_house1.id,
    )
    book2 = Books(
        title="The Hobbit",
        pages=300,
        year=1937,
        is_taking=True,
        publishing_house_id=pub_house2.id,
    )

    session.add_all([book1, book2])
    session.flush()  # Виконуємо flush для отримання id книг

    print(f"Book1 ID: {book1.id}, Book2 ID: {book2.id}")

    # Створення зв'язків між книгами та авторами
    book_author1 = BookAuthor(book_id=book1.id, author_id=author1.id)
    book_author2 = BookAuthor(book_id=book2.id, author_id=author2.id)

    session.add_all([book_author1, book_author2])
    session.flush()  # Виконуємо flush для отримання id зв'язків

    print(f"BookAuthor1 ID: {book_author1.id}, BookAuthor2 ID: {book_author2.id}")

    # Створення записів про взяття книг
    record1 = Records(
        take_date=datetime.date(2024, 1, 1),
        back_date=datetime.date(2024, 1, 15),
        book_id=book1.id,
        person_id=person1.id,
    )
    record2 = Records(
        take_date=datetime.date(2024, 2, 1),
        back_date=datetime.date(2024, 2, 15),
        book_id=book2.id,
        person_id=person2.id,
    )

    session.add_all([record1, record2])
    session.flush()  # Виконуємо flush для отримання id записів

    print(f"Record1 ID: {record1.id}, Record2 ID: {record2.id}")

    session.commit()
    print("Тестові дані успішно додані!")
except Exception as e:
    session.rollback()
    print(f"Виникла помилка: {e}")
finally:
    session.close()
