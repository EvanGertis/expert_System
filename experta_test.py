from experta import *
from random import choice
# https://readthedocs.org/projects/experta/downloads/pdf/stable/
class CSCI_5333(Fact):
    math1441_passed = False
    math2130_passed = False
    csci1310_passed = False
    fall_semester   = False
    """Info about the class"""
    pass

class RegisterForCSCI_5333(KnowledgeEngine):
    @Rule(OR(
                CSCI_5333(MATH1441='C'),
                CSCI_5333(MATH1441='B'),
                CSCI_5333(MATH1441='A')
                ))
    def passed_MATH1441(self):
        CSCI_5333.math1441_passed = True
        print("passed MATH 1441")

    @Rule(OR(
                CSCI_5333(MATH2130='C'),
                CSCI_5333(MATH2130='B'),
                CSCI_5333(MATH2130='A')
                ))
    def passed_MATH2130(self):
        CSCI_5333.math2130_passed = True
        print("passed MATH 2130")
    
    @Rule(OR(
                CSCI_5333(CSCI1301='C'),
                CSCI_5333(CSCI1301='B'),
                CSCI_5333(CSCI1301='A')
                ))
    def passed_CSCI1301(self):
        CSCI_5333.csci1310_passed = True
        print("passed CSCI 1301")
    
    @Rule(CSCI_5333(SEMESTER='F'))
    def is_FallSemester(self):
        CSCI_5333.fall_semester = True
        print("Is registering for fall semester")
    
    def can_register(self):
        if(
            CSCI_5333.csci1310_passed and
            CSCI_5333.math2130_passed and 
            CSCI_5333.math1441_passed and 
            CSCI_5333.fall_semester):
            print("student can register for CSCI 5333")
        else:
            print("student cannot register for CSCI 5333")

engine = RegisterForCSCI_5333()
engine.reset()
engine.declare(CSCI_5333(
    MATH1441=choice(['C','F','A']),
    MATH2130=choice(['C','F','A']),
    CSCI1301=choice(['C','F','A']),
    SEMESTER=choice(['S','SU','F','O'])
    ))
engine.run()