"""
title1
    user1
    10.10.1220
    
    conteasdasdasdasdawesfasdfsadf
    
    
    likes: 20
    
    comments:
        user1: 12e123eqwDFWERTFEWF23RF
        user2: 12e123eqwDFWERTFEWF23RF
    
        


"""

import datetime
from dataclasses import dataclass

import mysql.connector

# Establish the connection to the database
conn = mysql.connector.connect(
    host="localhost", user="root", password="1", database="social_db"
)
cursor = conn.cursor()

cursor.execute(
    """
SELECT Pr.username, Pub.id, Pub.title, Pub.content, Pub.publication_date
FROM `Publications` AS Pub, `Profile` AS Pr
WHERE Pr.id=Pub.author_id
LIMIT 1
;

"""
)


@dataclass
class Comment:
    username: str
    content: str
    publication_date: datetime.datetime
    is_answer: bool
    id: int

    _answers = None

    @property
    def answers(self):
        return self._answers

    def add_answer(self, answer):
        if self._answers is None:
            self._answers = []
        self._answers.append(answer)

    @classmethod
    def create(cls, data):
        return cls(
            username=data[0],
            content=data[1],
            publication_date=data[2],
            is_answer=data[3],
            id=data[4],
        )

    def show(self, shift=0):
        tabs = "\t" * shift
        print(
            f"{tabs}{self.username}:\n{tabs}\t{self.publication_date}\n{tabs}\t{self.content}"
        )
        if self._answers:
            print(f"{tabs}answers:")
            for answer in self._answers:
                answer.show(shift + 1)


def get_comments(publication_id):
    cursor.execute(
        f"""
    SELECT P.username, C.content, C.publication_date, C.is_answer, C.id
    FROM `Profile` AS P, `Comments` AS C
    WHERE C.publication_id={publication_id} AND C.user_id=P.id;
    """
    )
    comment_by_id = {}

    comments = []
    for comment_data in cursor.fetchall():

        comment = Comment.create(comment_data)
        comment_by_id[comment.id] = comment

        if comment.is_answer:
            # get_parent_comment_id
            cursor.execute(
                f"""
            SELECT parent_id
            FROM CommentsAnswers
            WHERE child_id={comment.id}
            """
            )
            parent_id = cursor.fetchone()[0]

            # get_parent_comment_instance_by_id
            parent = comment_by_id.get(parent_id)

            # parent_comment.add_answer(comment)
            if parent:
                parent.add_answer(comment)
        else:
            comments.append(comment)

        # if item["is_answer"]:
        #     answers.append(item)
        # else:
        #     comments.append(item)

    return comments


for publication_data in cursor.fetchall():
    owner, publication_id, title, content, creation_date = publication_data

    print(title)
    print(f"\t{owner}")
    print(f"\t{creation_date}")
    print(f"\t\t{content}")

    cursor.execute(
        f"""
    SELECT COUNT(id)
    FROM `Likes` 
    WHERE publication_id={publication_id}
    ;
    """
    )
    likes_count = cursor.fetchone()[0]
    print(f"\n\t\tLikes: {likes_count}")

    comments = get_comments(publication_id)

    for comment in comments:
        comment.show()

    print()
