from MyConnection import mydb
from MyConnection import mysql
from datetime import datetime

class Student:
    mydb = mydb
    myData = mydb.cursor() 

    def __init__(self,studentNo,studentName,studentSurname,studentBirthDay,studentGender):
        self.studentNo = studentNo
        self.studentName = studentName
        self.studentSurname = studentSurname
        self.studentBirthDay = studentBirthDay
        self.studentGender = studentGender

    def saveStudent(self):
        sql = "INSERT INTO student(StudentNo,StudentName,StudentSurname,StudentBirthDay,StudentGender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNo,self.studentName,self.studentSurname,self.studentBirthDay,self.studentGender)
        Student.myData.execute(sql,value)

        try:
            Student.mydb.commit()
            print(f"{Student.myData.rowcount} tane kayıt eklendi.")
        except mysql.Error as err:
            print("hata: " , err)
        finally:
            Student.mydb.close()

    @staticmethod    
    def saveStudents(students):
        sql = "INSERT INTO student(StudentNo,StudentName,StudentSurname,StudentBirthDay,StudentGender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.myData.executemany(sql,values)

        try:
            Student.mydb.commit()
            print(f"{Student.myData.rowcount} tane kayıt eklendi.")
        except mysql.Error as err:
            print("hata: " , err)
        finally:
            Student.mydb.close()

ogrenciler = [
    ("105","Ceylin","TOSUN",datetime(2006,6,20),"K"),
    ("107","Celal","Akagündüz",datetime(2008,6,20),"E")
]

Student.saveStudents(ogrenciler)