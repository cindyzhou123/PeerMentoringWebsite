class Picture(object):
    def __init__(self, imageID):
        self._imageID = imageID
        self._status = "Waiting"
        self._approver = "No one"
    
    @property
    def imageID(self):
        return self._imageID
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    @property
    def approver(self):
        return self._approver
    
    @approver.setter
    def approver(self, admin):
        self._approve = admin