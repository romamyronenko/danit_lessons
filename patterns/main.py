"""
шаблони класів


KISS (Keep It Simple, Stupid)
    "чим простіше тим краще"

    приклад:

    def is_email(s):
        if '.' in s:
            if '@' in s:
                return True
            else:
                return False
        else:
            return False


YAGNI (You Aren't Gonna Need It)
    не робити більше ніж потрібно прямо зараз

    приклад: ви створюєете калькудятор, не потрібно одрзу реалізовувати функції для
    складних операцій, їх можна додати тоді, коли вони знадобляться

SOLID
    Single Responsibility
        принцип єдиної відповідальності
        один об'єкт(функція, клас, метод, змінна) має відповідати за щось одне


        у вас є клас FileReader з методом read(path)
        якщо туди передати посилання на гугл диск - файл прочитається з гугл диску,
        а якщо шлях до локального файлу - прочитається локальний

        класи які зберігають дані(наприклад, контакти) і мають методи add/remove,
        а також зберігання в файл чи завантаження з файлу
        (причини зміни: якщо зміниться формат файлу, якщо зміниться формат даних)

        слід винести функціонал для запису чи читання з файлу в окремий клас або функцію


    Open/Closed
        принцип відкритості/закритості
        код має бути відкритим для розширення та закритим для змін

        приклад: для вашої програми вам потрібно створити FileReader який дозволяє переглядати локальні файли,
        згодом, вам знадобилося переглядати файли на гугл диску

        рішення: створити абстрактний клас FileReader, а потім його наслідувати:
        LocalFileReader, GoogleDriveFileReader

    Liskov Substitution
        принцип підстановки Барьари Лісков
        якщо об'єкт замінити екземпляром підтипу - програма має працювати коректно

        попередній приклад, якщо класи та методи мають однаковий інтерфейс

    Interface Segregation
        принцип розділення інтерфейсів
        великі інтерфейси слід розділяти на більш малі та вузьконаправлені
        інтерфейси мають знати лише про методи, які необхідні їм для роботи

    Dependency Inversion
        модулі більш виского рівня не повинні залежати від модулей нижчого рівня
        і ті і інші мають залежати від абстракцій
        абстракції не мають залежати від деталей реалізації
        деталі реалізації мають залежати від абстракцій


"""

import abc


class SQLite:
    def connect(self, host, port, username, password):
        pass

    def cursor(self, query):
        pass

    def commit(self):
        pass


class MySQLConnector:
    def conn(self, uri):
        pass

    def comm(self):
        pass

    def exec(self, query):
        pass


class BaseBDConnectorAdapter(abc.ABC):
    db: object

    @abc.abstractmethod
    def connect(self, host, port, username, password):
        pass

    @abc.abstractmethod
    def cursor(self, query):
        pass

    @abc.abstractmethod
    def commit(self):
        pass


class SQLiteDBConnectorAdapter(BaseBDConnectorAdapter):
    db = SQLite()

    def connect(self, host, port, username, password):
        self.db.connect(host, port, username, password)

    def cursor(self, query):
        self.db.cursor(query)

    def commit(self):
        self.db.commit()


class MySQLDBConnectorAdapter(BaseBDConnectorAdapter):
    db = MySQLConnector()

    def connect(self, host, port, username, password):
        self.db.conn(f"{host}:{port}@{username}:{password}")

    def cursor(self, query):
        self.db.exec(query)

    def commit(self):
        self.db.comm()


...


class AdapterFactory(abc.ABC):
    @abc.abstractmethod
    def create(self) -> BaseBDConnectorAdapter:
        pass


class MySQLDBConnectorAdapterFactory(AdapterFactory):
    def create(self) -> BaseBDConnectorAdapter:
        return MySQLDBConnectorAdapter()


factory_by_type = {
    "mysql": MySQLDBConnectorAdapterFactory,
    "sqlite": MySQLDBConnectorAdapterFactory,
}

type_ = ""
factory = factory_by_type.get(type_, "DefaultFactory")
db = factory.create()


