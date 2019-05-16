class Admin(object):
    def __init__(self, staffID):
        self._ID = staffID
        self._key = "originalkey"
    
    @property
    def ID(self):
        return self._ID
    
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, new_key):
        self._key = new_key