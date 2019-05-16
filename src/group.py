from users import Users, Mentee, Mentor

class Group(object):
    def __init__(self, groupID, mentor):
        self._groupID = groupID
        self._mentor = mentor
        self._mentee = []
        self._picture = []

    @property
    def groupID(self):
        return self._groupID
    
    @property
    def mentor(self):
        return self._mentor
    
    @property
    def mentee(self):
        return self._mentee
    
    @property
    def picture(self):
        return self._picture

    def add_mentee(self, mentee):
        self.mentee.append(mentee)
    
    def add_picture(self, picture):
        self.picture.append(picture)

        