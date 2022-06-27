from xml.etree import ElementTree
import xml.etree.ElementTree as ET

class MirthElement:
    def __init__(self, uXml):
        if type(uXml).__name__ != 'Element':
            self.root = ET.fromstring(uXml)
        else:
            self.root = uXml
    
    def xmlString(self):
        return ElementTree.tostring(self.root, encoding='utf8', method='xml').decode()