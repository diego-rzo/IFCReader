from IfcRoot import IfcRoot


class IfcRelationship(IfcRoot):

    def __init__(self, globalId, ownerHistory, name, description):
        IfcRoot.__init__(self, globalId, ownerHistory, name, description)
