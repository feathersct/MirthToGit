from models.mirthElement import MirthElement


class LinkedHashMap(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.entry = []

        for e in self.root.findall('./entry'):
            self.entry.append(Entry(e))

class Entry(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        strings = self.root.findall('./string')
        lists = self.root.findall('./lists')
        self.string = []
        self.list = []
        
        for e in strings:
            self.string.append(e.text)

        for e in lists:
            s = []
            for o in e.findall('./string'):
                s.append(o.text)
            self.list.append(s)

