class Event:
    def __init__(self, uXml):
        self.id = uXml.find('id').text
        self.dateTime = uXml.find('dateTime').text
        self.eventTime = uXml.find('./eventTime/time').text
        self.level = uXml.find('level').text
        self.name = uXml.find('name').text
        self.outcome = uXml.find('outcome').text
        self.userId = uXml.find('userId').text
        self.ipAddress = uXml.find('ipAddress').text if uXml.find('ipAddress') != None else None
        self.serverId = uXml.find('serverId').text

        self.attributes = []
        for a in uXml.findall('./attributes/entry'):
            self.attributes.append((a.findall('string')[0].text, a.findall('string')[1].text))