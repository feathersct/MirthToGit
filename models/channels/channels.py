import xml.etree.ElementTree as ET
from models.channels.channel import Channel

class Channels:
    def __init__(self, listXML):
        channels = ET.fromstring(listXML)
        self.channels = []

        for c in channels.findall('./channel'):
            self.channels.append(Channel(c))