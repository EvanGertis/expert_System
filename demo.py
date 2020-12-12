import csv
import pprint

semeseter_description = "a code of [S], [SU], [F] and [O] that indicates the semester that the CS department offers the course. And these codes stand for the semester “Spring”, “Summer”, “Fall”, and “all semesters”, respectively."
input_courses = {}
input_courses["course"] = {}
courses = {}
courses["course"] = {}
# TODO: transform courses.txt to csv and initialize courses object
with open('courses.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',',quotechar='"')

    for row in csvreader:
        courses["course"]["course_number"] = row["course_number"]
        courses["course"]["course_title"]  = row["course_title"] 
        courses["course"]["semester_code"] = row["semester_code"]
        courses["course"]["prerequisite"]  = row["prerequisite"]

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

val = ""
prerequisite_courses = {}
prerequisite_courses["course"] = {}
# test case with CSCI 1301
while(val != "q"):
    if(courses["course"]["course_number"] == input_courses["course"]["course_number"]):
        val = input("Did you take " + courses["course"]["prerequisite"] + " Y/N? or 'q' to quit \n")
        if val == "q":
            break
        if val == "N":
            # TODO get course WHERE course number matches prerequisite course number.
            prerequisite_courses["course"]["course_number"] = courses["course"]["prerequisite"]
            break

print("According to our analysis you should take: ")
pprint.pprint(prerequisite_courses)