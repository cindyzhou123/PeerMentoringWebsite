from admin import Admin
from image_gallery import ImageGallery
from picture import Picture

class AdminPortal(object):
    def __init__(self, system, gallery):
        self._access_pw = "PeerMentoringIsGreat"
        self._system = system
        self._gallery = gallery
        self._admin = []
    
    @property
    def access_pw(self):
        return self._access_pw
    
    @property
    def system(self):
        return self._system
    
    @property
    def admin(self):
        return self._admin
    
    @property
    def gallery(self):
        return self._gallery
    
    def add_admin(self, admin):
        self.admin.append(admin)
    
    def get_picture_to_approve(self):
        list_to_approve = []

        for image in self.gallery:
            if (image.status == "Waiting"):
                list_to_approve.append(image)
        
        return list_to_approve
    
    def get_admin(ID):
        for staff in self.admin:
            if(staff.ID == ID):
                return staff
        return NULL
    
    def approve_picture(self, pictureID, adminID):
        picture = self.gallery.get_picture(pictureID)
        admin = self.get_admin(adminID)

        picture.status = "Approved"
        picture.approver = admin

    def reject_picture(self, pictureID, adminID):
        picture = self.gallery.get_picture(pictureID)
        admin = self.get_admin(adminID)

        picture.status = "Rejected"
        picture.approver = admin

