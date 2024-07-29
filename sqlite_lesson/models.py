import datetime

from sqlalchemy import VARCHAR, ForeignKey, Integer, BOOLEAN, DATE
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(30))

    persons: Mapped[list["Person"]] = relationship(back_populates="status")

    def __repr__(self) -> str:
        return f"Status(id={self.id}, name={self.name})"


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(VARCHAR(30))
    first_name: Mapped[str] = mapped_column(VARCHAR(30))
    status_id = mapped_column(ForeignKey("status.id"))

    status: Mapped["Status"] = relationship(back_populates="persons")

    records: Mapped[list["Records"]] = relationship(back_populates="person")

    def __repr__(self) -> str:
        return f"Person(id={self.id}, full_name={self.last_name}, first_name={self.first_name}, status_id={self.status_id})"


class Authors(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(VARCHAR(30))
    first_name: Mapped[str] = mapped_column(VARCHAR(30))
    father_name: Mapped[str] = mapped_column(VARCHAR(30))

    book_authors: Mapped[list["BookAuthor"]] = relationship(back_populates="author")


class PublishingHouses(Base):
    __tablename__ = "publishing_houses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(30))
    city: Mapped[str] = mapped_column(VARCHAR(30))

    books: Mapped[list["Books"]] = relationship(back_populates="publishing_house")


class Books(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(30))
    pages: Mapped[int] = mapped_column(Integer())
    year: Mapped[int] = mapped_column(Integer())
    is_taking: Mapped[bool] = mapped_column(BOOLEAN())

    publishing_house_id = mapped_column(ForeignKey("publishing_houses.id"))

    publishing_house: Mapped["PublishingHouses"] = relationship(back_populates="books")

    book_authors: Mapped[list["BookAuthor"]] = relationship(back_populates="book")
    records: Mapped[list["Records"]] = relationship(back_populates="book")


class BookAuthor(Base):
    __tablename__ = "book_author"
    id: Mapped[int] = mapped_column(primary_key=True)

    book_id = mapped_column(ForeignKey("book.id"))
    author_id = mapped_column(ForeignKey("authors.id"))

    book: Mapped["Books"] = relationship(back_populates="book_authors")
    author: Mapped["Authors"] = relationship(back_populates="book_authors")


class Records(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    take_date: Mapped["datetime.date"] = mapped_column(DATE())
    back_date: Mapped["datetime.date"] = mapped_column(DATE())

    book_id = mapped_column(ForeignKey("book.id"))
    person_id = mapped_column(ForeignKey("person.id"))

    book: Mapped["Books"] = relationship(back_populates="records")
    person: Mapped["Person"] = relationship(back_populates="records")
