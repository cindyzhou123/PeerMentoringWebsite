class Group(object):
    def __init__(self, group_num, mentor):
        self._group_num = group_num
        self._mentor = mentor
        self._mentee = []
        self._picture = []

    @property
    def group_num(self):
        return self._group_num
    
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

        