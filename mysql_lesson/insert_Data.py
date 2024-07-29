import mysql.connector
from datetime import datetime, timedelta

# Establish the connection to the database
conn = mysql.connector.connect(
    host="localhost", user="root", password="1", database="social_db"
)
cursor = conn.cursor()

# Insert test data into Profile table
profiles = [
    ("user1@example.com", "password1", "user1", datetime.now()),
    ("user2@example.com", "password2", "user2", datetime.now() - timedelta(days=1)),
    ("user3@example.com", "password3", "user3", datetime.now() - timedelta(days=2)),
    ("user4@example.com", "password4", "user4", datetime.now() - timedelta(days=3)),
    ("user5@example.com", "password5", "user5", datetime.now() - timedelta(days=4)),
    ("user6@example.com", "password6", "user6", datetime.now() - timedelta(days=5)),
    ("user7@example.com", "password7", "user7", datetime.now() - timedelta(days=6)),
    ("user8@example.com", "password8", "user8", datetime.now() - timedelta(days=7)),
    ("user9@example.com", "password9", "user9", datetime.now() - timedelta(days=8)),
    ("user10@example.com", "password10", "user10", datetime.now() - timedelta(days=9)),
]

friends = [
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 8),
    (5, 9),
    (6, 10),
    (7, 8),
    (8, 9),
    (9, 10),
    (10, 1),
]

publications = [
    (1, "First Publication", "Content of the first publication", datetime.now()),
    (
        2,
        "Second Publication",
        "Content of the second publication",
        datetime.now() - timedelta(days=1),
    ),
    (
        3,
        "Third Publication",
        "Content of the third publication",
        datetime.now() - timedelta(days=2),
    ),
    (
        4,
        "Fourth Publication",
        "Content of the fourth publication",
        datetime.now() - timedelta(days=3),
    ),
    (
        5,
        "Fifth Publication",
        "Content of the fifth publication",
        datetime.now() - timedelta(days=4),
    ),
    (
        6,
        "Sixth Publication",
        "Content of the sixth publication",
        datetime.now() - timedelta(days=5),
    ),
    (
        7,
        "Seventh Publication",
        "Content of the seventh publication",
        datetime.now() - timedelta(days=6),
    ),
    (
        8,
        "Eighth Publication",
        "Content of the eighth publication",
        datetime.now() - timedelta(days=7),
    ),
    (
        9,
        "Ninth Publication",
        "Content of the ninth publication",
        datetime.now() - timedelta(days=8),
    ),
    (
        10,
        "Tenth Publication",
        "Content of the tenth publication",
        datetime.now() - timedelta(days=9),
    ),
]

likes = [
    (1, 1),
    (2, 1),
    (1, 2),
    (3, 2),
    (4, 1),
    (5, 2),
    (6, 3),
    (7, 4),
    (8, 5),
    (9, 6),
    (10, 7),
    (1, 8),
    (2, 9),
    (3, 10),
    (4, 1),
    (5, 2),
    (6, 3),
    (7, 4),
    (8, 5),
    (9, 6),
    (10, 7),
    (1, 8),
    (2, 9),
    (3, 10),
]

comments = [
    (1, 1, "First comment on first publication", datetime.now(), False),
    (
        1,
        2,
        "Second comment on first publication",
        datetime.now() - timedelta(hours=1),
        False,
    ),
    (
        2,
        3,
        "First comment on second publication",
        datetime.now() - timedelta(days=1),
        True,
    ),
    (
        2,
        4,
        "Second comment on second publication",
        datetime.now() - timedelta(days=1, hours=1),
        False,
    ),
    (
        3,
        5,
        "First comment on third publication",
        datetime.now() - timedelta(days=2),
        True,
    ),
    (
        3,
        6,
        "Second comment on third publication",
        datetime.now() - timedelta(days=2, hours=1),
        False,
    ),
    (
        4,
        7,
        "First comment on fourth publication",
        datetime.now() - timedelta(days=3),
        True,
    ),
    (
        5,
        8,
        "First comment on fifth publication",
        datetime.now() - timedelta(days=4),
        False,
    ),
    (
        6,
        9,
        "First comment on sixth publication",
        datetime.now() - timedelta(days=5),
        True,
    ),
    (
        7,
        10,
        "First comment on seventh publication",
        datetime.now() - timedelta(days=6),
        False,
    ),
]

comments_answers = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]


for email, password, username, last_seen in profiles:
    cursor.execute(
        """
        INSERT INTO Profile (email, password, username, last_seen)
        VALUES (%s, MD5(%s), %s, %s)
    """,
        (email, password, username, last_seen),
    )

# Insert test data into Friends table

for user1_id, user2_id in friends:
    cursor.execute(
        """
        INSERT INTO Friends (user1_id, user2_id)
        VALUES (%s, %s)
    """,
        (user1_id, user2_id),
    )

# Insert test data into Publications table

for author_id, title, content, publication_date in publications:
    cursor.execute(
        """
        INSERT INTO Publications (author_id, title, content, publication_date)
        VALUES (%s, %s, %s, %s)
    """,
        (author_id, title, content, publication_date),
    )

# Insert test data into Likes table

for publication_id, user_id in likes:
    cursor.execute(
        """
        INSERT INTO Likes (publication_id, user_id)
        VALUES (%s, %s)
    """,
        (publication_id, user_id),
    )

# Insert test data into Comments table


for publication_id, user_id, content, publication_date, is_answer in comments:
    cursor.execute(
        """
        INSERT INTO Comments (publication_id, user_id, content, publication_date, is_answer)
        VALUES (%s, %s, %s, %s, %s)
    """,
        (publication_id, user_id, content, publication_date, is_answer),
    )

# Insert test data into CommentsAnswers table


for parent_id, child_id in comments_answers:
    cursor.execute(
        """
        INSERT INTO CommentsAnswers (parent_id, child_id)
        VALUES (%s, %s)
    """,
        (parent_id, child_id),
    )

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()
