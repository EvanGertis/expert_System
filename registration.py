from experta import *
from random import choice
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
    def can_register(
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
        


engine = KE()
engine.reset()
course_no = "CSCI5333"                #input("please enter the course number that you wish to register for: \n")
semester  = choice(['S','SU','F','O']) #input("please enter the semester that you wish to register for S, SU, F or O: \n")
engine.declare(
    prerequisite(course_name='MATH1441', grade='A'),
    prerequisite(course_name='MATH2130', grade='A'),
    prerequisite(course_name='CSCI1301', grade='A'),
    registration(course_name=course_no, semester=semester)
    )
engine.how = True
print("attempting to register for %s during semester %s " % (course_no, semester))
engine.run()