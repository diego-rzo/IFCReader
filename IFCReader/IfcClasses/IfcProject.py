from IfcObject import IfcObject


class IfcProject(IfcObject):

    def __init__(self, globalId, ownerHistory, name, description, objectType,
                 longName, phase, representationContext, unitsInContext):
        IfcObject.__init__(self, globalId, ownerHistory, name,
                           description, objectType)
        self.longName = longName
        self.phase = phase
        self.representationContext = representationContext
        self.unitsInContext = unitsInContext
