from experta import *
from random import choice
import re
# https://readthedocs.org/projects/experta/downloads/pdf/stable/


class prerequisite(Fact):
    pass


class registration(Fact):
    pass


class KE(KnowledgeEngine):

    how = False
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5333", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='MATH1441', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A')),
            AS.prerequisite3 << prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5333(
        self, 
        registration, 
        prerequisite1,
        prerequisite2,
        prerequisite3):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Since ", prerequisite3['course_name']," was passed with ", prerequisite3['grade'])
            print("Registering for: ",registration["course_name"]," during semester: ",registration['semester'])
        else:
            print("Registering for: ",registration["course_name"]," during semester: ",registration['semester'])

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3341", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI2940', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A')),
        )
    )
    def can_register_CSCI3341(
        self, 
        registration, 
        prerequisite1,
        prerequisite2,
        prerequisite3):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Registering for: ",registration["course_name"]," during semester: ",registration['semester'])
        else:
            print("Registering for: ",registration["course_name"]," during semester: ",registration['semester'])

##################################
#         Build Knowledge Base   #
##################################
        
engine = KE()
engine.reset()
transcript = open('transcript.txt', 'r')
for line in transcript.readlines():
    print(line)
    print("__Reading transcript___")
    course_no_match = re.findall("([A-Z]{4} [0-9]{4})", line)
    grade_match = re.findall("( [A-Z]{1})", line)[0].replace(" ", "")
    if course_no_match and grade_match:
        course_no = course_no_match[0].replace(" ", "")
        grade = grade_match[0].replace(" ", "")
        print("Adding course: ", course_no, "grade :", grade, "to Knowledge Base")
        engine.declare(prerequisite(course_name=course_no, grade=grade))

##################################
#         Build Working Memory   #
##################################

course_no = "CSCI3341"                #input("please enter the course number that you wish to register for: \n")
semester  = choice(['S','SU','F','O']) #input("please enter the semester that you wish to register for S, SU, F or O: \n")
engine.how = True


##################################
#         Run Inference Engine   #
##################################

print("Attempting to register for %s during semester %s " % ("CSCI5333", 'F'))
engine.run()