#
# db.cursor('SELECT * from MY_TABLE')
#
# ...
# from enum import Enum
#
#
# class Colors(Enum):
#     BLACK = 'black'
#     RED = 'red'
#     BLUE = 'blue'
#
#
# class Enemy:
#     def __init__(self, name: str, color: Colors, type: str):
#         self.name = name
#         self.color = color
#         self.type = type
#
#
# black = 'black'
# enemies = []
# enemies.append(Enemy('...', Colors.BLACK, 'robot'))
# enemies.append(Enemy('...', Colors.BLACK, 'robot'))
# enemies.append(Enemy('...', Colors.BLACK, 'robot'))
# enemies.append(Enemy('...', Colors.BLACK, 'robot'))
# enemies.append(Enemy('...', Colors.BLACK, 'robot'))
# enemies.append(Enemy('...', Colors.RED, 'robot'))
# enemies.append(Enemy('...', Colors.BLACK, 'player'))
# enemies.append(Enemy('...', Colors.BLUE, 'player'))
# enemies.append(Enemy('...', Colors.RED, 'player'))
# enemies.append(Enemy('...', Colors.RED, 'player'))
# enemies.append(Enemy('...', Colors.RED, 'player'))
# enemies.append(Enemy('...', Colors.RED, 'player'))
# enemies.append(Enemy('...', Colors.RED, 'player'))
# class SingletonMeta(type):
#     """
#     The Singleton class can be implemented in different ways in Python. Some
#     possible methods include: base class, decorator, metaclass. We will use the
#     metaclass because it is best suited for this purpose.
#     """
#
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         """
#         Possible changes to the value of the `__init__` argument do not affect
#         the returned instance.
#         """
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
#
# class Singleton(metaclass=SingletonMeta):
#     def some_business_logic(self):
#         """
#         Finally, any singleton should define some business logic, which can be
#         executed on its instance.
#         """
#
#         # ...
#
#
# if __name__ == "__main__":
#     # The client code.
#
#     s1 = Singleton()
#     s2 = Singleton()
#
#     if id(s1) == id(s2):
#         print("Singleton works, both variables contain the same instance.")
#     else:
#         print("Singleton failed, variables contain different instances.")


#
# class Singleton:
#     def __new__(cls, *args, **kwds):
#         it = cls.__dict__.get("__it__")
#         if it is not None:
#             return it
#         cls.__it__ = it = super().__new__(cls)
#         it.init(*args, **kwds)
#         return it
#
#     def init(self, *args, **kwds):
#         print(args, kwds)
#
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#
# s1 = Singleton()
# s2 = Singleton()
#
# s1 = Singleton('aaa', x='ased')
# print('args:', s1.args)
# s2 = Singleton('bbb')
# print('args:', s1.args)
# print('args:', s2.args)
# print(id(s1))
# print(id(s2))
# connection = ...
# class A:
#     def foo(self):
#         pass
#
#     def __add__(self, other):
#         pass
#
#
# a = A()
#
# a.foo()


# @dataclass
# class Book:
#     title: str
#     author: str
#     year: str
#     pages: int
#
#     def __copy__(self):
#         return Book(self.title, self.author, self.year, self.pages)

# class A:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __copy__(self):
#         return A(..., ..., ...)
#
#     def __deepcopy__(self, memodict={}):
#         pass
#
#
# a1 = A('asdd', 23, 2)
#
# a2 = copy.copy(a1)
#
# print(a1.a)
# print(a2.a)

# class BaseTextHandler(abc.ABC):
#     next_handler: "BaseTextHandler" = None
#
#     @abc.abstractmethod
#     def _handle(self, text):
#         pass
#
#     def handle(self, text):
#         text = self._handle(text)
#         if self.next_handler:
#             text = self.next_handler.handle(text)
#         return text
#
#     def set_next(self, next_handler):
#         self.next_handler = next_handler
#
#
# class UpperCaseTextHandler(BaseTextHandler):
#     def _handle(self, text):
#         return text.upper()
#
#
# class ReplaceTextHandler(BaseTextHandler):
#     def _handle(self, text):
#         return text.replace('f', ' ')


# def foo(a):
#     print('foo')
#     return 42
#
#
# def boo():
#     print('boo')
#     return 'asd'
#
#
# my_funcs = [
#     foo,
#     boo
# ]
# my_funcs[0](1)


class Request:
    method = "get"
    body_params: dict
    query_params: dict


class RequestFactory:
    def create(self) -> Request:
        pass


class RequestFactory1(RequestFactory):
    pass


class RequestFactory2(RequestFactory):
    pass
