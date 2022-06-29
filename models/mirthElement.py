from xml.etree import ElementTree
import xml.etree.ElementTree as ET


class MirthElement:
    def __init__(self, uXml):
        if not isinstance(uXml, ET.Element):
            self.root = ET.fromstring(uXml)
        else:
            self.root = uXml
    
    def xmlString(self):
        return ElementTree.tostring(self.root, encoding='utf8', method='xml').decode()

    def getSafeText(self, prop: str) -> str:
        return self.root.find(prop).text if self.root.find(prop) != None else None