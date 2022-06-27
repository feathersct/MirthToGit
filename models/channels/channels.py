import xml.etree.ElementTree as ET
from models.channels.channel import Channel
from models.mirthElement import MirthElement

class Channels(MirthElement):
    def __init__(self, listXML):
        MirthElement.__init__(self, listXML)

        channels = self.root
        self.channels = []

        for c in channels.findall('./channel'):
            self.channels.append(Channel(c))