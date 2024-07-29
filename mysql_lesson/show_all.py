import mysql.connector
from datetime import datetime, timedelta
import hashlib

# Establish the connection to the database
conn = mysql.connector.connect(
    host="localhost", user="root", password="1", database="social_db"
)
cursor = conn.cursor()


# Function to display data from a table
def display_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"\n{table_name}:")
    for row in rows:
        print(row)


# Display all tables
tables = ["Profile", "Friends", "Publications", "Likes", "Comments", "CommentsAnswers"]
for table in tables:
    display_table(table)

# Close the connection
cursor.close()
conn.close()
