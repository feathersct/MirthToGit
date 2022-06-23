class User:
    def __init__(self, userXml):
        self.id = userXml.find('id').text
        self.username = userXml.find('username').text
        self.email = userXml.find('email').text
        self.firstName = userXml.find('firstName').text
        self.lastName = userXml.find('lastName').text
        self.organization = userXml.find('organization').text
        self.description = userXml.find('description').text
        self.phoneNumber = userXml.find('phoneNumber').text
        self.strikeCount = userXml.find('strikeCount').text