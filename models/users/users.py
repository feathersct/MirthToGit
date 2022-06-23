import xml.etree.ElementTree as ET
from models.users.user import User

class Users:
    def __init__(self, userListXml):
        users = ET.fromstring(userListXml)
        self.users = []

        for u in users.findall('./user'):
            self.users.append(User(u))