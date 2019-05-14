class Admin(object):
    def __init__(self):
        self._password = "PeerMentoringIsGreat"
        self._tag = 3
    
    @property
    def password(self):
        return self._password
    
    @property
    def tag(self):
        return self._tag