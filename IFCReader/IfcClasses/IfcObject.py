from IfcObjectDefinition import IfcObjectDefinition


class IfcObject(IfcObjectDefinition):

    def __init__(self, globalId, ownerHistory, name, description, objectType):
        IfcObjectDefinition.__init__(self, globalId, ownerHistory,
                                     name, description)
        self.objectType = objectType
