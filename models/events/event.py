from models.mirthElement import MirthElement


class Event(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.id = self.root.find('id').text
        self.dateTime = self.root.find('dateTime').text
        self.eventTime = self.root.find('./eventTime/time').text
        self.level = self.root.find('level').text
        self.name = self.root.find('name').text
        self.outcome = self.root.find('outcome').text
        self.userId = self.root.find('userId').text
        self.ipAddress = self.root.find('ipAddress').text if self.root.find('ipAddress') != None else None
        self.serverId = self.root.find('serverId').text
        # self.root = uXml

        self.attributes = []
        for a in self.root.findall('./attributes/entry'):
            self.attributes.append((a.findall('string')[0].text, a.findall('string')[1].text))