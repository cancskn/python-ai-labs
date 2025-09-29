import sqlite3
import os

# some operations on sqlite3

# db_path = os.path.join(os.getcwd(), "db_sqlite.db")  # or path 
# db_path2 = os.path.join(os.getcwd(), "sample_db.db")

# # connection = sqlite3.connect(db_path)
# # connection = sqlite3.connect(db_path2)

# if os.path.exists(db_path):
#     os.rename(db_path, "example.db")
#     print("name changed")

# if os.path.exists(db_path2):
#     os.remove(db_path2)


# create a db, table 

# db_path3 = os.path.join(os.getcwd(), "student.db")
# connection = sqlite3.connect(db_path3)
# cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE student(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             City TEXT,      
#             Country TEXT,
#             Date_of_birth TEXT,
#             Email TEXT UNIQUE,
#             Contact_number TEXT,
#             group_name TEXT,
#             average_grade REAL,
#             subject_min_avg TEXT,
#             subject_max_avg TEXT
#     );
# """)
# connection.commit()
# connection.close()

# print("table has been created")

# insert data into the table 

# cursor.execute("""
#     INSERT INTO student(
#             full_name ,
#             City ,      
#             Country ,
#             Date_of_birth ,
#             Email ,
#             Contact_number ,
#             group_name ,
#             average_grade ,
#             subject_min_avg ,
#             subject_max_avg
#     ) VALUES("john", "warsaw", "poland", "1954-09-12", "abc@def.com", "123456789", "22B", 90, "history", "computer")
               
# """)
# connection.commit()
# connection.close()
 
# print("data has been filled")


# add data as a list

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# for row in cursor.execute("SELECT *FROM student"):
#     print(row)

data = [("jane", "warsaw", "poland", "1954-09-12", "ikj@def.com", "89898989", "22B", 90, "history", "computer"),
        ("marta", "paris", "france", "1954-09-12", "dfg@def.com", "745896452", "22B", 80, "physics", "math"),
        ("ola", "london", "england", "1954-09-12", "tte@def.com", "454544545", "22B", 70, "chemestry", "biology")
        ]

cursor.executemany("""
INSERT INTO student (
    full_name, city, country, date_of_birth, email, contact_number,
    group_name, average_grade, subject_min_avg, subject_max_avg
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", data)

connection.commit()

