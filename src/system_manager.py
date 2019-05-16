class SystemManager(object):
    def __init__(self):
        self._groups = []
        self._mentees = []
        self._mentors = []

    @property
    def groups(self):
        return self._groups
    
    @property
    def mentees(self):
        return self._mentees

    @property
    def mentors(self):
        return self._mentors
    
    def add_group(self, group):
        self.groups.append(group)

    def add_mentee(self, mentee):
        self.mentees.append(mentee)
    
    def add_mentor(self, mentor):
        self.mentors.append(mentor)
    
    def get_mentor(self, zID):
        for mentor in self.mentors:
            if(mentor.zID == zID):
                return mentor
                
        return NULL
    
    def get_group(self, groupID):
        for group in self.groups:
            if(group.groupID == groupID):
                return group
        
        return NULL