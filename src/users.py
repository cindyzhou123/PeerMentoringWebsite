class Users():
    def __init__(self, zID):
        self._zID = zID
        self._groupID = 0
    
    @property
    def zID(self):
        return self._zID

    @property
    def group(self):
        return self._group
    
    @group.setter
    def group(self, groupID):
        self.groupID = groupID

class Mentee(Users):
    def __init__(self,zID):
        super().__init__(zID)
        self._tag = 2
        self._availability = {}

    @property
    def tag(self):
        return self._tag

    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self, availability):
        self._availability = availability

class Mentor(Users):
    def __init__(self,zID):
        super().__init__(zID)
        self._tag = 1
    
    @property
    def tag(self):
        return self._tag
    