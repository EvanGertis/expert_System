from experta import *
from random import choice
# https://readthedocs.org/projects/experta/downloads/pdf/stable/


class prerequisite(Fact):
    pass


class time_of_registration(Fact):
    pass


class Registration(KnowledgeEngine):
    @Rule(
        AND(
            OR(
                prerequisite(course_name='MATH1441', grade='C'),
                prerequisite(course_name='MATH1441', grade='B'),
                prerequisite(course_name='MATH1441', grade='A')
            ),
            OR(
                prerequisite(course_name='MATH2130', grade='C'),
                prerequisite(course_name='MATH2130', grade='B'),
                prerequisite(course_name='MATH2130', grade='A')
            ),
            OR(
                prerequisite(course_name='CSCI1301', grade='C'),
                prerequisite(course_name='CSCI1301', grade='B'),
                prerequisite(course_name='CSCI1301', grade='A')
            ),
            time_of_registration(SEMESTER='F')
        )
    )
    def can_register(self):
        print("student can register")


engine = Registration()
engine.reset()
engine.declare(
    prerequisite(course_name='MATH1441', grade='C'),
    prerequisite(course_name='MATH2130', grade='C'),
    prerequisite(course_name='CSCI1301', grade='C'),
    time_of_registration(SEMESTER='F'))
engine.run()
engine.can_register()