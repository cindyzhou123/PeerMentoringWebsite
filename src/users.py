class Users():
    def __init__(self, zID):
        self._zID = zID
        self._groupID = 0
    
    @property
    def zID(self):
        return self._zID

    @property
    def groupID(self):
        return self._groupID
    
    @groupID.setter
    def groupID(self, groupID):
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
    
    def __str__(self):
        output_string = "Mentee:\n"
        output_string += "  Tag:"
        output_string += str(self.tag)
        output_string += "\n"
        output_string += "  zID:"
        output_string += str(self.zID)
        output_string += "\n"
        output_string += "  group:"
        if(self.groupID == 0):
            output_string += "UNDEFINED\n"
        else:
            output_string += str(self.groupID)
        output_string += "\n"

        return output_string

class Mentor(Users):
    def __init__(self,zID):
        super().__init__(zID)
        self._tag = 1
    
    @property
    def tag(self):
        return self._tag
    
    def __str__(self):
        output_string = "Mentor:\n"
        output_string += "  Tag:"
        output_string += str(self.tag)
        output_string += "\n"
        output_string += "  zID:"
        output_string += str(self.zID)
        output_string += "\n"
        output_string += "  group:"
        if(self.groupID == 0):
            output_string += "UNDEFINED\n"
        else:
            output_string += str(self.groupID)
        output_string += "\n"

        return output_string
