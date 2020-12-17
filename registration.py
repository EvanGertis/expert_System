from experta import *
from random import choice
import sys
import re
# https://readthedocs.org/projects/experta/downloads/pdf/stable/


class prerequisite(Fact):
    pass


class registration(Fact):
    pass

class isAvaibleForRegistration(Fact):
    pass


class KE(KnowledgeEngine):

    how = False
    results = open("results.txt", 'w')

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI1301", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='MATH1441', grade=L('C') | L('B') | L('A'))
        )
        
    )
    def can_register_CSCI1301(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI1302", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='MATH1441', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A')),
            AS.prerequisite3 << prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI1302(
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
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI2120", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='COMM110', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI2120(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI2490", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI2490(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3230", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3230(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3231", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3231(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    # TODO: what to do about prior or concurrent enrollment
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3232", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3232(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3236", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3236(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3330", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI2490', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3232', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3330(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3341", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI2490', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3341(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI3432", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI3342(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4132", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3432', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4132(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4210", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3341', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4210(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4220", semester='F')
        )
    )
    def can_register_CSCI4220(
        self, 
        registration):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4235", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4235(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4235", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4235(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4322", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI2130', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4322(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4342", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3341', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4342(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4343", semester='SU'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3341', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4343(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4350", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3341', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4350(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4360", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4360(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4370", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4370(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4410", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI12242', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4410(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4439", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4439(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4520", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI2490', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3232', grade=L('C') | L('B') | L('A')),
            AS.prerequisite3 << prerequisite(course_name='CSCI2130', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4520(
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
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4534", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3236', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4534(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4535", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3432', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4535(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4537", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI5332', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4537(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI4539", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI5332', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI4539(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5130", semester='SU'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5130(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5230", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='STAT1401', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5230(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5330", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3236', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH2242', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5330(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5331", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3232', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3341', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5331(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5332", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5332(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5335", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5335(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5380", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5380(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5430", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI5330', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5430(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5431", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI2120', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI5332', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5431(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5436", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3432', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5436(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5437", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI3230', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3236', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5437(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5438", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI5437', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5438(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
    
    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5530", semester='O'),
            AS.prerequisite1 << prerequisite(course_name='CSCI5330', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI5335', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI5432', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5530(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5531", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI1302', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='CSCI3432', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5531(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5532", semester='F'),
            AS.prerequisite1 << prerequisite(course_name='CSCI5332', grade=L('C') | L('B') | L('A'))
        )
    )
    def can_register_CSCI5532(
        self, 
        registration, 
        prerequisite1):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

    # @Rule(
    #     AND(
    #         AS.registration  << registration(course_name="CSCI5333", semester='F'),
    #         AS.prerequisite1 << prerequisite(course_name='MATH1441', grade=L('C') | L('B') | L('A')),
    #         AS.prerequisite2 << prerequisite(course_name='MATH2130', grade=L('C') | L('B') | L('A')),
    #         AS.prerequisite3 << prerequisite(course_name='CSCI1301', grade=L('C') | L('B') | L('A'))
    #     )
    # )
    # def can_register_CSCI5333(
    #     self, 
    #     registration, 
    #     prerequisite1,
    #     prerequisite2,
    #     prerequisite3):
    #     if(self.how == True):
    #         print("Since semester is ",registration['semester'])
    #         print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
    #         print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
    #         print("Since ", prerequisite3['course_name']," was passed with ", prerequisite3['grade'])
    #         print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
    #     else:
    #         print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])

    @Rule(
        AND(
            AS.registration  << registration(course_name="CSCI5538", semester='S'),
            AS.prerequisite1 << prerequisite(course_name='CSCI5332', grade=L('C') | L('B') | L('A')),
            AS.prerequisite2 << prerequisite(course_name='MATH1441', grade=L('C') | L('B') | L('A')),
        )
    )
    def can_register_CSCI5538(
        self, 
        registration, 
        prerequisite1,
        prerequisite2):
        if(self.how == True):
            print("Since semester is ",registration['semester'])
            print("Since ", prerequisite1['course_name']," was passed with ", prerequisite1['grade'])
            print("Since ", prerequisite2['course_name']," was passed with ", prerequisite2['grade'])
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")
        else:
            print("Can register for: ",registration["course_name"]," during semester: ",registration['semester'])
            self.results.write("Can register for: " + registration["course_name"] + " during semester: " + registration['semester'] + "\n")

##################################
#         Build Knowledge Base   #
##################################
        
engine = KE()
engine.reset()
transcript = open('transcript.txt', 'r')
for line in transcript.readlines():
    course_no_match = re.findall("([A-Z]{4} [0-9]{4})", line)
    grade_match = re.findall("( [A-Z]{1})", line)[0].replace(" ", "")
    if course_no_match and grade_match:
        course_no = course_no_match[0].replace(" ", "")
        grade = grade_match[0].replace(" ", "")
        print("Reading course: ", course_no, "grade :", grade, " from transcript.txt")
        engine.declare(prerequisite(course_name=course_no, grade=grade))

##################################
#         Build Working Memory   #
##################################

semester  = input("please enter the semester that you wish to register for S, SU, F or O: \n")

if sys.argv[1] == 'how':
    engine.how = True
    courses = open("course_no.txt", 'r')
    for course in courses.readlines():
        print("We will check registration for course: %s semester: %s" % (course.rstrip(), semester))
        engine.declare(registration(course_name=course.rstrip(), semester=semester))


##################################
#         Run Inference Engine   #
##################################
engine.run()