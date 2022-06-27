import xml.etree.ElementTree as ET

from models.codeTemplates.codeTemplate import CodeTemplate

class CodeTemplates:
    def __init__(self, listXML):
        codeTemplates = ET.fromstring(listXML)
        self.codeTemplates = []

        for ct in codeTemplates.findall('./codeTemplate'):
            self.codeTemplates.append(CodeTemplate(ct))