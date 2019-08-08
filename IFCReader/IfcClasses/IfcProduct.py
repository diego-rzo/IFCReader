from IfcObject import IfcObject


class IfcProduct(IfcObject):

    def __init__(self, globalId, ownerHistory, name, description, objectType,
                 objectPlacement, representation):
        IfcObject.__init__(self, globalId, ownerHistory, name,
                           description, objectType)
        self.objectPlacement = objectPlacement
        self.representation = representation
