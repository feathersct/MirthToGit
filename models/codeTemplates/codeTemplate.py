class CodeTemplate:
    def __init__(self, uXml):
        self.id = uXml.find('id').text
        self.name = uXml.find('name').text
        self.revision = uXml.find('revision').text
        self.properties = uXml.find('properties')
        self.lastModified = uXml.find('./lastModified/time').text
        self.contextSet = uXml.find('contextSet')