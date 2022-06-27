import xml.etree.ElementTree as ET
from models.mirthElement import MirthElement
from models.users.user import User

class Users(MirthElement):
    def __init__(self, userListXml):
        MirthElement.__init__(self, userListXml)
        users = self.root
        self.users = []

        for u in users.findall('./user'):
            self.users.append(User(u))