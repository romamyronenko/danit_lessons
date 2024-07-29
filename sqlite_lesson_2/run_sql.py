import sqlite3

# Підключення до БД
conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()

# result = cursor.execute("""
#
# SELECT LessonGroup.id, Groups.Name, Subjects.Title, Days.Name, DaySchedule.Start, DaySchedule.End
# FROM Subjects
# INNER JOIN TeachersSubjects ON TeachersSubjects.id=Subjects.id
# INNER JOIN Lessons ON TeachersSubjects.id=Lessons.TeacherSubjectID
# INNER JOIN LessonGroup ON Lessons.id=LessonGroup.LessonID
# INNER JOIN Groups ON Groups.id=LessonGroup.GroupID
# INNER JOIN Days ON Days.id=Lessons.DayID
# INNER JOIN DaySchedule ON DaySchedule.id=Lessons.DayScheduleID
#
# /* WHERE Groups.Name="Group 1" */
# ;
# """)


result = cursor.execute(
    """

SELECT LessonGroup.id, Groups.Name, Subjects.Title, Days.Name, DaySchedule.Start, DaySchedule.End
FROM Subjects, TeachersSubjects, Lessons, LessonGroup, Groups, Days, DaySchedule
WHERE
TeachersSubjects.id=Subjects.id
AND TeachersSubjects.id=Lessons.TeacherSubjectID
AND Lessons.id=LessonGroup.LessonID
AND Groups.id=LessonGroup.GroupID
AND Days.id=Lessons.DayID
AND DaySchedule.id=Lessons.DayScheduleID

/* WHERE Groups.Name="Group 1" */
;
"""
)

for i in result:
    print(i)
