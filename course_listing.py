import re

textfile = open('course_listing.txt', 'r')
for line in textfile.readlines():
    course_no_match = re.findall("([A-Z]{4} [0-9]{4})", line)
    if course_no_match:
        course_no = course_no_match[0].replace(" ", "")
        print(course_no)