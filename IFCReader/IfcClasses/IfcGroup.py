from IfcObject import IfcObject


class IfcGroup(IfcObject):

    def __init__(self, globalId, ownerHistory, name, description, objectType):
        IfcObject.__init__(self, globalId, ownerHistory, name,
                           description, objectType)
