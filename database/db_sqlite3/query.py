# Displaying of all data from the table about students and grades;
 
import sqlite3
import os
 
db_path = os.path.join(os.getcwd(), "student.db")
 
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
 
# for row in cursor.execute("SELECT * FROM student"):
#     print(row)
 
# Displaying the full name of all the students;
# for row in cursor.execute("SELECT full_name FROM student"):
#     print(row)
 
# Displaying of all average marks;
# for row in cursor.execute("SELECT average_grade FROM student"):
#     print(row)
 
# # Show the full names of all the students with a minimum mark but higher than the specified one;
# specific_marks = int(input("marks :"))
# for row in cursor.execute("SELECT full_name FROM student WHERE average_grade > ? ;", (specific_marks,)):
#     print(row)
 
# Show the countries of the students. Country names should be unique;
# for row in cursor.execute("SELECT DISTINCT country FROM student"):
#     print(row)
 
# Show the students' cities. City names should be unique;
# for row in cursor.execute("SELECT DISTINCT city FROM student"):
#     print(row)
 
# Show group names. Group names should be unique;
# for row in cursor.execute("SELECT DISTINCT group_name FROM student"):
#     print(row)
 
# Show the name of all subjects with the minimum average marks. The names of the subjects should be unique.
# for row in cursor.execute("SELECT DISTINCT subject_min_avg FROM student"):
#     print(row)