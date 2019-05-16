from picture import Picture

class ImageGallery(object):
    def __init__(self):
        self._pictures = []
    
    @property
    def pictures(self):
        return self._pictures
    
    def add_picture(self, new_pic):
        self.pictures.append(new_pic)
    
    def get_picture(self, imageID):
        for picture in self.pictures:
            if(picture.imageID == imageID):
                return picture
        return NULL
