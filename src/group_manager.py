class GroupManager(object):
    def __init__(self):
        self._groups = []

    @property
    def groups(self):
        return self._groups
    
    def add_group(self, group):
        self.groups.append(group)