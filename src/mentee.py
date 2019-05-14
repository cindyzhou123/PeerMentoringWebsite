class Mentee(object):
    def __init__(self,zID, group):
        self._zID = zID
        self._group = group
        self._tag = 2
        self._availability = {}
    
    @property
    def zID(self):
        return self._zID
    
    @property
    def group(self):
        return self._group

    @property
    def tag(self):
        return self._tag

    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self, availability):
        self._availability = availability