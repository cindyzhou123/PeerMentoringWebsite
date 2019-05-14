class Mentee(object):
    def __init__(self,zID, group):
        self._zID = zID
        self._group = group
    
    @property
    def zID(self):
        return self._zID
    
    @property
    def group(self):
        retuen self._group
    