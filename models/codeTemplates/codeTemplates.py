import xml.etree.ElementTree as ET

from models.codeTemplates.codeTemplate import CodeTemplate
from models.mirthElement import MirthElement

class CodeTemplates(MirthElement):
    def __init__(self, listXML):
        MirthElement.__init__(self, listXML)
        codeTemplates = self.root
        self.codeTemplates = []

        for ct in codeTemplates.findall('./codeTemplate'):
            self.codeTemplates.append(CodeTemplate(ct))