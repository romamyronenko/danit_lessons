"""
питання?

стосовно дз - threadpoolexecutor

sqlalchemy

install
    pip install SQLAlchemy

import sqlalchemy

print(sqlalchemy.__version__)

***

cтворення "рушія"(движка)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)  # dialect+driver://username:password@host:port/database

***
створення з'єднання

сonn = engine.connect()
також підтримується контекстний менеджер
with engine.connect() as conn:
    ...


діалекти
    https://docs.sqlalchemy.org/en/20/dialects/index.html

альтернативний спосіб (не потребує коміту)

with engine.begin() as conn:
    pass

в разі помилки відбувається rollback

***
виконання sql коду

conn.execute(text("CREATE TABLE some_table (x int, y int)"))
conn.commit() # якщо потрібно

***

створення об'єктів метаданих

metadata_obj = MetaData()

***

створення об'єкту таблиці

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

***
про таблицю
user_table.c.name # дані колонки
user_table.c.keys() # імена усіх колонок
user_table.primary_key

***
використання foreign key

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)


***
надсилання в БД

metadata_obj.create_all(engine)

***
metadata.drop_all(engine)

***
створення через класи

from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass


class User(Base):
     __tablename__ = "user_account"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     fullname: Mapped[Optional[str]]

     addresses: Mapped[List["Address"]] = relationship(back_populates="user")

     def __repr__(self) -> str:
         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
     __tablename__ = "address"

     id: Mapped[int] = mapped_column(primary_key=True)
     email_address: Mapped[str]
     user_id = mapped_column(ForeignKey("user_account.id"))

     user: Mapped[User] = relationship(back_populates="addresses")

     def __repr__(self) -> str:
         return f"Address(id={self.id!r}, email_address={self.email_address!r})"


Base.metadata.create_all(engine)


***
insert

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
print(stmt)
compiled = stmt.compile()
compiled.params

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()


***
спосіб 2

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ],
    )
    conn.commit()


***
select

from sqlalchemy import select
stmt = select(user_table).where(user_table.c.name == "spongebob")
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

print(select(user_table.c.name, user_table.c.fullname))
print(select(User))


***
update

from sqlalchemy import bindparam
stmt = (
    update(user_table)
    .where(user_table.c.name == bindparam("oldname"))
    .values(name=bindparam("newname"))
)
with engine.begin() as conn:
    conn.execute(
        stmt,
        [
            {"oldname": "jack", "newname": "ed"},
            {"oldname": "wendy", "newname": "mary"},
            {"oldname": "jim", "newname": "jake"},
        ],
    )

***

update_stmt = (
    update(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
    .values(fullname="Pat")
)
print(update_stmt)
***
delete


from sqlalchemy import delete
stmt = delete(user_table).where(user_table.c.name == "patrick")
print(stmt)

***
сесія
stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)

***
приклади з викоритсанням сесії
https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html


гайд повністю
https://docs.sqlalchemy.org/en/20/index.html

foreign keys pragma
https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
"""

from typing import Optional, List

from sqlalchemy import create_engine, MetaData, String, ForeignKey, insert, update

engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True)
metadata_obj = MetaData()

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


Base.metadata.create_all(engine)

stmt = insert(User).values(name="spongebob", fullname="Spongebob Squarepants")
# print("STMT:", stmt)
compiled = stmt.compile()
# print("PARAMS:", compiled.params)

with engine.begin() as conn:
    result = conn.execute(stmt)

with engine.begin() as conn:
    result = conn.execute(
        insert(User),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ],
    )

from sqlalchemy import select

stmt = select(User).where(User.name == "spongebob")
print("STMT:", stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print("ROW:", row)

print("SELECT 1:", select(User.name, User.fullname))
print("SELECT 2:", select(User))

from sqlalchemy import bindparam

stmt = (
    update(User)
    .where(User.name == bindparam("oldname"))
    .values(name=bindparam("newname"))
)
with engine.begin() as conn:
    conn.execute(
        stmt,
        [
            {"oldname": "jack", "newname": "ed"},
            {"oldname": "wendy", "newname": "mary"},
            {"oldname": "jim", "newname": "jake"},
        ],
    )

from sqlalchemy import delete

stmt = delete(User).where(User.name == "spongebob")
print(stmt)
with engine.begin() as conn:
    conn.execute(stmt)


stmt = select(User)
print("STMT:", stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print("ROW:", row)


stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)


from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


"""




***
select

from sqlalchemy import select
stmt = select(user_table).where(user_table.c.name == "spongebob")
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

print(select(user_table.c.name, user_table.c.fullname))
print(select(User))


***
update

from sqlalchemy import bindparam
stmt = (
    update(user_table)
    .where(user_table.c.name == bindparam("oldname"))
    .values(name=bindparam("newname"))
)
with engine.begin() as conn:
    conn.execute(
        stmt,
        [
            {"oldname": "jack", "newname": "ed"},
            {"oldname": "wendy", "newname": "mary"},
            {"oldname": "jim", "newname": "jake"},
        ],
    )

***

update_stmt = (
    update(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
    .values(fullname="Pat")
)
print(update_stmt)
***
delete
"""
