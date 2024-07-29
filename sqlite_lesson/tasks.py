"""
БД для бібліотеки університету

Вчителі
Студенти
Книги
Записи про взяття/повернення книги


***
Кінотеатр

Фільми
Сеанси
Зали
Квитки
Ціни

***
Онлайн курси

Викладачі
Учні
Розклад уроків, лекцій тощо


"""

from sqlalchemy import create_engine

from models import Base

engine = create_engine("sqlite+pysqlite:///test.db", echo=True)

Base.metadata.create_all(engine)
