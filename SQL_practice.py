# SQL practice w Toronto hospital data
from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('practice.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS hospital(
            "Hospital_Id" INTEGER NOT NULL,
            "Hospital_Name" TEXT NOT NULL,
            "Bed_Count" INTEGER,
            PRIMARY KEY("Hospital_Id")
            )"""

cursor.execute(command1)
cursor.execute("""INSERT INTO hospital ('Hospital_Id', 'Hospital_Name', 
'Bed_Count') VALUES
                ('1', 'Toronto General Hospital', '471'),
                ('2', "St. Joseph's Health Centre", '376'),
                ('3', 'Mississauga Hospital', '751'),
                ('4', 'Credit Valley Hospital', '382')""")
cursor.execute("SELECT * FROM hospital")


command2 = """CREATE TABLE "doctor" (
            "Doctor_Id" INTEGER NOT NULL,
            "Doctor_Name" TEXT NOT NULL,
            "Hospital_Id" INTEGER NOT NULL,
            "Joining_Date" TEXT NOT NULL,
            "Speciality" TEXT,
            "Salary" INTEGER,
            "Experience" INTEGER,
            PRIMARY KEY("Doctor_Id")
            );"""
cursor.execute(command2)
command3 = """INSERT INTO 'doctor' 
    ('Doctor_Id', 'Doctor_Name', 'Hospital_Id', 'Joining_Date', 'Speciality', 
'Salary', 'Experience') VALUES
            ('101', 'Duemler', '1', '2005-02-10', 'Pediatric', '140000', NULL),
            ('102', 'McBroom', '1', '2018-07-23', 'Oncologist', '120000', NULL),
            ('103', 'El-Ashry', '2', '2016-05-19', 'Surgeon', '125000', NULL),
            ('104', 'Chan', '2', '2017-12-28', 'Pediatric ', '128000', NULL),
            ('105', 'Platonov', '3', '2004-06-04', 'Psychiatrist', '142000', NULL),
            ('106', 'Izukaw', '3', '2012-09-11', 'Dermatologist', '130000', NULL),
            ('107', 'Jhas', '4', '2014-08-21', 'Obstetrician/Gynecologist', 
'132000', NULL),
            ('108', 'Marmor', '4', '2011-10-17', 'Radiologist', '130000', NULL)"""
cursor.execute(command3)


def exercise1():
    cursor.execute("SELECT * FROM doctor ORDER BY Speciality")
    results = cursor.fetchall()
    print(results)
    for i in results:
        print("Specialty:" + i[4]+" Dr." + i[1])


def exercise2():
    cursor.execute("SELECT * FROM hospital")
    results = cursor.fetchall()
    num = 1
    for i in results:
        print("Hospital#" + str(num) + ": " + i[1])
        num += 1
    choice = ""
    goodInput = False

    while goodInput == False:
        choice = input("Please select a number between 1 and 4 ")

        if choice.isdigit() == False:
            print("Please select a number between 1 and 4  ")
        else:
            if int(choice) < 1:
                print("Please select a number between 1 and 4  ")

            elif int(choice) > 4:
                print("Please select a number between 1 and 4 ")

            else:
                print(results[int(choice)-1])
                goodInput = True

    print('finished')


def exercise3():

    cursor.execute("SELECT * FROM doctor ")
    results = cursor.fetchall()
    doctorYearPairs = []
    for i in results:
        print("year joined:" + str(i[3][0:4])+" Dr." + i[1])
        # //import current date instead of hardcoding 2022 if looking for updating app
        exp = 2022 - int(i[3][0:4])
        doctorYearPairs.append([i[1], exp, i[2]])
    for j in doctorYearPairs:
        print(j[0])
        print(j[1])

    choice = ""
    goodInput = False

    while goodInput == False:
        choice = input("Please select a number for years of experience ")

        if choice.isdigit() == False:
            print("Please select a number for years of experience  ")
        else:
            goodInput = True
    for pair in doctorYearPairs:
        if pair[1] > int(choice):
            print("Doctor: "+pair[0] + " (Hospital:" +
                  str(pair[2])+") Years of experience: " + str(pair[1]))
        else:
            print('.')
    print('finished')


exercise3()
