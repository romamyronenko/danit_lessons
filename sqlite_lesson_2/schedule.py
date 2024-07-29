import sqlite3

# Підключення до БД
conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()

# Створення таблиць
cursor.executescript(
    """
CREATE TABLE IF NOT EXISTS `Groups` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `Name` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Students` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `FirstName` TEXT NOT NULL,
    `LastName` TEXT NOT NULL,
    `GroupID` INTEGER NOT NULL,
    FOREIGN KEY(`GroupID`) REFERENCES `Groups`(`id`)
);
CREATE TABLE IF NOT EXISTS `Teachers` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `FirstName` TEXT NOT NULL,
    `LastName` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Subjects` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `Title` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `TeachersSubjects` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `TeacherID` INTEGER NOT NULL,
    `SubjectID` INTEGER NOT NULL,
    FOREIGN KEY(`TeacherID`) REFERENCES `Teachers`(`id`),
    FOREIGN KEY(`SubjectID`) REFERENCES `Subjects`(`id`)
);
CREATE TABLE IF NOT EXISTS `Lessons` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `TeacherSubjectID` INTEGER NOT NULL,
    `DayID` INTEGER NOT NULL,
    `DayScheduleID` INTEGER NOT NULL,
    FOREIGN KEY(`TeacherSubjectID`) REFERENCES `TeachersSubjects`(`id`),
    FOREIGN KEY(`DayID`) REFERENCES `Days`(`id`),
    FOREIGN KEY(`DayScheduleID`) REFERENCES `DaySchedule`(`id`)
);
CREATE TABLE IF NOT EXISTS `Days` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `Name` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `DaySchedule` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `Start` TEXT NOT NULL,
    `End` TEXT NOT NULL,
    `Number` INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS `LessonGroup` (
    `id` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `GroupID` INTEGER NOT NULL,
    `LessonID` INTEGER NOT NULL,
    FOREIGN KEY(`GroupID`) REFERENCES `Groups`(`id`),
    FOREIGN KEY(`LessonID`) REFERENCES `Lessons`(`id`)
);
"""
)

# Вставка тестових даних
groups = [
    (1, "Group 1"),
    (2, "Group 2"),
    (3, "Group 3"),
    (4, "Group 4"),
    (5, "Group 5"),
]

students = [
    (1, "John", "Doe", 1),
    (2, "Jane", "Smith", 2),
    (3, "Emily", "Johnson", 3),
    (4, "Michael", "Brown", 4),
    (5, "Sarah", "Davis", 5),
    (6, "David", "Wilson", 1),
    (7, "Linda", "Taylor", 2),
    (8, "James", "Anderson", 3),
    (9, "Patricia", "Thomas", 4),
    (10, "Robert", "Jackson", 5),
]

teachers = [
    (1, "Alice", "Johnson"),
    (2, "Bob", "Brown"),
    (3, "Charlie", "Davis"),
    (4, "Diana", "Miller"),
    (5, "Edward", "Wilson"),
]

subjects = [
    (1, "Math"),
    (2, "History"),
    (3, "Science"),
    (4, "Literature"),
    (5, "Art"),
    (6, "Music"),
    (7, "Physical Education"),
    (8, "Geography"),
    (9, "Computer Science"),
    (10, "Chemistry"),
]

teachers_subjects = [
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 1, 6),
    (7, 2, 7),
    (8, 3, 8),
    (9, 4, 9),
    (10, 5, 10),
]

days = [(1, "Monday"), (2, "Tuesday"), (3, "Wednesday"), (4, "Thursday"), (5, "Friday")]

day_schedule = [
    (1, "08:00", "09:30", 1),
    (2, "09:45", "11:15", 2),
    (3, "11:30", "13:00", 3),
    (4, "13:15", "14:45", 4),
    (5, "15:00", "16:30", 5),
    (6, "16:45", "18:15", 6),
    (7, "18:30", "20:00", 7),
]

lessons = [
    (1, 1, 1, 1),
    (2, 2, 2, 2),
    (3, 3, 3, 3),
    (4, 4, 4, 4),
    (5, 5, 5, 5),
    (6, 6, 1, 2),
    (7, 7, 2, 3),
    (8, 8, 3, 4),
    (9, 9, 4, 5),
    (10, 10, 5, 6),
    (11, 1, 1, 7),
    (12, 2, 2, 1),
    (13, 3, 3, 2),
    (14, 4, 4, 3),
    (15, 5, 5, 4),
]

lesson_group = [
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 1, 6),
    (7, 2, 7),
    (8, 3, 8),
    (9, 4, 9),
    (10, 5, 10),
    (11, 1, 11),
    (12, 2, 12),
    (13, 3, 13),
    (14, 4, 14),
    (15, 5, 15),
]


cursor.executemany("INSERT INTO Groups (id, Name) VALUES (?, ?)", groups)
cursor.executemany(
    "INSERT INTO Students (id, FirstName, LastName, GroupID) VALUES (?, ?, ?, ?)",
    students,
)
cursor.executemany(
    "INSERT INTO Teachers (id, FirstName, LastName) VALUES (?, ?, ?)", teachers
)
cursor.executemany("INSERT INTO Subjects (id, Title) VALUES (?, ?)", subjects)
cursor.executemany(
    "INSERT INTO TeachersSubjects (id, TeacherID, SubjectID) VALUES (?, ?, ?)",
    teachers_subjects,
)
cursor.executemany("INSERT INTO Days (id, Name) VALUES (?, ?)", days)
cursor.executemany(
    "INSERT INTO DaySchedule (id, Start, End, Number) VALUES (?, ?, ?, ?)", day_schedule
)
cursor.executemany(
    "INSERT INTO Lessons (id, TeacherSubjectID, DayID, DayScheduleID) VALUES (?, ?, ?, ?)",
    lessons,
)
cursor.executemany(
    "INSERT INTO LessonGroup (id, GroupID, LessonID) VALUES (?, ?, ?)", lesson_group
)

# Збереження змін
conn.commit()

# res = cursor.execute()

# Закриття з'єднання
conn.close()
