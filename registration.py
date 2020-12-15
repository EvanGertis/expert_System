from experta import *
from random import choice
# https://readthedocs.org/projects/experta/downloads/pdf/stable/


class prerequisite(Fact):
    pass


class registration(Fact):
    pass


class KE(KnowledgeEngine):
    @Rule(
        AND(
            registration(course_name="CSCI5333", semester='F'),
            prerequisite(course_name='MATH1441', grade=L('C') | L('B') | L('A')),
            prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A')),
            prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register(self):
        print("registering")


engine = KE()
engine.reset()
course_no = "CSCI5333"                #input("please enter the course number that you wish to register for: \n")
semester  = choice(['S','SU','F','O']) #input("please enter the semester that you wish to register for S, SU, F or O: \n")
engine.declare(
    prerequisite(course_name='MATH1441', grade=choice(['A','B','C','F'])),
    prerequisite(course_name='MATH2130', grade=choice(['A','B','C','F'])),
    prerequisite(course_name='CSCI1301', grade=choice(['A','B','C','F'])),
    registration(couse_name=course_no, semester=semester))
engine.run()
print("attempting to register for %s during semester %s " % (course_no, semester))
engine.can_register()