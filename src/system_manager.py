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
    
    def get_user_by_ID(self, zID):
        for mentor in self.mentors:
            if(mentor.zID == zID):
                return mentor
            
        for mentee in self.mentees:
            if(mentee.zID == zID):
                return mentee
                
        return NULL
    
    def get_group_by_ID(self, groupID):
        for group in self.groups:
            if(group.groupID == groupID):
                return group
        
        return NULL
    
    def get_user_by_name(self, name):
        for mentor in self.mentors:
            if(mentor.name == name):
                return mentor
            
        for mentee in self.mentees:
            if(mentee.name == name):
                return mentee
                
        return NULL
    
    def get_group_by_name(self, name):
        for group in self.groups:
            if(group.name == name):
                return group
        
        return NULL