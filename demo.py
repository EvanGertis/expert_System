import csv
import pprint

semeseter_description = "a code of [S], [SU], [F] and [O] that indicates the semester that the CS department offers the course. And these codes stand for the semester “Spring”, “Summer”, “Fall”, and “all semesters”, respectively."
input_courses = {}
input_courses["course"] = {}
courses = []
with open('courses.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',',quotechar='"')

    for row in csvreader:
        print(row)

val = ""
while(val != "q"):
    val = input("Enter your course number that you wish to register for or 'q' to quit \n")
    if val == "q":
        break
    input_courses["course"]["course_number"] = val  
    print(semeseter_description)
    val = input("Enter your semester that you wish to register for or 'q' to quit \n")
    input_courses["course"]["semester_code"] = val 
    if val == "q":
        break

print(input_courses)