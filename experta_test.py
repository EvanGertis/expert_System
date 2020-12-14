from experta import *
from random import choice

class CSCI_5333(Fact):
    """Info about the class"""
    pass

class RegisterForCSCI_5333(KnowledgeEngine):
    @Rule(CSCI_5333(MATH1441='C'))
    def passed_MATH1441(self):
        print("passed MATH 1441")

    @Rule(CSCI_5333(MATH2130='C'))
    def passed_MATH2130(self):
        print("passed MATH 2130")
    
    @Rule(CSCI_5333(CSCI1301='C'))
    def passed_CSCI1301(self):
        print("passed CSCI 1301")
    
    @Rule(CSCI_5333(SEMESTER='F'))
    def is_FallSemester(self):
        print("Is registering for fall semester")
    
    @Rule(AND(CSCI_5333(MATH1441='C'), CSCI_5333(MATH2130='C'), CSCI_5333(CSCI1301='C'), CSCI_5333(SEMESTER='F')))
    def can_register(self):
        print("student can register for CSCI 5333")

engine = RegisterForCSCI_5333()
engine.reset()
# engine.declare(CSCI_5333(
#     MATH1441=choice(['C','F','A']),
#     MATH2130=choice(['C','F','A']),
#     CSCI1301=choice(['C','F','A']),
#     SEMESTER=choice(['S','SU','F','O'])
#     ))
engine.declare(CSCI_5333(
    MATH1441='C',
    MATH2130='C',
    CSCI1301='C',
    SEMESTER='F'
    ))
engine.run()