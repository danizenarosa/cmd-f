from datetime import time

class Day:
    def __init__(self, day):
        
        self.name = day; 
        self.allSections = [] # all sections that have not yet been scheduled 
        self.schedSections = [] # scheduled sections
        self.mustSections = {} # sections that were scheduled from preceding days
        self.latestEndTime = time(0, 0)

